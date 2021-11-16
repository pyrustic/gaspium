import tkinter as tk
from collections import namedtuple
from gaspium import Component, error


class Label(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._icon = None
        self._label = None
        self._strvar_text = tk.StringVar()

    def build(self, parent=None, text="This is a Label", color="tomato",
              font_family="Liberation Mono", font_size=15, font_weight="bold",
              icon=None, compound=tk.LEFT, on_click=None, side=tk.LEFT,
              anchor="nw", padx=5, pady=5, expand=False, fill=None):
        # parent
        parent = self._get_parent(parent)
        # keep a reference to icon
        self._icon = icon
        # fill text stringvar
        if text:
            self._strvar_text.set(text)
        # font
        font = (font_family, font_size, font_weight)
        # create label
        self._label = tk.Label(parent, textvariable=self._strvar_text,
                         foreground=color, font=font,
                         image=icon, compound=compound)
        self._label.pack(side=side, anchor=anchor, padx=padx, pady=pady,
                          expand=expand, fill=fill)
        self._body = self._label

    def read(self):
        return None

    def update(self, text=None):
        # update text
        if text is not None:
            self._strvar_text.set(text)

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
