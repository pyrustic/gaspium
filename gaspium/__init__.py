"""Main module exposing the classes 'App', 'Page', and the module 'component' that contains default components."""
from gaspium.app import App
from gaspium.page import Page
from gaspium.page import error


__all__ = ["App", "Page", "Component"]


class Component:
    """
    Base class to create a Component class like the ones in 'gaspium.component'.
    """
    def __init__(self, page, cid):
        self._page = page
        self._cid = cid
        self._body = None
        self._parts = dict()

    @property
    def page(self):
        """
        Get the page instance.
        """
        return self._page

    @property
    def cid(self):
        """
        Get the CID (Component ID).
        """
        return self._cid

    @property
    def body(self):
        """
        Get the body of this component.
        """
        return self._body

    @property
    def parts(self):
        """
        Get the parts of this component.
        """
        return self._parts.copy()

    def build(self, **config):
        """
        Method to call to build this component.
        This method must create the body of this component and assign it to 'self._body'.
        This method should also update the 'parts' property.

        [parameters]
        - **config: options to configure this component.
         This configuration include the five keywords of the layout mechanism
         ('parent', 'side', 'anchor', 'fill', and 'expand').
        """
        pass

    def read(self, **kwargs):
        """
        Method to read the contents of this component.

        [parameters]
        - **kwargs: keyword-arguments.

        [return value]
        The contents of this component.
        """
        pass

    def update(self, **config):
        """
        Method to update this component.

        [parameters]
        - **config: options to configure this component.

        [return value]
        None or something else.
        """
        pass
