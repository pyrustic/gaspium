Back to [Modules overview](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md)
  
# Module documentation
>## gaspium.app.\_\_init\_\_
No description
<br>
[classes (2)](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.app.__init__/classes.md)


## Classes
```python
class App(object):
    """
    This is the entry point of your Gaspium app
    """

    def __init__(self, title='Application', width=800, height=500, theme=<cyberpunk_theme.Cyberpunk object at 0x7feab7644250>, caching=False, resizable=(False, True), on_exit=None):
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

```python
class View(viewable.Viewable):
    """
    Subclass this if you are going to create a view.
    
    Lifecycle of a view:
        1- you instantiate the view
        2- '__init__()' is implicitly called
        3- you call the method '.build()'
        4- '_build()' is implicitly called
        5- '_on_map()' is implicitly called once the widget is mapped
        6- '_on_destroy()' is implicitly called when the widget is destroyed/closed
    
    The rules to create your view is simple:
    - You need to subclass Viewable.
    - You need to implement the methods '_build()', and optionally
        implement '_on_map()' and '_on_destroy()'.
    - You need to set an instance variable '_body' with either a tk.Frame or tk.Toplevel
        in the method '_on_build()'
    That's all ! Of course, when you are ready to use the view, just call the 'build()' method.
    Calling the 'build()' method will return the body of the view. The one that you assigned
    to the instance variable '_body'. The same body can be retrieved with the property 'body'.
    The 'build()' method should be called once. Calling it more than once will still return
    the body object, but the view won't be built again.
    You can't re-build your same view instance after destroying its body.
    You can destroy the body directly, by calling the conventional tkinter destruction method
     on the view's body. But it's recommended to destroy the view by calling the view's method
     'destroy()' inherited from the class Viewable.
    The difference between these two ways of destruction is that when u call the Viewable's
     'destroy()' method, the method '_on_destroy()' will be called BEFORE the effective
     destruction of the body. If u call directly 'destroy' conventionally on the tkinter
     object (the body), the method '_on_destroy()' will be called AFTER the beginning
      of destruction of the body.
    
      By the way, you can use convenience methods "build_pack", "build_grid", "build_place"
      to build and pack/grid/place your widget in the master !!
      Use "build_wait" for toplevels if you want the app to wait till the window closes
    """

    def __init__(self, app, root, todo_on_map, on_exit):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    # inherited from viewable.Viewable
    @property
    def state(self):
        """
        Return the current state of the Viewable instance.
        States are integers, you can use these constants:
            - pyrustic.view.NEW: the state just after instantiation;
            - pyrustic.view.BUILT: the state after the call of _built
            - pyrustic.view.MAPPED: the state after the call of on_map
            - pyrustic.view.DESTROYED: the state after the call of on_destroy
        """

    # inherited from viewable.Viewable
    def build(self):
        """
        Build this view object. It returns the body 
        """

    # inherited from viewable.Viewable
    def build_grid(self, cnf=None, **kwargs):
        """
        Build this view then grid it 
        """

    # inherited from viewable.Viewable
    def build_pack(self, cnf=None, **kwargs):
        """
        Build this view then pack it 
        """

    # inherited from viewable.Viewable
    def build_place(self, cnf=None, **kwargs):
        """
        Build this view then place it 
        """

    # inherited from viewable.Viewable
    def build_wait(self):
        """
        Build this view then wait till it closes.
        The view should have a tk.Toplevel as body 
        """

    # inherited from viewable.Viewable
    def destroy(self):
        """
        Destroy the body of this view 
        """

    def populate_menubar(self, pid, page, category):
        """
        
        """

    def _build(self):
        """
        Build the view here by defining the _body instance
        """

    def _on_destroy(self):
        """
        Put here the code that will be executed at destroy event
        """

    def _on_map(self):
        """
        Put here the code that will be executed once
        the body is mapped.
        """

    def _set_title(self):
        """
        
        """

```

