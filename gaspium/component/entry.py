import tkinter as tk
from collections import namedtuple
from gaspium import Component, error


class Entry(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._entry = None
        self._strvar_entry = tk.StringVar()
        self._strvar_title = tk.StringVar()

    def build(self, parent=None, title="Entry field", text=None, focus=False,
              width=20, secretive=False, readonly=False, on_submit=None,
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
        # entry
        show = None
        if secretive:
            show = "x"
        state = "readonly" if readonly else "normal"
        self._entry = tk.Entry(self._body, width=width, show=show,
                         state=state, textvariable=self._strvar_entry)
        self._entry.pack(anchor="w", fill=fill)
        self._strvar_entry.set(text if text else "")
        # set focus
        if focus:
            self._entry.focus_set()
        # on submit
        if on_submit:
            info = self._gen_info()
            command = (lambda event, on_submit=on_submit, info=info: on_submit(info))
        else:
            command = None
        self._entry.bind("<Return>", command)

    def read(self):
        return self._strvar_entry.get()

    def update(self, title=None, text=None, focus=None, readonly=None):
        if title is not None:
            self._strvar_entry.set(title)
        if text is not None:
            self._strvar_entry.set(text)
        if readonly is not None:
            state = "readonly" if readonly else "normal"
            self._entry.config(state=state)
        if focus is True:
            self._entry.focus_set()

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
