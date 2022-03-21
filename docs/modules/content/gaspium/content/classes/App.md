Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

**gaspium**
 
Main module exposing the class 'App'

> **Classes:** &nbsp; [App](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium/content/classes/App.md#class-app)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class App
This class is the entry point of your Gaspium app

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|caching|getter|Return a boolean to indicate if the caching option is set to True or False.||
|caching|setter|Set True if you want pages to be cached. Cached pages retains their data.||
|crash_resistant|getter|Get the crash_resistant boolean||
|crash_resistant|setter|Set the crash_resistant boolean||
|data|getter|This is an empty dictionary linked to this app. Use it to store whatever you want. Example: you can use it to retain the information about whether  the user is authenticated or not.||
|geometry|getter|Return the geometry of the app||
|geometry|setter|Set the geometry of the app||
|on_exit|getter|Return the on_exit callback||
|on_exit|setter|Set the on_exit handler. The handler is a function that accepts the app instance as argument||
|on_stop|getter|Return the on_stop callback||
|on_stop|setter|Set the on_stop handler. The handler is a function that accepts the app instance as argument||
|pages|getter|Return the copy of an internal dictionary that contains pages information. Note: Keys are PIDs (Page ID)||
|pid|getter|Return the currently opened Page ID||
|resizable|getter|Return the resizable booleans tuple||
|resizable|setter|Set the resizable booleans tuple||
|root|getter|Return the root, i.e. the Tkinter's Tk instance that serves as the root of this app.||
|theme|getter|Return the current theme||
|theme|setter|Set a theme, i.e., a tkstyle.Theme instance||
|title|getter|Return the title of the app||
|title|setter|Set the title of the app||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [\_apply\_theme](#_apply_theme) &nbsp;&nbsp; [\_apply\_window\_config](#_apply_window_config) &nbsp;&nbsp; [\_center\_window](#_center_window) &nbsp;&nbsp; [\_close\_page](#_close_page) &nbsp;&nbsp; [\_edit\_app\_title](#_edit_app_title) &nbsp;&nbsp; [\_init\_root](#_init_root) &nbsp;&nbsp; [\_maximize\_window](#_maximize_window) &nbsp;&nbsp; [\_new\_pid](#_new_pid) &nbsp;&nbsp; [\_on\_report\_callback\_exception](#_on_report_callback_exception) &nbsp;&nbsp; [\_open\_page](#_open_page) &nbsp;&nbsp; [\_restart](#_restart) &nbsp;&nbsp; [\_set\_title](#_set_title) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_update\_root\_background](#_update_root_background) &nbsp;&nbsp; [add](#add) &nbsp;&nbsp; [clear\_cache](#clear_cache) &nbsp;&nbsp; [exit](#exit) &nbsp;&nbsp; [open](#open) &nbsp;&nbsp; [start](#start) &nbsp;&nbsp; [stop](#stop)

## \_\_init\_\_
Initialization.




**Signature:** (self, title='Application', geometry='800x500', theme=<tkstyle.Theme object at 0x7ff48f1e31f0>, caching=False, resizable=(True, True), on\_stop=None, on\_exit=None, crash\_resistant=True, navbar=<class 'gaspium.misc.Navbar'>)

|Parameter|Description|
|---|---|
|title|string, the title of the app |
|geometry|str, to specify the geometry. Put "max" to maximize the window. Example: "800x400", "800x400+0+0", "+0+0", "max" |
|theme|the theme, i.e. an instance of tkstyle.Theme |
|caching|boolean to tell if whether you want pages to be cached or re-built at open. |
|resizable|2-tuple of booleans to tell if you want the width and the height of the app to be resizable. |
|on\_stop|the on_stop handler, i.e. a function that will be called when the app is going to close. This function should accept an argument: the app instance |
|on\_exit|the on_exit handler, i.e. a function that will be called when the app is going to exit. This function should accept an argument: the app instance |
|crash\_resistant|boolean, set it to True if you don't want the GUI to close when a random exception is raised |
|navbar|navigation bar class. The constructor must accept the app instance. The class must have an "add" method that accepts these arguments: pid, title, and category|





**Return Value:** None.

[Back to Top](#module-overview)


## \_apply\_theme
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_apply\_window\_config
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_center\_window
Center the window



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_close\_page
None



**Signature:** (self, pid)





**Return Value:** None.

[Back to Top](#module-overview)


## \_edit\_app\_title
None



**Signature:** (self, pid)





**Return Value:** None.

[Back to Top](#module-overview)


## \_init\_root
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_maximize\_window
Maximize the window



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_new\_pid
Generate a new valid PID (Page ID).
A PID value follows this pattern: 'pid-x', with x being an integer

[return value]
A new valid PID



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_on\_report\_callback\_exception
None



**Signature:** (self, exc, val, tb)





**Return Value:** None.

[Back to Top](#module-overview)


## \_open\_page
None



**Signature:** (self, pid, data)





**Return Value:** None.

[Back to Top](#module-overview)


## \_restart
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_set\_title
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_setup
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_update\_root\_background
None



**Signature:** (self, body)





**Return Value:** None.

[Back to Top](#module-overview)


## add
Add a new page to the app. This method will generate a new page instance then
will call the layout function to complete the process




**Signature:** (self, view, pid=None, title=None, category=None, indexable=True, on\_open=None, on\_close=None)

|Parameter|Description|
|---|---|
|view|either a structured view class (a Viewable subclass) or a plain view function (returning a widget). The view takes the page instance as argument. |
|pid|str, the Page ID. A PID will be automatically generated if you don't set one. Note that the first added page is de facto the home page and if you don't assign a PID, the PID "home" will be assigned to it. |
|title|the title of the page. By default, it is the pid of the page |
|category|string, the menu category name under which the page is indexed |
|indexable|boolean, to tell if you want the page to be indexed on the menu bar or not. |
|on\_open|function to call when the page is opened. It should accept an argument: the context (namedtuple) |
|on\_close|function to call when the page is closed. It should accept an argument: the context (namedtuple) |



|Exception|Description|
|---|---|
|gaspium.error.DuplicatePageError|raised if the page name already exists |



**Return Value:** ['Returns the pid (Page ID)']

[Back to Top](#module-overview)


## clear\_cache
Clear the cache.




**Signature:** (self, \*pid)

|Parameter|Description|
|---|---|
|\*pid|the PID(s) which cache should be erased. If you don't set any PID, the entire cache will be purged |





**Return Value:** ['Returns True or False']

[Back to Top](#module-overview)


## exit
Exit the app after calling the stop method



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## open
Open a page specified by its PID (Page ID).




**Signature:** (self, pid, data=None)

|Parameter|Description|
|---|---|
|pid|PID |
|data|Associated data. This data is passed to the 'on_open' callback of the page. Note: If you open this page from the command line, the data passed to the page is split into a tuple. |



|Exception|Description|
|---|---|
|gaspium.error.PageNotFoundError|raised if not page is associated to this PID.|
|gaspium.error.PageStateError|raised if you try to open a new page inside 'on_close' callback. |



**Return Value:** ['None']

[Back to Top](#module-overview)


## start
Start the app. Mainloop here.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## stop
Stop the app, i.e. destroy the window



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)



