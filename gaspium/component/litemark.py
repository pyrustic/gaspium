import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from collections import namedtuple
from gaspium import Component, error
import litemark


class Litemark(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._strvar_title = tk.StringVar()
        self._text_widget = None
        self._viewer = None

    def build(self, parent=None, title=None, text=None, path=None, root=None,
              style=None,
              width=45, height=10, side=tk.LEFT, anchor="nw",
              padx=5, pady=5, expand=False, fill=None):
        # parent
        parent = self._get_parent(parent)
        # body
        self._body = tk.Frame(parent)
        self._body.pack(side=side, anchor=anchor, padx=padx,
                        pady=pady, expand=expand, fill=fill)
        # set title
        if title is not None:
            self._strvar_title.set(title)
            title_label = tk.Label(self._body, textvariable=self._strvar_title)
            title_label.pack(anchor="nw", pady=(0, 2))
        # create text widget
        self._text_widget = ScrolledText(self._body, width=width, height=height,
                                         bg="white", wrap="word")
        self._text_widget.pack(fill=fill, expand=expand)
        self._viewer = litemark.Viewer(widget=self._text_widget, root=root,
                                       style=style)
        if text:
            self._viewer.render(text)
        elif path:
            self._viewer.open(path)
        self._viewer.readonly = True

    def read(self):
        if self._text_widget:
            return self._text_widget.get("1.0", tk.END)
        return None

    def update(self, title=None, text=None):
        if title is not None:
            self._strvar_title.set(title)
        if text is not None:
            self._viewer.clear()
            self._viewer.render(text)
            self._viewer.readonly = True

    def _gen_info(self):
        Info = namedtuple("Info", ("app", "pid", "page", "cid", "component"))
        info = Info(self._page.app, self._page.pid, self._page, self._cid, self)
        return info

    def _get_parent(self, parent=None):
        if not parent:
            if self._page.frame:
                return self._page.frame
            else:
                return self._page.body
        if isinstance(parent, str):
            component = self._page.components.get(parent)
            if not component:
                msg = "Component ID '{}' not found !".format(parent)
                raise error.ComponentNotFoundError(msg)
            return component.body
        return parent
