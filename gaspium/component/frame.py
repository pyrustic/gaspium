import tkinter as tk
from gaspium import Component, error


class Frame(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)

    def build(self, color=None, width=None, height=None,
              parent=None, side=tk.TOP, anchor=tk.CENTER,
              padx=0, pady=0, expand=False, fill=tk.X):
        parent = self._get_parent(parent)
        self._body = tk.Frame(parent, background=color, width=width,
                              height=height)
        self._body.pack(side=side, anchor=anchor, padx=padx, pady=pady,
                        expand=expand, fill=fill)
        self._page.frame = self._body

    def read(self):
        pass

    def update(self, color=None):
        if color is not None:
            self._body.config(background=color)

    def _get_parent(self, parent=None):
        if not parent:
            return self._page.body
        if isinstance(parent, str):
            component = self._page.components.get(parent)
            if not component:
                msg = "Component ID '{}' not found !".format(parent)
                raise error.ComponentNotFoundError(msg)
            return component.body
        return parent
