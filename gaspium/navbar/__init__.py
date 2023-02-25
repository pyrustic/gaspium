import tkinter as tk


class Navbar:
    def __init__(self, app):
        self._app = app
        self._root = app.root
        self._menubar = None
        self._menu_cache = []
        self._menu_map = {}

    def attach(self, pid, title, category):
        self._ensure_menubar()
        command = (lambda self=self, pid=pid:
                   self._app.open(pid))
        if category:
            if category in self._menu_map:
                menu = self._menu_map[category]
            else:
                menu = tk.Menu(self._menubar, tearoff=0)
                self._menu_map[category] = menu
                self._menubar.add_cascade(label=category,
                                          menu=menu)
            menu.add_command(label=title,
                             command=command)
        else:
            if title in self._menu_map:
                menu = self._menu_map[title]
            else:
                menu = self._menubar
            menu.add_command(label=title,
                             command=command)

    def detach(self, pid):
        pass

    def _ensure_menubar(self):
        if self._menubar:
            return
        # set menubar
        self._menubar = tk.Menu(self._root)
        self._root.config(menu=self._menubar)
