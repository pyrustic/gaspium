





















# Layout Guide

Work in progress...

[Modules documentation](https://github.com/pyrustic/gaspium/tree/master/docs/modules#readme) . [ReadMe](https://github.com/pyrustic/gaspium#readme) . [Pyrustic Open Ecosystem](https://pyrustic.github.io)




















<br><br><br>



## Example 1
```python
from gaspium import App, Page
from gaspium.component import Frame


def get_page():
    page = Page(name="Home", scrolling=None)
    page.add(Frame, color="red", expand=True, fill="both")
    page.add(Frame, color="green", expand=True, fill="both")
    page.add(Frame, color="blue", expand=True, fill="both")
    return page


app = App(width=300, height=200)
page = get_page()
app.add(page)
app.start()

```
The result:
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/gaspX.png" alt="Figure" width="674">
    <p align="center">
    <i> GUI As Stapled Pages (GASP) </i>
    </p>
</div>

## Example 2
```python
from gaspium import App, Page
from gaspium.component import Frame


def get_page():
    page = Page(name="Home", scrolling=None)
    page.add(Frame, color="blue", side="left", expand=True, fill="both")
    page.add(Frame, color="green", side="left", expand=True, fill="both")
    page.add(Frame, color="red", side="left", expand=True, fill="both")
    return page


app = App(width=300, height=200)
page = get_page()
app.add(page)
app.start()

```

The result:
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/gaspX.png" alt="Figure" width="674">
    <p align="center">
    <i> GUI As Stapled Pages (GASP) </i>
    </p>
</div>

## Example 3

```python
from gaspium import App, Page
from gaspium.component import Frame, Entry, Button
from cyberpunk_theme.widget.button import get_button_red_style


def get_page():
    page = Page(name="Home", scrolling=None)
    page.add(Frame)
    page.add(Entry, title="Name")
    page.add(Entry, title="Password", secretive=True)
    page.add(Frame)
    page.add(Button, fill="x", expand=True)
    page.add(Frame, side="bottom")
    page.add(Button, text="Quit", side="right", style=get_button_red_style())

    return page


app = App(width=400, height=200)
page = get_page()
app.add(page)
app.start()

```
The result:
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/gaspium/gaspX.png" alt="Figure" width="674">
    <p align="center">
    <i> GUI As Stapled Pages (GASP) </i>
    </p>
</div>



