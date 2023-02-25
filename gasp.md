# GASP: GUI As Stapled Pages

## 1. Introduction

Two functions are enough to know to make a command line application: the function to display text and the function to retrieve the input entered by the user. Building an app with a graphical user interface is a bit more complicated than that, as you need to know what widgets to use and the settings to configure them, think about the user experience, create the layout, smartly separate the GUI code from the rest of the project, et cetera. Thus, GUI programming is difficult.

Solutions are proposed to simplify GUI programming. For example, there are GUI builders that allow the developer to arrange graphical control elements using a drag-and-drop WYSIWYG editor, software design patterns such as MVC that allows splitting the logic of a program in three interconnected elements, et cetera. These two examples indicate that there are different angles for dealing with the difficulty of GUI programming. So there is an opportunity to propose a new solution.

In this document, I propose a new GUI programming metaphor based on something we already know. I'm inspired by the fact that the desktop metaphor implemented in computers is based on something we already know, the physical desktop, which makes using a computer intuitive even for someone who isn't tech-savvy.

This new GUI programming metaphor is freely implementable in different programming languages and is suitable for a wide range of projects, from simple projects to complex projects.

## 2. Stapled Pages Metaphor

Imagine an application designed to solve three tasks A, B and C. This application is divided into three independent modules. We will use the term 'page' to refer to the user interface exposed by each of the modules. The application displays one page at a time and has a navigation bar to switch between pages. On each page are arranged graphical components with which the user interacts.


<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/gasp.png" alt="Figure" width="674">
    <p align="center">
    <i> GUI As Stapled Pages (GASP) </i>
    </p>
</div>

The developer of this application simply has to define the pages. It is not concerned with the implementation of the navigation bar. The user should be able to run the app like a traditional monolithic software or arbitrarily open a page from the command line. Again, the developer is not concerned with the implementation of this "command line aware" feature. It should be easy to import and open in one application an arbitrary page exposed by another application, much like stapling a new sheet to a document.

For this, we need a lightweight framework that allows the developer to create GASP (GUI As Stapled Pages) applications. In the same way that CLI programming welcomes newcomers with two simple Input and Print functions, using a GASP framework is simply defining Pages which are functions or classes and then passing them to an instance of an App class. We'll briefly explore the App class and the Page concept in the next sections.

Note that in this document, examples will be written in Python, and we have to distinguish three actors of interest which are the GASP framework developer, the GASP application developer and the GASP application user.


## 3. App Class

It is the main class of the GASP Framework. An instance of the App class represents the running application. It is to this instance that the developer adds Pages.

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


The App class has at least the 'add' method to add a page to the application, 'open' method to open a page, 'start' method to start the application, and 'exit' method to exit the application. The 'open' method has a 'data' parameter which allows data to be passed from page to page.



## 4. Page

A Page is either a function or a class. Each Page added to the App instance is either manually or automatically assigned a unique page identifier, the PID, and automatically referenced in the navigation bar. A page is rebuilt or not at each opening depending on whether the 'caching' feature has been activated or not.


```python
import tkinter as tk
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
    return body


class LoginPage:
    """
    Login Page.
    This class must have a 'build' method and a 'body' property
    """
    def __init__(self, context):
        """
        The constructor must accept the dto argument
        """
        # the dto contains some useful objects
        self._app = context.app
        self._pid = context.pid
        self._data = context.data
        self._root = context.root
        # the body of the page
        self._body = None

    @property
    def body(self):
        return self._body
    
    def build(self):
        self._body = tk.Frame(self._root)

        
def on_open_home(context):
    """
    This on_open callback must accept a dto object
    """
    # redirect to login_page
    # instead of letting the home_page open
    app = context.app
    app.open("login")
    

# For more on constructor parameters, check the reference implementation
app = App(caching=True)

# Add home_page and bind the 'on_open_home' callback
# to perform a custom redirection to login_page
app.add(home_page, title="Home", on_open=on_open_home)

# Add login_page (it won't be referenced in the navigation bar)
app.add(LoginPage, pid="login", title="Login", indexable=False)

# The home page will open automatically
app.start()

```

## 5. Command Line Aware

By default, when you run a GASP application, the first page added to the App instance opens as the home page. It is possible to open an arbitrary page of the application from the command line. To do this, just put its PID (Page ID) as an argument on the command line. The strings entered after the identifier are considered as data to be sent to the page when it is opened.

```bash
$ my-app login "Alex Rustic"
# the login page will open
```

## 6. Reference Framework

A GASP framework with a permissive license was created in Python to serve as an implementation reference. The repository of this framework completes the summary content of this document. The framework is called **Gaspium**, it is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io), and it comes with batteries included (megawidgets, View with lifecyle, GUI-compatible multithreading library, data exchange and persistence library, et cetera).

> **Discover [Gaspium](https://github.com/pyrustic/gaspium#readme) !**

<br>

<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/cover.png" alt="Figure" width="920">
    <p align="center">
    <i>Demo built with <a href="https://github.com/pyrustic/gaspium">Gaspium</a> (theme: <a href="https://github.com/pyrustic/cyberpunk-theme">Cyberpunk-Theme)</a></i>
    </p>
</div>
