Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

> **gaspium.app**
> 
> The App class is defined inside this module.
>
> **Classes:** &nbsp; [App](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.app/content/classes/App.md#class-app) &nbsp; [View](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.app/content/classes/View.md#class-view)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class View
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

## Base Classes
viewable.Viewable

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|body|getter|Get the body of this view.|viewable.Viewable|
|state|getter|Return the current state of the Viewable instance.
States are integers, you can use these constants:
    - pyrustic.view.NEW: the state just after instantiation;
    - pyrustic.view.BUILT: the state after the call of _built
    - pyrustic.view.MAPPED: the state after the call of on_map
    - pyrustic.view.DESTROYED: the state after the call of on_destroy|viewable.Viewable|



# All Methods
[\_viewable\_\_bind\_destroy\_event](#_Viewable__bind_destroy_event) &nbsp; [\_viewable\_\_bind\_map\_event](#_Viewable__bind_map_event) &nbsp; [\_viewable\_\_binding](#_Viewable__binding) &nbsp; [\_viewable\_\_build](#_Viewable__build) &nbsp; [\_viewable\_\_run\_on\_destroy](#_Viewable__run_on_destroy) &nbsp; [\_viewable\_\_run\_on\_map](#_Viewable__run_on_map) &nbsp; [\_\_init\_\_](#__init__) &nbsp; [\_build](#_build) &nbsp; [\_on\_destroy](#_on_destroy) &nbsp; [\_on\_map](#_on_map) &nbsp; [\_set\_title](#_set_title) &nbsp; [build](#build) &nbsp; [build\_grid](#build_grid) &nbsp; [build\_pack](#build_pack) &nbsp; [build\_place](#build_place) &nbsp; [build\_wait](#build_wait) &nbsp; [destroy](#destroy) &nbsp; [populate\_menubar](#populate_menubar)

## \_Viewable\_\_bind\_destroy\_event
No description

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_Viewable\_\_bind\_map\_event
No description

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_Viewable\_\_binding
No description

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_Viewable\_\_build
No description

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_Viewable\_\_run\_on\_destroy
No description

**Inherited from:** viewable.Viewable

**Signature:** (self, event=None)



**Return Value:** None

[Back to Top](#module-overview)


## \_Viewable\_\_run\_on\_map
No description

**Inherited from:** viewable.Viewable

**Signature:** (self, event=None)



**Return Value:** None

[Back to Top](#module-overview)


## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self, app, root, todo\_on\_map, on\_exit)



**Return Value:** None

[Back to Top](#module-overview)


## \_build
Build the view here by defining the _body instance



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_on\_destroy
Put here the code that will be executed at destroy event



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_on\_map
Put here the code that will be executed once
the body is mapped.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_set\_title
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## build
Build this view object. It returns the body 

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## build\_grid
Build this view then grid it 

**Inherited from:** viewable.Viewable

**Signature:** (self, cnf=None, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## build\_pack
Build this view then pack it 

**Inherited from:** viewable.Viewable

**Signature:** (self, cnf=None, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## build\_place
Build this view then place it 

**Inherited from:** viewable.Viewable

**Signature:** (self, cnf=None, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## build\_wait
Build this view then wait till it closes.
The view should have a tk.Toplevel as body 

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## destroy
Destroy the body of this view 

**Inherited from:** viewable.Viewable

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## populate\_menubar
No description



**Signature:** (self, pid, page, category)



**Return Value:** None

[Back to Top](#module-overview)



