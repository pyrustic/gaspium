"""This module exposes the default components classes (Button, Frame, Table, et cetera.)"""
from gaspium.component.frame import Frame
from gaspium.component.button import Button
from gaspium.component.choice import Choice
from gaspium.component.entry import Entry
from gaspium.component.optionmenu import OptionMenu
from gaspium.component.editor import Editor
from gaspium.component.image import Image
from gaspium.component.label import Label
from gaspium.component.litemark import Litemark
from gaspium.component.pathfield import PathField
from gaspium.component.spinbox import SpinBox
from gaspium.component.table import Table
#  TODO: add Slider and Tree

__all__ = ["Frame", "Button", "Choice", "Entry", "OptionMenu",
           "Editor", "Image", "Label", "Litemark", "PathField",
           "SpinBox", "Table"]
