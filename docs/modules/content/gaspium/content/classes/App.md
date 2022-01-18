Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

> **gaspium**
> 
> Main module exposing the classes 'App', 'Page', and the module 'component' that contains default components.
>
> **Classes:** &nbsp; [App](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium/content/classes/App.md#class-app) &nbsp; [Component](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium/content/classes/Component.md#class-component) &nbsp; [Page](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium/content/classes/Page.md#class-page)
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
|body|getter|Return the Body frame of this app, i.e. the tkinter.Frame instance that serves of the body of this app||
|caching|getter|Return a boolean to indicate if the caching option is True or False.||
|caching|setter|Set True if you want pages to be cached. Cached pages retains their data.||
|data|getter|This is an empty dictionary linked to this app.
Use it to store whatever you want.
Example: you can use it to retain the information about whether the user is authenticated or not.||
|height|getter|Return the height of the app||
|height|setter|Set the height of the app||
|home|getter|Return the home page instance, i.e. the first page added to this app||
|on_exit|getter|Return the on_exit callback||
|on_exit|setter|Set the on_exit handler. The handler is a function that accepts no argument||
|page|getter|Return the currently opened page instance||
|pages|getter|Return the copy of an internal dictionary that contains pages.
Note: Keys are PIDs (Page ID)||
|resizable|getter|Return the resizable booleans tuple||
|resizable|setter|Set the resizable booleans tuple||
|root|getter|Return the root, i.e. the Tkinter's Tk instance that serves as the root of this app.||
|theme|getter|Return the current theme||
|theme|setter|Set a theme, i.e., a tkstyle.Theme instance||
|title|getter|Return the title of the app||
|title|setter|Set the title of the app||
|width|getter|Return the width of the app||
|width|setter|Set the width of the app||



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [\_handle\_open\_page\_from\_cli](#_handle_open_page_from_cli) &nbsp; [\_setup](#_setup) &nbsp; [\_todo](#_todo) &nbsp; [add](#add) &nbsp; [exit](#exit) &nbsp; [new\_pid](#new_pid) &nbsp; [open](#open) &nbsp; [start](#start)

## \_\_init\_\_
Init.




**Signature:** (self, title='Application', width=800, height=500, theme=<cyberpunk\_theme.Cyberpunk object at 0x7fe6b3565790>, caching=False, resizable=(False, True), on\_exit=None)

|Parameter|Description|
|---|---|
| title| string, the title of the app|
| width| int, the width of the app|
| height| int, the height of the app|
| theme| the theme, i.e. an instance of tkstyle.Theme|
| caching| boolean to tell if whether you want pages to be cached or built at open.|
| resizable| tuple of boolean to tell if you want the width and the height of the app to be resizable.|
| on\_exit| the on_exit handler, i.e. a function that will be called on exit.|



**Return Value:** None

[Back to Top](#module-overview)


## \_handle\_open\_page\_from\_cli
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_todo
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## add
Add a page instance to the app.




**Signature:** (self, page, indexable=True, category=None)

|Parameter|Description|
|---|---|
| page| an instance of gaspium.page.Page|
| indexable| boolean, if False, the page won't be indexed in the menubar|
| category| string, the menu category name under which the page is indexed|



**Return Value:** Returns the pid

Raises 'gaspium.error.DuplicatePageError' if the pid already exists

[Back to Top](#module-overview)


## exit
Exit the app.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## new\_pid
Generate a new valid PID (Page ID).
A PID value follows this pattern: 'pid-x', with x being an integer




**Signature:** (self)



**Return Value:** A new valid PID

[Back to Top](#module-overview)


## open
Open a page specified by its PID (Page ID).




**Signature:** (self, pid, data=None)

|Parameter|Description|
|---|---|
| pid| PID|
| data| Associated data. This data is passed to the 'on_open' callback of the page.|
| Note| If you open this page from the command line, the data passed is split into a tuple.|



**Return Value:** Raise gaspium.error.PageNotFoundError if not page is associated to this PID.
Raise gaspium.error.PageStateError if you try to open a new page inside 'on_close' callback.

[Back to Top](#module-overview)


## start
Start the app. Mainloop here.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)



