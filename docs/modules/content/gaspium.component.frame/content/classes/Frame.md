Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

> **gaspium.component.frame**
> 
> No description
>
> **Classes:** &nbsp; [Frame](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component.frame/content/classes/Frame.md#class-frame)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Frame
Base class to create a Component class like the ones in 'gaspium.component'.

## Base Classes
gaspium.Component

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|body|getter|Get the body of this component.|gaspium.Component|
|cid|getter|Get the CID (Component ID).|gaspium.Component|
|page|getter|Get the page instance.|gaspium.Component|
|parts|getter|Get the parts of this component.|gaspium.Component|



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [\_get\_parent](#_get_parent) &nbsp; [build](#build) &nbsp; [read](#read) &nbsp; [update](#update)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self, page, cid)



**Return Value:** None

[Back to Top](#module-overview)


## \_get\_parent
No description



**Signature:** (self, parent=None)



**Return Value:** None

[Back to Top](#module-overview)


## build
Method to call to build this component.
This method must create the body of this component and assign it to 'self._body'.
This method should also update the 'parts' property.




**Signature:** (self, color=None, width=None, height=None, parent=None, side='top', anchor='center', padx=0, pady=0, expand=False, fill='x')

|Parameter|Description|
|---|---|
| \*\*config| options to configure this component.|



**Return Value:** None

[Back to Top](#module-overview)


## read
Method to read the contents of this component.




**Signature:** (self)

|Parameter|Description|
|---|---|
| \*\*kwargs| keyword-arguments.|



**Return Value:** The contents of this component.

[Back to Top](#module-overview)


## update
Method to update this component.




**Signature:** (self, color=None)

|Parameter|Description|
|---|---|
| \*\*config| options to configure this component.|



**Return Value:** None or something else.

[Back to Top](#module-overview)



