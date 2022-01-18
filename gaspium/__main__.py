"""Demo. Note: this demo needs an image that is only on my computer."""
from gaspium import App, Page
from gaspium.component import Frame, Label, Choice, Button, Editor, Entry, Table, Image, SpinBox, PathField, OptionMenu
from cyberpunk_theme.widget.button import get_button_dark_style, get_button_dark_filled_style, get_button_blue_style, get_button_blue_filled_style, get_button_green_style, get_button_green_filled_style, get_button_yellow_style, get_button_yellow_filled_style, get_button_red_style, get_button_red_filled_style


TEXT = """\
Hello Friend !

This GUI is built with Gaspium.

Gaspium: high-productivity framework to build Python apps.

This project is part of the Pyrustic Open Ecosystem.



                      	Join the Pyrustic Open Ecosystem !

	                   https://pyrustic.github.io       

"""


def get_home_page(app):
    page = Page(name="Home", scrolling=None)
    # Row 1
    page.add(Frame, cid="frame1")
    # radiobbutons
    items = ("TkF", "Gaspium", "Shared", "TkStyle", "Litemark",
             "Backstage", "Cyberpunk-Theme", "Threadom",
             "Megawidget", "Viewable", "...")
    page.add(Choice, parent="frame1",
             title="Pyrustic Ecosystem", flavor="radio", items=items, selection=1)
    # Editor
    page.add(Editor, parent="frame1", fill="both", expand=True, text=TEXT)
    # Choices
    items = ("Python", "Desktop", "Frontend", "Backend", "Distribution",
             "Megawidgets", "Multithreading   ", "Theme|Style",
             "Autocomplete", "Productivity", "Bullshit", "More...")
    page.add(Choice, parent="frame1", flavor="check", items=items,
             selection=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11))

    # Row 2
    page.add(Frame, cid="frame2")
    # table
    headers = ("Mountain", "Height", "Planet")
    data = [["Everest", "8,848", "Earth"],
            ["Skil Brum", "7,410", "Mars"],
            ["Abi Gamin", "7,355", "Venus"],
            ["Mana Peak", "7,272", "Krypton"],
            ["Karjiang", "7,221", "Tao-Hung"]]
    megaconfig = {"listboxes_columns": {"width": 14, "height": 6}}
    page.add(Table, parent="frame2", headers=headers, data=data,
             megaconfig=megaconfig)
    # image
    page.add(Frame)
    try:
        with open("/home/alex/demo-img.png", "rb") as file:
            img = file.read()
        page.add(Image, parent="frame2", image=img, anchor="center", fill="x", expand=1)
    except Exception as e:
        pass
    # Row 3
    page.add(Frame, cid="frame3")
    # entry
    # --
    page.add(Frame, parent="frame3", side="left")
    page.add(Entry, title="Name", side="top", text="Alex Rustic")
    page.add(Entry, title="Password", secretive=True, text="Password", side="top")
    # --
    page.add(Frame, parent="frame3", side="left")
    page.add(Entry, title="GitHub", side="top", text="github.com/pyrustic", readonly=True)
    page.add(OptionMenu, title="Options", side="top", items=("Item 1", "Item 2"))
    # --
    page.add(Frame, parent="frame3", side="left")
    page.add(PathField, title="Path", side="top", path="/home/alex/demo")
    page.add(SpinBox, title="Duration", side="top", prompt="3.141592653")
    # --
    page.add(Frame, parent="frame3", side="right", anchor="s")
    page.add(Label, side="right", text="{GASP}", color="#242a2f", anchor="center", font_size=58)

    # Row 4
    page.add(Frame, cid="frame4", side="bottom")
    page.add(Button, parent="frame4", style=get_button_dark_style())
    page.add(Button, parent="frame4", style=get_button_dark_filled_style())
    page.add(Button, parent="frame4", style=get_button_blue_style())
    page.add(Button, parent="frame4", style=get_button_blue_filled_style())
    page.add(Button, parent="frame4", style=get_button_green_style())
    page.add(Button, parent="frame4", style=get_button_green_filled_style())
    page.add(Button, parent="frame4", style=get_button_yellow_style())
    page.add(Button, parent="frame4", style=get_button_yellow_filled_style())
    page.add(Button, parent="frame4", style=get_button_red_style())
    page.add(Button, parent="frame4", style=get_button_red_filled_style())
    return page


def get_process_page(app):
    page = Page(name="Process")
    return page


def get_about_page(app):
    page = Page(name="About")
    return page


def get_row_1(app):
    pass


def main():
    """Demo"""
    app = App(width="920", height="537")

    home_page = get_home_page(app)
    app.add(home_page)

    process_page = get_process_page(app)
    app.add(process_page)

    about_page = get_about_page(app)
    app.add(about_page)


    app.start()


if __name__ == "__main__":
    main()
