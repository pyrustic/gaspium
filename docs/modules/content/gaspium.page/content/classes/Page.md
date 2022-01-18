Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

> **gaspium.page**
> 
> This Page class is defined inside this module.
>
> **Classes:** &nbsp; [Page](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.page/content/classes/Page.md#class-page) &nbsp; [View](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.page/content/classes/View.md#class-view)
>
> **Functions:** &nbsp; [get\_info\_instance\_1](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.page/content/functions.md#get_info_instance_1) &nbsp; [get\_info\_instance\_2](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.page/content/functions.md#get_info_instance_2)
>
> **Constants:** &nbsp; None

# Class Page
This is the definition of the Page class

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|app|getter|Returns the app reference||
|app|setter|Set the app reference||
|body|getter|Return the body reference||
|components|getter|Returns the dictionary of components.
The dictionary keys are CIDs (Component ID)||
|data|getter|Empty dictionary linked to this page. Store inside it whatever you want.||
|frame|getter|Return the current Frame container for components||
|frame|setter|Update the current Frame container for components||
|name|getter|Returns the page name||
|on_close|getter|Return the on_close callback||
|on_close|setter|Set the on_close callback||
|on_open|getter|Return the on_open callback||
|on_open|setter|Set the on_open callback||
|pid|getter|Returns the page id||
|pid|setter|Set the page id||
|private_close_method|getter|Returns the method reference to close this page.
You shouldn't use this method !||
|private_open_method|getter|Internal method !
Returns the method reference to open this page.||
|scrolling|getter|Returns the scrolling value||



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [\_before\_after\_widget](#_before_after_widget) &nbsp; [\_check\_component\_keyword](#_check_component_keyword) &nbsp; [\_close](#_close) &nbsp; [\_consume\_todo](#_consume_todo) &nbsp; [\_open](#_open) &nbsp; [add](#add) &nbsp; [hide](#hide) &nbsp; [new\_cid](#new_cid) &nbsp; [read](#read) &nbsp; [scroll](#scroll) &nbsp; [toast](#toast) &nbsp; [unhide](#unhide) &nbsp; [update](#update)

## \_\_init\_\_
Init.




**Signature:** (self, pid=None, name='Page', scrolling='vertical', on\_open=None, on\_close=None)

|Parameter|Description|
|---|---|
| pid| String, the PID (Page ID) of this page should be unique. If you don't set a PID,|
| name| string, the name of this page.|
| scrolling| should be one of these values: None, "vertical", "horizontal".|
| on\_open| the callback to call when this page is opened. This callback must accept|
| on\_close| the callback to call when this page is about to close. This callback must accept|



**Return Value:** None

[Back to Top](#module-overview)


## \_before\_after\_widget
No description



**Signature:** (self, widget)



**Return Value:** None

[Back to Top](#module-overview)


## \_check\_component\_keyword
No description



**Signature:** (self, operation, kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_close
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_todo
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_open
This method shouldn't be called by you



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## add
Add a new component to this page.




**Signature:** (self, component\_class, cid=None, \*\*config)

|Parameter|Description|
|---|---|
| component\_class| the component class, example: 'gaspium.component.Button'|
| cid| the CID (Component ID) of the component. This CID should be unique.|
| \*\*config| the options to configure this component.|



**Return Value:** The CID

[Back to Top](#module-overview)


## hide
Hide a given component already installed on this page.




**Signature:** (self, cid)

|Parameter|Description|
|---|---|
| cid| the CID (Component ID) of the component to hide|



**Return Value:** None

[Back to Top](#module-overview)


## new\_cid
Generate a new valid CID (Component ID).
The CID string follow this pattern: "cid-x", with x being an integer.




**Signature:** (self)



**Return Value:** A new valid CID

[Back to Top](#module-overview)


## read
Read the contents of a given component already installed on this page.




**Signature:** (self, cid, \*\*kwargs)

|Parameter|Description|
|---|---|
| cid| the CID (Component ID) of the component|
| \*\*kwargs| optional keyword-arguments|



**Return Value:** The value returned by the component

[Back to Top](#module-overview)


## scroll
Scrolls the page.
For orient == "x", set value to:
    - 0: to scroll to left
    - 1: to scroll to right
For orient == "y", set value to:
    - 0: to scroll to top
    - 1: to scroll to bottom




**Signature:** (self, orient='y', value=1)

|Parameter|Description|
|---|---|
| orient| "x" or "y" to scroll horizontally or vertically|
| value| float value between 0 and 1|



**Return Value:** None

[Back to Top](#module-overview)


## toast
Displays a toast that will last for x milliseconds (duration)




**Signature:** (self, message, duration=1000, blocking=False)

|Parameter|Description|
|---|---|
| message| the message string to show|
| duration| integer, milliseconds before the toast closes itself.|
| blocking| boolean to tell if whether you want the flow to block while|



**Return Value:** None

[Back to Top](#module-overview)


## unhide
Unhide a previously hidden component




**Signature:** (self, cid)

|Parameter|Description|
|---|---|
| cid| the CID (Component ID)|



**Return Value:** None

[Back to Top](#module-overview)


## update
Update the contents of a given component already installed on this page.




**Signature:** (self, cid, \*\*config)

|Parameter|Description|
|---|---|
| cid| the CID (Component ID) of the component|
| \*\*config| options to configure this component|



**Return Value:** Value returned by the component

[Back to Top](#module-overview)



