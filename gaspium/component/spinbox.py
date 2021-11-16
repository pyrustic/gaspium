import tkinter as tk
from collections import namedtuple
from gaspium import Component, error


class SpinBox(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._button = None
        self._icon = None
        self._strvar_title = tk.StringVar()
        self._strvar_selection = tk.StringVar()

    def build(self, parent=None, title=None, items=None, prompt="- Select -",
              selection=None, readonly=True, on_submit=None, side=tk.LEFT, anchor="nw",
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
        # on_select handler
        if on_submit:
            info = self._gen_info()
            command = lambda event, on_submit=on_submit, info=info: on_submit(info)
        else:
            command = None
        # create OptionMenu widget
        state = "readonly" if readonly else "normal"
        self._spinbox = tk.Spinbox(self._body, textvariable=self._strvar_selection,
                             values=items, state="readonly")
        self._spinbox.pack(fill=fill, expand=expand)
        self._spinbox.config(relief="flat")
        self._spinbox.bind("<Return>", command)
        self._items = items
        # set default selection
        if selection is None:
            self._strvar_selection.set(prompt)
        else:
            self._strvar_selection.set(selection)

    def read(self):
        str_selection = self._strvar_selection.get()
        index = None
        if not self._items:
            return None
        if str_selection in self._items:
            index = self._items.index(str_selection)
        return (index, str_selection)

    def update(self, title=None):
        # update title
        if title is not None:
            self._strvar_title.set(title)

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