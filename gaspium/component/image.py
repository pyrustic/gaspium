import tkinter as tk
from collections import namedtuple
from gaspium import Component, error


class Image(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._strvar_caption = tk.StringVar()
        self._img_id = None
        self._photo_image = None

    def build(self, parent=None, image=None, caption=None,
              width=None, height=None, on_click=None,
              side=tk.LEFT, anchor="nw", padx=5, pady=5,
              expand=False, fill=None):
        # parent
        parent = self._get_parent(parent)
        # body
        self._body = tk.Frame(parent)
        self._body.pack(side=side, anchor=anchor, padx=padx,
                        pady=pady, expand=expand, fill=fill)
        # photo image
        width = 0 if width is None else width
        height = 0 if height is None else height
        self._photo_image = tk.PhotoImage(data=image,
                                    width=width,
                                    height=height)
        self._canvas = tk.Canvas(self._body,
                           width=self._photo_image.width(),
                           height=self._photo_image.height())
        self._canvas.pack()
        self._img_id = self._canvas.create_image(0, 0,
                                                 image=self._photo_image, anchor="nw")
        # label caption
        if caption is not None:
            label = tk.Label(self._body, textvariable=self._strvar_caption)
            label.pack(pady=(2, 0))
            self._strvar_caption.set(caption)
        # on click
        if on_click:
            info = self._gen_info()
            command = (lambda event, on_submit=on_click, info=info: on_submit(info))
            self._canvas.config(cursor="hand1")
        else:
            command = None
        self._canvas.bind("<Button-1>", command)

    def read(self):
        return None

    def update(self, image=None, width=None, height=None, caption=None):
        if image is not None:
            if self._img_id:
                self._canvas.delete(self._img_id)
            width = 0 if width is None else width
            height = 0 if height is None else height
            self._photo_image = tk.PhotoImage(data=image,
                                        width=width,
                                        height=height)
            self._canvas.config(width=self._photo_image.width(),
                                height=self._photo_image.height())
            self._img_id = self._canvas.create_image(0, 0,
                                                     image=self._photo_image, anchor="nw")
        if caption is not None:
            self._strvar_caption.set(caption)

    def _gen_info(self):
        Info = namedtuple("Info", ("app", "pid", "page", "cid", "component"))
        info = Info(self._page.app, self._page.pid, self._page, self._cid, self)
        return info

    def _get_parent(self, parent=None):
        if not parent:
            if self._page.frame:
                return self._page.frame
            else:
                return self._page.body
        if isinstance(parent, str):
            component = self._page.components.get(parent)
            if not component:
                msg = "Component ID '{}' not found !".format(parent)
                raise error.ComponentNotFoundError(msg)
            return component.body
        return parent
