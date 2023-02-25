import sys
import tkinter as tk


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


def check_cli_request():
    pid = data = None
    request = sys.argv[1:]
    if request:
        pid = request[0]
        data = None
        if len(request) > 1:
            data = tuple(request[1:])
    return pid, data


def default_help_page(info):
    info.app.root.iconify()
    print("Application built with Gaspium")
    print("https://github.com/pyrustic/gaspium")
    print()
    print("Available Pages:")
    pages = " ".join(info.app.pages.keys())
    print(pages)
    info.app.exit()
