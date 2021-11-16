import tkinter as tk
import inspect
from viewable import Viewable
from megawidget import ScrollBox, Toast
from gaspium import error
from collections import namedtuple


class Page:
    def __init__(self, pid=None, name="Page",
                 scrolling="vertical",
                 on_open=None, on_close=None):
        self._pid = pid
        self._name = name
        self._scrolling = scrolling
        self._on_open = on_open
        self._on_close = on_close
        self._app = None
        self._view = None
        self._frame = None
        self._cids_count = 0
        self._components = {}
        self._cache = []
        self._todo_cache = []
        self._hidden = {}
        self._data = {}
        self._name = name if name else str(self._pid).capitalize()

    @property
    def pid(self):
        """Returns the page id"""
        return self._pid

    @pid.setter
    def pid(self, val):
        """Set the page id"""
        if self._pid and val != self._pid:
            raise error.AlreadyDefinedError
        self._pid = val

    @property
    def name(self):
        """Returns the page name"""
        return self._name

    @property
    def scrolling(self):
        """Returns the scrolling value"""
        return self._scrolling

    @property
    def on_open(self):
        return self._on_open

    @on_open.setter
    def on_open(self, val):
        self._on_open = val

    @property
    def on_close(self):
        return self._on_close

    @on_close.setter
    def on_close(self, val):
        self._on_close = val

    @property
    def app(self):
        """Returns the app reference"""
        return self._app

    @app.setter
    def app(self, val):
        """Set the app reference"""
        if self._app and val != self._app:
            raise error.AlreadyDefinedError
        self._app = val

    @property
    def body(self):
        if self._view:
            return self._view.body.box
        return None

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, val):
        self._frame = val

    @property
    def components(self):
        """Returns the dictionary of components.
        The dictionary keys are CIDs (component id)"""
        return self._components.copy()

    @property
    def data(self):
        """Dictionary Data linked to this page"""
        return self._data

    @property
    def private_open_method(self):
        """Returns the method reference to open this page.
        You shouldn't use this method !"""
        return self._open

    @property
    def private_close_method(self):
        """Returns the method reference to close this page.
        You shouldn't use this method !"""
        return self._close

    def toast(self, message, duration=1000, blocking=False):
        """Displays a toast that will last for x milliseconds (duration)"""
        if not self._app:
            raise error.PageStateError("You must add this page to the app first")
        toast = Toast(self._app.root, message=message, duration=duration)
        if blocking:
            toast.wait_window()

    def scroll(self, orient="y", value=1):
        """
        Scrolls the page
        For orient = x:
            - 0: to scroll to left
            - 1: to scroll to right
        For orient = y:
            - 0: to scroll to top
            - 1: to scroll to bottom
        """
        if not self._app:
            raise error.PageStateError("You must add this page to the app first")
        if orient == "x":
            self._view.body.xview_moveto(value)
        else:
            self._view.body.yview_moveto(value)

    def new_cid(self):
        self._cids_count += 1
        return "cid-{}".format(self._cids_count)

    def add(self, component_class, cid=None, **config):
        """
        Standard config: new_col, side, anchor, fill, padx and pady
        Component specific config: **specific_config
        """
        if not cid:
            cid = self.new_cid()
        if cid in self._components:
            raise error.DuplicateComponentError
        if not self._view:
            operation = {"name": "add",
                         "data":
                             {
                                 "component_class": component_class,
                                 "cid": cid,
                                 "config": config
                             }
                         }
            self._todo_cache.append(operation)
            return
        component = component_class(self, cid)
        self._components[cid] = component
        self._check_component_keyword(component.build, config)
        component.build(**config)
        return cid

    def read(self, cid, **kwargs):
        try:
            component = self._components[cid]
        except KeyError as e:
            raise error.ComponentNotFoundError from None
        else:
            self._check_component_keyword(component.read, kwargs)
            return component.read(**kwargs)

    def update(self, cid, **config):
        try:
            component = self._components[cid]
        except KeyError as e:
            raise error.ComponentNotFoundError from None
        else:
            self._check_component_keyword(component.update, config)
            return component.update(**config)

    def hide(self, cid):
        try:
            component = self._components[cid]
        except KeyError as e:
            raise error.ComponentNotFoundError from None
        if not component.body:
            return
        if cid in self._hidden:
            return
        component.body.master.config(width=1, height=1)
        before, after = self._before_after_widget(component.body)
        body = component.body
        pack_info = body.pack_info()
        component.body.pack_forget()
        self._hidden[cid] = {"body": body, "pack_info": pack_info,
                             "before": before, "after": after}

    def unhide(self, cid):
        try:
            info = self._hidden[cid]
        except KeyError as e:
            return
        before, after = info["before"], info["after"]
        body = info["body"]
        pack_info = info["pack_info"]
        if before:
            pack_info.update(after=before)
        elif after:
            pack_info.update(before=after)
        body.pack(**pack_info)
        del self._hidden[cid]

    def _open(self, data=None):
        """This method shouldn't be called by you"""
        if not self._app:
            msg = "Add the page to the App instance first !"
            raise error.PageStateError(msg)
        if not self._view:
            self._view = View(self)
            self._view.build()
        self._view.body.pack(fill=tk.BOTH, expand=1, padx=0,
                             pady=(5, 0))
        # consume to-do
        self._consume_todo()
        # on open
        if self._on_open:
            Info = namedtuple("Info", ("app", "page", "pid", "data"))
            info = Info(self._app, self, self._pid, data)
            self._on_open(info)

    def _close(self):
        if self._app.caching:
            if self._on_close:
                Info = namedtuple("Info", ("app", "page", "pid"))
                info = Info(self._app, self, self._pid)
                self._on_close(info)
            self._view.body.pack_forget()
        else:
            self._view.body.pack_forget()
            self._view.destroy()
            self._view = None
            self._components = dict()

    def _before_after_widget(self, widget):
        before = None
        found = False
        after = None
        for item in widget.master.pack_slaves():
            if item is widget:
                found = True
                continue
            if found:
                after = item
                break
            before = item
        return before, after

    def _consume_todo(self):
        for operation in self._todo_cache:
            name, data = operation["name"], operation["data"]
            if name == "add":
                self.add(data["component_class"], data["cid"],
                         **data["config"])
        if self._app.caching:
            self._todo_cache = []

    def _check_component_keyword(self, operation, kwargs):
        sig = inspect.signature(operation)
        valid_keywords = [item for item, _ in sig.parameters.items()]
        for keyword, _ in kwargs.items():
            if keyword not in valid_keywords:
                msg = "Invalid option '{}'. These are valid options: {}"
                msg = msg.format(keyword, ", ".join(valid_keywords))
                raise error.ComponentInterfaceError(msg)


class View(Viewable):
    def __init__(self, page):
        super().__init__()
        self._page = page
        self._master = page.app.body

    @property
    def master(self):
        return self._master

    def _build(self):
        self._body = ScrollBox(self._master,
                               orient=self._page.scrolling)

    def _on_map(self):
        pass

    def _on_destroy(self):
        if self._page.on_close:
            self._page.on_close(self)
