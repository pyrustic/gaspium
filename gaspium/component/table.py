import tkinter as tk
from collections import namedtuple
from gaspium import Component, error
import megawidget


class Table(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._table = None
        self._strvar_entry = tk.StringVar()
        self._strvar_title = tk.StringVar()

    def build(self, parent=None, title=None,
              headers=None, data=None, orient=None, megaconfig=None,
              side=tk.LEFT, anchor="nw", padx=5, pady=5,
              expand=False, fill=None):
        # parent
        parent = self._get_parent(parent)
        # body
        self._body = tk.Frame(parent)
        self._body.pack(side=side, anchor=anchor, padx=padx,
                        pady=pady, expand=expand, fill=fill)
        # label title
        if title is not None:
            label = tk.Label(self._body, textvariable=self._strvar_title)
            label.pack(anchor="nw", pady=(0, 2))
            self._strvar_title.set(title)
       # table
        self._table = megawidget.Table(self._body, titles=headers, data=data,
                                       orient=orient, megaconfig=megaconfig)
        self._table.pack(anchor="w", fill=fill)

    def read(self):
        return None

    def update(self, title=None, text=None):
        if title is not None:
            self._strvar_entry.set(title)

    def _gen_info(self):
        Info = namedtuple("Info", ("app", "pid", "page",
                                   "cid", "component"))
        info = Info(self._page.app, self._page.pid,
                    self._page, self._cid, self)
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
