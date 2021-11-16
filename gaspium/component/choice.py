import tkinter as tk
import megawidget
from collections import namedtuple
from gaspium import Component, error


class Choice(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._choice = None
        self._strvar_title = tk.StringVar()

    def build(self, parent=None, title=None, items=None,
              selection=None, flavor="radio",
              stacking="vertical", on_change=None,
              side=tk.LEFT, anchor="nw",
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
        # set on_change
        if on_change:
            info = self._gen_info()
            command = (lambda choice, on_change=on_change, info=info: on_change(info))
        else:
            command = None
        # create choice megawidget
        self._choice = megawidget.Choice(self._body, items=items, selection=selection,
                                         flavor=flavor, stacking=stacking,
                                         on_change=command)
        self._choice.pack(fill=fill, expand=expand)

    def read(self):
        if self._choice:
            return self._choice.selection
        return None

    def update(self, title=None):
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
