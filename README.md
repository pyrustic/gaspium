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
- [Batteries included](#batteries-included)
- [Installation](#installation)
- [Demo](#demo) 

# Overview
**Gaspium** is a framework that allows you to create applications with the **GASP** (**G**UI **A**s **S**tapled **P**ages) metaphor. 

In short, we define **pages** to which we add graphical **components**. Then we add these **pages** to an instance of the **App** class. The first **page** added is de facto the **home page** and it will be open when the application is started.Adding a **page** makes it automatically referenced in the application's **navigation bar**. You can open an arbitrary **page** of your application directly from the **command line**.

**Gaspium** serves as the reference implementation of the **GASP concept**. 

**Discover the [GASP concept](https://github.com/pyrustic/gaspium/blob/master/gasp.md) !**



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
