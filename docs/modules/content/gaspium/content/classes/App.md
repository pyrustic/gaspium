Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

**gaspium**
 
Main module exposing the class 'App'.

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
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|caching|getter|Return a boolean to indicate if the caching option is set to True or False.||
|caching|setter|Set True if you want pages to be cached. Cached pages retains their data.||
|clargs|getter|Command line arguments||
|data|getter|This is an empty dictionary linked to this app. Use it to store whatever you want. Example: you can use it to retain the information about whether  the user is authenticated or not.||
|failfast|getter|Get the failfast boolean||
|failfast|setter|Set the failfast boolean||
|geometry|getter|Return the geometry of the app||
|geometry|setter|Set the geometry of the app||
|history|getter|None||
|manager|getter|None||
|name|getter|Return the name of the app||
|on_exit|getter|Return the on_exit callback||
|on_exit|setter|Set the on_exit handler. The handler is a function that accepts the app instance as argument||
|on_stop|getter|Return the on_stop callback||
|on_stop|setter|Set the on_stop handler. The handler is a function that accepts the app instance as argument||
|page|getter|Return the currently opened page DTO representation||
|pages|getter|Return a dictionary of DTOs that contain pages information. Note: Keys are PIDs (Page ID)||
|pid|getter|Return the currently opened Page ID||
|resizable|getter|Return the resizable booleans tuple||
|resizable|setter|Set the resizable booleans tuple||
|root|getter|Return the root, i.e. the Tkinter's Tk instance that serves as the root of this app.||
|title|getter|Return the title of the app||
|title|setter|Set the title of the app||
|view|getter|Returns the current view||
|viewstack|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [attach](#attach) &nbsp;&nbsp; [clear\_cache](#clear_cache) &nbsp;&nbsp; [detach](#detach) &nbsp;&nbsp; [exit](#exit) &nbsp;&nbsp; [open](#open) &nbsp;&nbsp; [start](#start) &nbsp;&nbsp; [stop](#stop) &nbsp;&nbsp; [\_app\_\_restart](#_App__restart) &nbsp;&nbsp; [\_apply\_window\_config](#_apply_window_config) &nbsp;&nbsp; [\_center\_window](#_center_window) &nbsp;&nbsp; [\_close\_page](#_close_page) &nbsp;&nbsp; [\_create\_page\_info\_dto](#_create_page_info_dto) &nbsp;&nbsp; [\_destroy\_root](#_destroy_root) &nbsp;&nbsp; [\_edit\_app\_title](#_edit_app_title) &nbsp;&nbsp; [\_init\_root](#_init_root) &nbsp;&nbsp; [\_maximize\_window](#_maximize_window) &nbsp;&nbsp; [\_new\_pid](#_new_pid) &nbsp;&nbsp; [\_on\_report\_callback\_exception](#_on_report_callback_exception) &nbsp;&nbsp; [\_open\_page](#_open_page) &nbsp;&nbsp; [\_pre\_start](#_pre_start) &nbsp;&nbsp; [\_set\_title](#_set_title) &nbsp;&nbsp; [\_setup](#_setup)

## \_\_init\_\_
Initialization.




**Signature:** (self, name='app', title='Application', manager=None, geometry='800x500', remember\_geometry\_change=True, resizable=(True, True), caching=True, on\_stop=None, on\_exit=None, failfast=True, show\_page\_title=True, navbar=<class 'gaspium.navbar.Navbar'>, page\_from\_cli=True)

|Parameter|Description|
|---|---|
|name|string, unique name of this app |
|title|string, the title of the app |
|manager|the instance of a manager |
|geometry|str, to specify the geometry. Put "max" to maximize the window. Example: "800x400", "800x400+0+0", "+0+0", "max" |
|remember\_geometry\_change|boolean, to specify if the window's geometry should be remembered. |
|resizable|2-tuple of booleans to tell if you want the width and the height of the app to be resizable. |
|theme|the theme, i.e. an instance of tkstyle.Theme |
|caching|boolean to tell if whether you want pages to be cached or re-built at open. |
|on\_stop|the on_stop handler, i.e. a function that will be called when the app is going to close. This function should accept an argument: the app instance |
|on\_exit|the on_exit handler, i.e. a function that will be called when the app is going to exit. This function should accept an argument: the app instance |
|failfast|boolean, set it to True if you don't want the GUI to close when a random exception is raised |
|show\_page\_title|boolean, set True to allow the app to update the window title to show the current page title. |
|navbar|navigation bar class. The constructor must accept the app instance. The class must have an "add" method that accepts these arguments: pid, title, and category |
|page\_from\_cli|boolean, specify if pages can be opened directly from cli or not.|





**Return Value:** None

[Back to Top](#module-overview)


## attach
Attach a new page to the app. This method will generate a new page instance then
will call the layout function to complete the process




**Signature:** (self, view\_class, pid=None, title=None, category=None, indexable=True, kwargs=None)

|Parameter|Description|
|---|---|
|view\_class|a view class (i.e. a class that subclassed gaspium.Page). The Context instance is passed to the constructor of the view. |
|pid|str, the Page ID. A PID will be automatically generated if you don't set one. Note that the first added page is de facto the home page and if you don't assign a PID, the PID "home" will be assigned to it. |
|title|the title of the page. By default, it is the pid of the page |
|category|string, the menu category name under which the page is indexed |
|indexable|boolean, to tell if you want the page to be indexed on the menu bar or not. |
|kwargs|dict representing the keyword-arguments to pass to the view_class constructor. |



|Exception|Description|
|---|---|
|gaspium.error.DuplicatePageError|raised if the page id already exists |



**Return Value:** Returns the pid (Page ID)

[Back to Top](#module-overview)


## clear\_cache
Clear the cache.




**Signature:** (self, \*pid)

|Parameter|Description|
|---|---|
|\*pid|the PID(s) which cache should be erased. If you don't set any PID, the entire cache will be purged |





**Return Value:** Returns True or False

[Back to Top](#module-overview)


## detach
No description



**Signature:** (self, pid)





**Return Value:** None

[Back to Top](#module-overview)


## exit
Exit the app after calling the stop method



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## open
Open a page specified by its PID (Page ID).




**Signature:** (self, pid)

|Parameter|Description|
|---|---|
|pid|PID |



|Exception|Description|
|---|---|
|gaspium.error.PageNotFoundError|raised if not page is associated to this PID.|
|gaspium.error.PageStateError|raised if you try to open a new page inside 'on_close' callback. |



**Return Value:** the view opened

[Back to Top](#module-overview)


## start
Start the app. Mainloop here.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## stop
Stop the app, i.e. destroy the window



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_App\_\_restart
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_apply\_window\_config
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_center\_window
Center the window



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_close\_page
No description



**Signature:** (self, pid)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_page\_info\_dto
No description



**Signature:** (self, page\_info)





**Return Value:** None

[Back to Top](#module-overview)


## \_destroy\_root
No description



**Signature:** (self, event)





**Return Value:** None

[Back to Top](#module-overview)


## \_edit\_app\_title
No description



**Signature:** (self, pid)





**Return Value:** None

[Back to Top](#module-overview)


## \_init\_root
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_maximize\_window
Maximize the window



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_new\_pid
Generate a new valid PID (Page ID).
A PID value follows this pattern: 'pid-x', with x being an integer

[return value]
A new valid PID



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_on\_report\_callback\_exception
No description



**Signature:** (self, exc, val, tb)





**Return Value:** None

[Back to Top](#module-overview)


## \_open\_page
No description



**Signature:** (self, pid)





**Return Value:** None

[Back to Top](#module-overview)


## \_pre\_start
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_set\_title
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



