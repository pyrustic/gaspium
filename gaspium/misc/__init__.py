import sys
import tkinter as tk
from collections import namedtuple
from viewable import Viewable


class EnhanceTk:
    """ Ctrl-a in an Entry or Text doesn't make a text selection by default.
        Now it's possible ! Enjoy ! """

    def __init__(self, root_tk):
        root_tk.bind_class("Entry", "<Control-a>", self._select_all_in_entry, "+")
        root_tk.bind_class("Text", "<Control-a>", self._select_all_in_text, "+")

    def _select_all_in_entry(self, event):
        widget = event.widget
        widget.focus()
        widget.select_range(0, tk.END)
        widget.icursor(tk.END)

    def _select_all_in_text(self, event):
        widget = event.widget
        widget.tag_add(tk.SEL, "1.0", tk.END)


class Navbar:
    def __init__(self, app):
        self._app = app
        self._root = app.root
        self._menubar = None
        self._menu_cache = []
        self._menu_map = {}

    def add(self, pid, title, category):
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

    def _ensure_menubar(self):
        if self._menubar:
            return
        # set menubar
        self._menubar = tk.Menu(self._root)
        self._root.config(menu=self._menubar)


def create_context_1(app, root, pid, data):
    """Used in the context of Page creation:
        - to call "on_open" callback
        - to instantiate a view class or to call a view function"""
    Context = namedtuple("Context", ("app", "root", "pid", "data"))
    return Context(app, root, pid, data)


def create_context_2(app, root, pid, body):
    """ Used for 'on_close' call"""
    Context = namedtuple("Info", ("app", "root", "pid", "body"))
    return Context(app, root, pid, body)


def check_cli_request():
    pid = data = None
    request = sys.argv[1:]
    if request:
        pid = request[0]
        data = None
        if len(request) > 1:
            data = tuple(request[1:])
    return pid, data


def get_view_type(view):
    view_type = "function"
    try:
        if issubclass(view, Viewable):
            view_type = "class"
    except TypeError as e:
        pass
    return view_type


def default_help_page(info):
    info.app.root.iconify()
    print("Application built with Gaspium")
    print("https://github.com/pyrustic/gaspium")
    print()
    print("Available Pages:")
    pages = " ".join(info.app.pages.keys())
    print(pages)
    info.app.exit()
