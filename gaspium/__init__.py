from gaspium.app import App
from gaspium.page import Page
from gaspium.page import error


class Component:
    def __init__(self, page, cid):
        self._page = page
        self._cid = cid
        self._body = None
        self._parts = dict()

    @property
    def page(self):
        return self._page

    @property
    def cid(self):
        return self._cid

    @property
    def body(self):
        return self._body

    @property
    def parts(self):
        return self._parts.copy()

    def build(self, **config):
        pass

    def read(self, **kwargs):
        pass

    def update(self, **config):
        pass
