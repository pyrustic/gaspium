Back to [Modules overview](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md)
  
# Module documentation
>## gaspium.app.\_\_init\_\_
No description
<br>
[classes (1)](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.app.__init__/classes.md)


## Classes
```python
class App(object):
    """
    This is the entry point of your Gaspium app
    """

    def __init__(self, title='Application', width=800, height=500, theme=<cyberpunk_theme.Cyberpunk object at 0x7fd2371dcfa0>, caching=False, resizable=(False, True), on_exit=None):
        """
        Parameters
        ==========
        - title: string, the title of the app
        - width: int, the width of the app
        - height: int, the height of the app
        - scrolling: the orient of the scrollbar, "vertical", "horizontal", "both".
        - theme: the theme, i.e. an instance of tkstyle.Theme
        - on_exit: the on_exit handler, ie a function that will be called on exit.
        """

    @property
    def body(self):
        """
        Body frame
        """

    @property
    def caching(self):
        """
        Return a boolean to indicate if the caching option is True or False.
        By default, caching is set to False.
        """

    @caching.setter
    def caching(self, val):
        """
        Set True if you want pages to be cached. Cached pages retains their data.
        By default, caching is set to False.
        """

    @property
    def data(self):
        """
        Dictionary Data linked to this app
        """

    @property
    def height(self):
        """
        Return the height of the app
        """

    @height.setter
    def height(self, val):
        """
        Set the height of the app
        """

    @property
    def home(self):
        """
        
        """

    @property
    def on_exit(self):
        """
        Return the on_exit handler
        """

    @on_exit.setter
    def on_exit(self, val):
        """
        Set the on_exit handler. The handler is a function that accepts no argument
        """

    @property
    def page(self):
        """
        Return the currently opened page
        """

    @property
    def pages(self):
        """
        Return an internal dictionary that contains pages. Keys are pages ids
        """

    @property
    def resizable(self):
        """
        Return the resizable tuple state
        """

    @resizable.setter
    def resizable(self, val):
        """
        
        """

    @property
    def root(self):
        """
        root
        """

    @property
    def theme(self):
        """
        Return the current theme
        """

    @theme.setter
    def theme(self, val):
        """
        Set a theme, ie, a themebase.Theme instance
        """

    @property
    def title(self):
        """
        Return the title of the app
        """

    @title.setter
    def title(self, val):
        """
        Set the title of the app
        """

    @property
    def width(self):
        """
        Return the width of the app
        """

    @width.setter
    def width(self, val):
        """
        Set the width of the app
        """

    def add(self, page, indexable=True, category=None):
        """
        Add a page to the app.
        Parameters
        ==========
            - page: an instance of gaspium.page.Page
            - indexable: boolean, if False, the page won't be indexed in the menubar
            - category: string, the menu category name under
             which the page is indexed
        
        Returns the pid
        
        Raises gaspium.error.DuplicatePageError if the pid already exists
        """

    def exit(self):
        """
        Exit the app
        """

    def new_pid(self):
        """
        
        """

    def open(self, pid, data=None):
        """
        Open a page specified by its pid
        Raise gaspium.error.PageNotFoundError if not page is associated to this PID
        Raise gaspium.error.NestedOpeningError if you try to open a new page inside
        on_open and on_close callbacks
        """

    def start(self):
        """
        Start the app. Mainloop here.
        """

    def _handle_open_page_from_cli(self):
        """
        
        """

    def _setup(self):
        """
        
        """

    def _todo(self):
        """
        
        """

```

