<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/cover.png" alt="Demo" width="920">
    <p align="center">
    <i> </i>
    </p>
</div>

# Gaspium
**Framework to build Python apps with the GASP metaphor**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Demo](#demo) . [Latest](https://github.com/pyrustic/gaspium/tags) . [Documentation](https://github.com/pyrustic/gaspium/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview)
- [App](#app)
- [Page](#page)
- [Command line aware](#command-line-aware)
- [Batteries included](#batteries-included)
- [Installation](#installation)
- [Demo](#demo) 

# Overview
**Gaspium** is a framework that allows you to create applications with the **GASP** (**G**UI **A**s **S**tapled **P**ages) metaphor. 

In short, we define **pages** to which we add graphical **components**. Then we add these **pages** to an instance of the **App** class. The first **page** added is de facto the **home page** and it will be open when the application is started. Adding a **page** makes it automatically referenced in the application's **navigation bar**. You can open an arbitrary **page** of your application directly from the **command line**.

**Gaspium** serves as the reference implementation of the **GASP concept**. 

**Discover the [GASP concept](https://github.com/pyrustic/gaspium/blob/master/gasp.md) !**

# App

It is the main class of the Framework. An instance of the App class represents the running application. It is to this instance that the developer adds Pages.

```python
from gaspium import App


app = App()

# ...
# Here you add pages to the app
# The first page is considered the home page
# ...

# The last line starts the app (mainloop)
# The home page will open automatically
app.start()
```
The `App` class accepts arguments like the theme to use, the geometry of the window, whether the caching should be enabled or not, et cetera. The `App` class also has the `add` method to add a page to the application, `open` method to open a page, `start` method to start the application, `exit` method to exit the application, et cetera.

> **Read the App [documentation](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.app/content/classes/App.md#class-app).**

# Page
A **Page** is either a function or a [Viewable](https://github.com/pyrustic/viewable) subclass. Each Page added to the App instance is either manually or automatically assigned a unique page identifier, the PID, and automatically referenced in the navigation bar. A page is rebuilt or not at each opening depending on whether the `caching` feature has been activated or not.

```python
import tkinter as tk
from viewable import Viewable
from gaspium import App


def home_page(context):
    """Home Page. Must accept the dto argument"""
    # the dto contains some useful objects
    app = context.app
    pid = context.pid
    data = context.data
    root = context.root
    # the page function must returns the body
    # i.e. the graphical container of the page
    body = tk.Frame(root)
    label = tk.Label(body, text="Home")
    label.pack()
    return body


class LoginPage(Viewable):
    """
    Login Page
    """

    def __init__(self, context):
        """
        The constructor must accept the dto argument
        """
        super().__init__()
        # the dto contains some useful objects
        self._app = context.app
        self._pid = context.pid
        self._data = context.data
        self._root = context.root
        # the body of the page
        self._body = None

    def _build(self):
        self._body = tk.Frame(self._root)
        label = tk.Label(self._body, text="Login")
        label.pack()


def on_open_home(context):
    """
    This on_open callback must accept a dto object
    """
    # redirect to login_page
    # instead of letting the home_page open
    app = context.app
    app.open("login")


app = App(caching=False)

# Add home_page and bind the 'on_open_home' callback
# to perform a custom redirection to login_page
app.add(home_page, title="Home", on_open=on_open_home)

# Add login_page (it won't be referenced in the navigation bar)
app.add(LoginPage, pid="login", title="Login", indexable=False)

# The home page will open automatically
app.start()
```

**Play with the [Demo](https://gist.github.com/pyrustic/79c9ee0efde8c06b7d4685f3c58b7761).**

# Command line aware

By default, when you run a GASP application, the first page added to the App instance opens as the home page. It is possible to open an arbitrary page of the application from the command line. To do this, just put its PID (Page ID) as an argument on the command line. The strings entered after the identifier are considered as data to be sent to the page when it is opened.

```bash
$ my-app login "Alex Rustic"
# the login page will open
```

# Batteries included
**Gaspium** comes with a handful of useful lightweight packages.

| Name | Description |
| --- | --- |
| [Backstage](https://github.com/pyrustic/backstage) | Extensible command line tool for managing software projects |
|[Cyberpunk-Theme](https://github.com/pyrustic/cyberpunk-theme) | A modern `dark theme` for Python apps|
| [Shared](https://github.com/pyrustic/shared) | Data exchange and persistence |
| [Subrun](https://github.com/pyrustic/subrun) | Intuitive API to safely start and communicate with processes in Python |
| [TkStyle](https://github.com/pyrustic/tkstyle) | Library to create styles and themes for Python apps |
| [Megawidget](https://github.com/pyrustic/megawidget) | Collection of megawidgets to build graphical user interfaces for Python apps |
| [Viewable](https://github.com/pyrustic/viewable) | Python library to implement a GUI view with lifecycle |
| [Threadom](https://github.com/pyrustic/threadom) | Tkinter-compatible multithreading |
| [Suggestion](https://github.com/pyrustic/suggestion) | Democratizing auto-complete(suggest) for Python desktop applications |
| [Kurl](https://github.com/pyrustic/kurl) | Konnection URL: HTTP requests in Python with an implementation of conditional request and a responses caching system |

# Installation
**Gaspium** is **cross platform** and versions under **1.0.0** will be considered **Beta** at best. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on **Python 3.5** or **newer**.

## For the first time

```bash
$ pip install gaspium
```

## Upgrade
```bash
$ pip install gaspium --upgrade --upgrade-strategy eager
```


# Demo
A demo is available to play with as a **Github Gist**. Feel free to give a feedback in the comments section.

**Play with the [Demo](https://gist.github.com/pyrustic/79c9ee0efde8c06b7d4685f3c58b7761).**

<br>
<br>
<br>

[Back to top](#readme)
