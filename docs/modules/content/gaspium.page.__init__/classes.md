Back to [Modules overview](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md)
  
# Module documentation
>## gaspium.page.\_\_init\_\_
No description
<br>
[classes (1)](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.page.__init__/classes.md)


## Classes
```python
class Page(object):
    """
    
    """

    def __init__(self, pid=None, name='Page', scrolling='vertical', on_open=None, on_close=None):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def app(self):
        """
        Returns the app reference
        """

    @app.setter
    def app(self, val):
        """
        Set the app reference
        """

    @property
    def body(self):
        """
        
        """

    @property
    def components(self):
        """
        Returns the dictionary of components.
        The dictionary keys are CIDs (component id)
        """

    @property
    def data(self):
        """
        Dictionary Data linked to this page
        """

    @property
    def frame(self):
        """
        
        """

    @frame.setter
    def frame(self, val):
        """
        
        """

    @property
    def name(self):
        """
        Returns the page name
        """

    @property
    def on_close(self):
        """
        
        """

    @on_close.setter
    def on_close(self, val):
        """
        
        """

    @property
    def on_open(self):
        """
        
        """

    @on_open.setter
    def on_open(self, val):
        """
        
        """

    @property
    def pid(self):
        """
        Returns the page id
        """

    @pid.setter
    def pid(self, val):
        """
        Set the page id
        """

    @property
    def private_close_method(self):
        """
        Returns the method reference to close this page.
        You shouldn't use this method !
        """

    @property
    def private_open_method(self):
        """
        Returns the method reference to open this page.
        You shouldn't use this method !
        """

    @property
    def scrolling(self):
        """
        Returns the scrolling value
        """

    def add(self, component_class, cid=None, **config):
        """
        Standard config: new_col, side, anchor, fill, padx and pady
        Component specific config: **specific_config
        """

    def hide(self, cid):
        """
        
        """

    def new_cid(self):
        """
        
        """

    def read(self, cid, **kwargs):
        """
        
        """

    def scroll(self, orient='y', value=1):
        """
        Scrolls the page
        For orient = x:
            - 0: to scroll to left
            - 1: to scroll to right
        For orient = y:
            - 0: to scroll to top
            - 1: to scroll to bottom
        """

    def toast(self, message, duration=1000, blocking=False):
        """
        Displays a toast that will last for x milliseconds (duration)
        """

    def unhide(self, cid):
        """
        
        """

    def update(self, cid, **config):
        """
        
        """

    def _before_after_widget(self, widget):
        """
        
        """

    def _check_component_keyword(self, operation, kwargs):
        """
        
        """

    def _close(self):
        """
        
        """

    def _consume_todo(self):
        """
        
        """

    def _open(self, data=None):
        """
        This method shouldn't be called by you
        """

```

