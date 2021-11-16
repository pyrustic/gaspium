Back to [Modules overview](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md)
  
# Module documentation
>## gaspium.page.\_\_init\_\_
No description
<br>
[classes (2)](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.page.__init__/classes.md)


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

    def __init__(self, page):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    @property
    def master(self):
        """
        
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

```

