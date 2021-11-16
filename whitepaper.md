# GASP: GUI As Stapled Pages

## 1. Introduction

Two functions are enough to know to make a command line application: the function to display text and the function to retrieve the input entered by the user. Building an app with a graphical user interface is a bit more complicated than that, as you need to know what widgets to use and the settings to configure them, think about the user experience, create the layout and, most importantly, write well organized code, etc. Thus, GUI programming is difficult.

The barrier to entering GUI programming isn't a big deal when you have a lot of spare time, motivation, or tools like a GUI builder for example. But unfortunately, this is not always the case and even the GUI builder is not necessarily the first choice that comes to mind. There is therefore an opportunity to propose a new solution to this situation.
    
In this document, I propose a new GUI programming metaphor that focuses on the essentials and is freely implementable in different programming languages. This metaphor is suitable for a wide range of projects, from simple projects to complex projects in a context where productivity is sought without sacrificing flexibility.
    

## 2. Stapled Pages Metaphor

Imagine an application designed to solve three tasks A, B and C. This application is divided into three modules. We will use the term 'page' to refer to the user interface exposed by each of the modules. The app displays one page at a time and has a navigation bar that makes it easy to switch between pages. Each page can have a vertical or horizontal scroll bar, or both at the same time or neither. Graphical components with which the user interacts are arranged on each page.


<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/gasp.png" alt="Figure" width="674" height="791">
    <p align="center">
    <i> GUI As Stapled Pages (GASP) </i>
    </p>
</div>

The developer of this application simply has to define the pages and arrange the graphic components on these pages. It is not concerned with the implementation of the navigation bar or the scroll bars or other features to be discovered in the next sections. For this, we need a lightweight framework that allows the developer to create GASP (GUI As Stapled Pages) applications.

A GASP framework contains three main classes which are App, Page and Component. We will briefly explore these classes in the following sections. In this document the snippet code examples will be written in Python, and we have to distinguish three actors which are the GASP framework developer, the GASP application developer and the GASP application user.


## 3. App Class

It is the main class of the GASP Framework. An instance of the App class represents the running application. It is to this instance that the developer adds instances of the Page class.

```python
from gaspium import App

app = App()
# by default the app is initialized with:
# title="Application", width=800, height=500,
# theme=Cyberpunk(), caching=False,
# resizable=(False, True), on_exit=None"""

# ...
# here you add pages to the app
# and the first page is considered the home page
# ...

# The last line starts the app (mainloop)
# The home page will open automatically
app.start()
```


The App class has at least the 'add' method to add a page to the application, 'open' to open a page, 'start' to start the application, and 'exit' to stop the application. The 'open' method has a 'data' parameter which allows data to be passed from page to page. When the application is about to be closed, the 'on_exit' callback is called.



## 4. Page Class

This class represents a page. A page instance is only added once to the App instance and can be opened multiple times. Each page is either manually or automatically assigned a unique page identifier, the pid. A page is rebuilt or not at each opening depending on whether the 'cache' feature has been activated or not at the level of the instance of the App class. When the 'cache' feature is activated, the data entered on one page is retained even when you leave the page for another.

```python
from gaspium import App, Page


app = App()

# Define and add Page A (de facto, the home page)
page_a = Page(name="Page-A")
app.add(page_a)

# Define and add Page B.
# Assign 'page-b' as page id (pid) to this page
page_b = Page(name="Page-B", pid="page-b")
app.add(page_b)

# Define and add Page C
# The pid automatically assigned to this page
# can be retrieved via its property 'pid'
page_c = Page(name="Page-C")
app.add(page_c)

# The home page will open automatically
app.start()


```

The Page class has at least the 'add' method to add a graphical component, 'read' and 'update' to respectively read and update the content of a graphical component, 'scroll' to scroll the page, 'toast' to display a message to the user, 'hide' and 'unhide' to hide or unhide a graphical component. When opening and closing a page, the 'on_open' and 'on_close' callbacks are respectively called.


## 5. Component Class

This class represents a graphical component. Each graphical component inherits from this class so that it can be added to a page. Each component instance is either manually or automatically assigned a unique component identifier, the cid. The application developer does not need to know the configuration parameters of each graphical component. It will only need to enter a dummy keyword argument and then the GASP framework will throw an exception with the list of valid configuration parameters for this graphical component.

```python
from gaspium import App, Page
from gaspium.component import Label, Entry, Button


def login(info):
    # We can retrieve via the named tuple 'info' the content of the form (username, password)
    # and then process it, update the content of the page (add another component, ...),
    # pop-up some information to the user, programmatically open another page, et cetera.
    pass


def get_page():
    page = Page()
    # Add the Label graphical component
    page.add(Label, text="Login")
    # You can change the default layout config
    # with the parameters 'parent', 'side', 'anchor', 'fill', and 'expand'
    page.add(Entry, title="Username")
    page.add(Entry, title="Password", secretive=True)
    page.add(Button, on_click=login)
    return page


app = App()

page = get_page()
app.add(page)

app.start()


```

The GASP Framework comes with a default collection of graphical components, but it is possible for the developer to create their own graphical components or to use graphical components created by other developers. Whoever creates a graphical component provides the framework with methods that will allow the framework to install the component, update and read the content of the component. The layout system is part of the configuration parameters of the graphical components, which saves the time of the application developer.


## 6. Command Line Interface

By default, when you run a GASP application, the first page that was defined in the source code opens as the home page. It is possible to open an arbitrary page of the application from the command line. To do this, just put its pid identifier as an argument on the command line. The strings entered after the identifier are considered as data to be sent to the page when it is opened. The application developer does not have to implement this feature which makes their GUI application very convenient and command-line-friendly.


## 7. Reference Framework

A GASP framework with a permissive license was created in Python to serve as an implementation reference. The repository of this framework completes the summary content of this document. The framework is called **Gaspium**, it is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io) and its repository on GitHub is accessible via https://github.com/pyrustic/gaspium.

<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/cover.png" alt="Figure" width="934" height="606">
    <p align="center">
    <i>Demo built with <a href="https://github.com/pyrustic/gaspium">Gaspium</a> (theme: <a href="https://github.com/pyrustic/cyberpunk-theme">Cyberpunk-Theme)</a></i>
    </p>
</div>



## 8. Conclusion
I have proposed a metaphor that makes several aspects of GUI programming simpler. This metaphor is encapsulated in a framework whose reference implementation called Gaspium is freely accessible on GitHub. The application developer adds graphical components on pages that represent logical units of the application. A GASP application is command-line-friendly since you can open an arbitrary page directly from the command line and even pass data to it from the command line.



_Alex Rustic_

































