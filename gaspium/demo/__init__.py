import tkinter as tk
from viewable import Viewable
from gaspium import App


class Home(Viewable):
    def __init__(self, context):
        super().__init__()
        self._context = context

    def _build(self, container):
        self._body = tk.Frame(container)
        text = "This is the Home Page"
        label = tk.Label(self._body, text=text, anchor="w")
        label.pack(fill=tk.X)


class Computation(Viewable):
    def __init__(self, context):
        super().__init__()
        self._context = context

    def _build(self, container):
        self._body = tk.Frame(container)
        text = "This is the Computation Page"
        label = tk.Label(self._body, text=text, anchor="w")
        label.pack(fill=tk.X)
        entry = tk.Entry(self._body)
        entry.pack()


class About(Viewable):
    def __init__(self, context):
        super().__init__()
        self._context = context

    def _build(self, container):
        self._body = tk.Frame(container)
        text = "This is the About Page"
        label = tk.Label(self._body, text=text, anchor="w")
        label.pack(fill=tk.X)


def main():
    app = App(caching=True)
    app.attach(Home, title="Home")
    app.attach(Computation, title="Computation")
    app.attach(About, title="About")
    app.start()
