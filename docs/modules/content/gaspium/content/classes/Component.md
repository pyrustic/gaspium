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

# Class Component
Base class to create a Component class like the ones in 'gaspium.component'.

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|body|getter|Get the body of this component.||
|cid|getter|Get the CID (Component ID).||
|page|getter|Get the page instance.||
|parts|getter|Get the parts of this component.||



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [build](#build) &nbsp; [read](#read) &nbsp; [update](#update)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self, page, cid)



**Return Value:** None

[Back to Top](#module-overview)


## build
Method to call to build this component.
This method must create the body of this component and assign it to 'self._body'.
This method should also update the 'parts' property.




**Signature:** (self, \*\*config)

|Parameter|Description|
|---|---|
| \*\*config| options to configure this component.|



**Return Value:** None

[Back to Top](#module-overview)


## read
Method to read the contents of this component.




**Signature:** (self, \*\*kwargs)

|Parameter|Description|
|---|---|
| \*\*kwargs| keyword-arguments.|



**Return Value:** The contents of this component.

[Back to Top](#module-overview)


## update
Method to update this component.




**Signature:** (self, \*\*config)

|Parameter|Description|
|---|---|
| \*\*config| options to configure this component.|



**Return Value:** None or something else.

[Back to Top](#module-overview)



