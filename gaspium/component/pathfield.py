import tkinter as tk
from collections import namedtuple
from gaspium import Component, error
import megawidget


class PathField(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._path_field = None
        self._strvar_path = tk.StringVar()
        self._strvar_title = tk.StringVar()

    def build(self, parent=None, title="Path field", path=None,
              browse="file", initialdir=None,
                 initialfile=None,
                 mustexist=None,
                 defaultextension=None,
                 filetypes=None,
              width=20, side=tk.LEFT, anchor="nw", padx=5, pady=5,
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
        # entry
        self._path_field = megawidget.PathField(self._body,
                                                width=width,
                                                browse=browse,
                                                initialdir=initialdir,
                                                initialfile=initialfile,
                                                mustexist=mustexist,
                                                defaultextension=defaultextension,
                                                filetypes=filetypes,
                                                textvariable=self._strvar_path)
        self._path_field.pack(anchor="w", fill=fill)
        self._strvar_path.set(path if path else "")

    def read(self):
        return self._strvar_path.get()

    def update(self, title=None, path=None):
        if title is not None:
            self._strvar_title.set(title)
        if path is not None:
            self._strvar_path.set(path)

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
