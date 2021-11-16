import tkinter as tk
from collections import namedtuple
from gaspium import Component, error


class Button(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._button = None
        self._icon = None
        self._strvar_text = tk.StringVar()

    def build(self, parent=None, text="Submit", icon=None,
              compound=tk.LEFT, on_click=None, style=None,
              state="normal", side=tk.LEFT, anchor="nw",
              padx=5, pady=5, expand=False, fill=None):
        # parent
        parent = self._get_parent(parent)
        # keep a reference to icon
        self._icon = icon
        # fill text stringvar
        if text:
            self._strvar_text.set(text)
        # on_click handler
        if on_click:
            info = self._gen_info()
            command = lambda on_click=on_click, info=info: on_click(info)
        else:
            command = None
        # create button
        self._button = tk.Button(parent, textvariable=self._strvar_text,
                                 command=command, image=icon, compound=compound,
                                 cursor="hand1", state=state)
        self._button.pack(side=side, anchor=anchor, padx=padx, pady=pady,
                          expand=expand, fill=fill)
        self._body = self._button
        # styling
        if style:
            style.target(self._button)

    def read(self):
        return None

    def update(self, text=None, style=None,
               state=None):
        # update text
        if text is not None:
            self._strvar_text.set(text)
        # update style
        if style is not None:
            style.target(self._button)
        # update state
        if state is not None:
            self._button.config(state=state)

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
