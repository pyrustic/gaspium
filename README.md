<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/cover.png" alt="Demo" width="920">
    <p align="center">
    <i> </i>
    </p>
</div>

# Gaspium
**High-productivity framework to build Python apps.**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Demo](#demo) . [Latest](https://github.com/pyrustic/gaspium/tags) . [Documentation](https://github.com/pyrustic/gaspium/tree/master/docs#readme)

## Table of contents
- [Overview](#overview) 
- [App](#app) 
- [Page](#page)
- [Component](#component) 
- [Default components](default-components) 
- [Layout](#layout)
- [Command line interface](#command-line-interface)
- [Batteries included](#batteries-included)
- [Installation](#installation)
- [Demo](#demo) 

# Overview
**Gaspium** is a framework that allows you to create applications with the **GASP** (**G**UI **A**s **S**tapled **P**ages) metaphor. 

In short, we define **pages** to which we add graphical **components**. Graphical **components** are placed on a **page** with a single line of code since the layout mechanism is controlled with only five keyword arguments (**parent**, **side**, **anchor**, **fill**, and **expand**) whose defaults are sufficient in most cases.

Then we add these **pages** to an instance of the **App** class. The first **page** added is de facto the **home page** and it will be open when the application is started.

Adding a **page** makes it automatically referenced in the application's **navigation bar**.

Each graphical component can be identified with a unique **identifier** in order to be able to read its content or update it. Each page has a unique **identifier** assigned automatically or manually.

You can open an arbitrary **page** of your application directly from the **command line**.

**Gaspium** serves as the reference implementation of the **GASP concept**. You can implement the **GASP** concept in another language or with another GUI toolkit (**Gaspium** is based on **TkF** which uses **Tkinter** the default GUI toolkit of **Python**)

**Discover the [GASP concept](https://github.com/pyrustic/gaspium/blob/master/gasp.md).**


# App
It is the main class of the framework.

Here's a commented code snippet:
```python
from gaspium import App

app = App()
# by default the app is initialized with:
#   title="Application", width=800, height=500,
#   theme=Cyberpunk(), caching=False,
#   resizable=(False, True), on_exit=None"""

# ...
# here you add pages to the app
# and the first page is considered the home page
# ...

# The last line starts the app (mainloop)
# The home page will open automatically
app.start()
```

**Read the [App Guide](https://github.com/pyrustic/gaspium/blob/master/docs/guides/app.md) or play with the [Demo](#demo).**


# Page
A **page** is a view that is added to the instance of the **App** class.

Here's a commented code snippet:
```python
from gaspium import App, Page


app = App()

# Define and add Page A (de facto, the home page)
page_a = Page(name="Page-A")
app.add(page_a)

# Define and add Page B.
# Assign 'page-b' as PID (Page ID) to this page
page_b = Page(name="Page-B", pid="page-b")
app.add(page_b)

# Define and add Page C
# The PID automatically assigned to a page
# can be retrieved via the page property 'pid'
page_c = Page(name="Page-C")
app.add(page_c)

# The home page will open automatically
app.start()

```

**Read the [Page Guide](https://github.com/pyrustic/gaspium/blob/master/docs/guides/page.md) or play with the [Demo](#demo).**


# Component
A graphical **component** is a widget or group of widgets that you add to a page and with which the user interacts.

Here's a commented code snippet:
```python
from gaspium import App, Page
import gaspium.component as comp


def login(info):
    """Callback function called when the user clicks the login Button"""
    # We can retrieve via 'info' the content of the form (username, password)
    # and then process it, update the content of the page (add another component, ...),
    # pop-up some information to the user, programmatically open another page, et cetera
    pass


def get_page():
    """This function returns a page with a login form on it"""
    page = Page()
    # In the next lines we will add graphical components to make a login form.
    # This form will be made of Username, and Password text fields plus a button.
    # Note that you can control the layout mechanism with five parameters:
    # 'parent', 'side', 'anchor', 'fill', and 'expand'
    page.add(comp.Label, text="Login")
    page.add(comp.Entry, title="Username")
    page.add(comp.Entry, title="Password", secretive=True)
    page.add(comp.Button, on_click=login)
    return page


app = App()

page = get_page()
app.add(page)

app.start()

```

Also to improve the developer experience, **Gaspium** comes with a feature that helps you configure a given graphical component. Suppose you want to configure the `Label` graphical component, but you don't want to go to its documentation to see the list of valid options. You just have to pass a bogus parameter (like: `oops = True`) which will raise an exception and display the list of valid options.

**Read the [Component Guide](https://github.com/pyrustic/gaspium/blob/master/docs/guides/component.md) or play with the [Demo](#demo).**


# Default Components
The following graphical components are included by default in the **Gaspium** framework: 

`Button` `Choice` `Editor` `Entry` `Frame` `Image` `Label` `Litemark` `OptionMenu` `PathField` `SpinBox` `Table`.

**Gaspium** has been implemented to also allow developers to collaborate: it's easy to create your own components and share them with other developers as installable packages.

**Discover [Default Components](https://github.com/pyrustic/gaspium/blob/master/docs/guides/default-components.md) or [Create Your Own Component](https://github.com/pyrustic/gaspium/blob/master/docs/guides/component-creation.md).**


# Layout
Each **page** in a **GASP** app has a default frame on which whatever component you add is lay. You are free to arrange new frames on the main frame.

The layout mechanism is controlled with **five** parameters accepted by the graphical component.

|Keyword|Description|
|---|---|
|parent|The CID (Component ID) of the parent widget|
|anchor|It specifies where to position a graphical component on its parent. Valid values are the strings `'center'`, `'n'`, `'ne'`, `'e'`, `'se'`, `'s'`, `'sw'`, `'w'`, `'nw'`|
|expand|Boolean to specifies whether the component should be expanded to consume extra space in their container|
|fill|Stretch the component. Valid values are `None`, `'x'`, `'y'`, and `'both'`|
|side|Use the string values `'left'`, `'right'`, `'top'`, and `'bottom'` to specify which side of the parent the graphical component will be packed against|

**Read the [Layout Guide](https://github.com/pyrustic/gaspium/blob/master/docs/guides/layout.md) or play with the [Demo](#demo).**

# Command line interface
**Gaspium** makes your application very convenient and **command-line-friendly**.

Suppose you have created a **calc.py** application with **Gaspium**. Your app has two pages: `Calculator` and `About`. These pages are marked with the PIDs: `calculator` and `about`.

Here's how to open the `About` page directly from the command line:

```bash
$ python -m calc about
```
You can, from the command line, open an arbitrary page with data passed as an argument (provided that you have written code to process the `data` argument in the `on_open` callback of the page):

```bash
$ python -m calc calculator 34+8
```

In the last example, the Calculator page might open with its user interface populated with data passed in the command line.

**Play with the [Demo](#demo).**

# Batteries included
**Gaspium** comes with a handful of useful lightweight packages.

|Name | Description|
|---|---|
|[Shared](https://github.com/pyrustic/shared) |  Library to store, expose, read, and edit **collections** of data|
|[TkStyle](https://github.com/pyrustic/tkstyle) | Library to create **styles** and **themes** for Python apps|
|[Cyberpunk-Theme](https://github.com/pyrustic/cyberpunk-theme) | A modern **dark theme** for Python apps|
|[Winter-Theme](https://github.com/pyrustic/winter-theme) | A modern **light theme** for Python apps|
|[Litemark](https://github.com/pyrustic/litemark) | Lightweight **Markdown** dialect for Python apps|
|[Megawidget](https://github.com/pyrustic/megawidget) | Collection of **megawidgets** to build graphical user interfaces for Python apps|
|[Viewable](https://github.com/pyrustic/viewable) | Class to implement a GUI view with **lifecycle**|
|[Threadom](https://github.com/pyrustic/threadom) | Tkinter-compatible **multithreading**|
|[Suggestion](https://github.com/pyrustic/suggestion) | Democratizing **auto-complete**(suggest) for Python desktop applications|
|[Kurl](https://github.com/pyrustic/kurl) | Konnection URL: **HTTP requests** in Python with an implementation of **conditional request** and a **responses caching** system|
|[Litedao](https://github.com/pyrustic/litedao) | Library to perform intuitive interaction with **SQLite** database|
|[Probed](https://github.com/pyrustic/probed) | Probed **collections** for Python|


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

## Make your project packageable
**Backstage** is an extensible command line tool for managing software projects. By default, it supports Python, so you can run the `init` command to make your Python project [packageable](https://packaging.python.org/en/latest/tutorials/packaging-projects/):

```bash
$ cd /path/to/project
$ backstage init
Project successfully initialized !
```

You can also create a distribution package of your project with the `build` command, then publish it to [PyPI](https://pypi.org/) with the `release` command, et cetera.

**Discover [Backstage](https://github.com/pyrustic/backstage) !**


# Demo
A demo is available to play with as a **Github Gist**. Feel free to give a feedback in the comments section.

**Play with the [Demo](https://gist.github.com/pyrustic/79c9ee0efde8c06b7d4685f3c58b7761).**

<br>
<br>
<br>

[Back to top](#readme)
