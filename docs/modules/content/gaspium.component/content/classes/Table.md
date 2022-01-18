Back to [All Modules](https://github.com/pyrustic/gaspium/blob/master/docs/modules/README.md#readme)

# Module Overview

> **gaspium.component**
> 
> This module exposes the default components classes (Button, Frame, Table, et cetera.)
>
> **Classes:** &nbsp; [Button](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Button.md#class-button) &nbsp; [Choice](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Choice.md#class-choice) &nbsp; [Editor](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Editor.md#class-editor) &nbsp; [Entry](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Entry.md#class-entry) &nbsp; [Frame](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Frame.md#class-frame) &nbsp; [Image](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Image.md#class-image) &nbsp; [Label](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Label.md#class-label) &nbsp; [Litemark](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Litemark.md#class-litemark) &nbsp; [OptionMenu](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/OptionMenu.md#class-optionmenu) &nbsp; [PathField](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/PathField.md#class-pathfield) &nbsp; [SpinBox](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/SpinBox.md#class-spinbox) &nbsp; [Table](https://github.com/pyrustic/gaspium/blob/master/docs/modules/content/gaspium.component/content/classes/Table.md#class-table)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Table
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
[\_\_init\_\_](#__init__) &nbsp; [\_gen\_info](#_gen_info) &nbsp; [\_get\_parent](#_get_parent) &nbsp; [build](#build) &nbsp; [read](#read) &nbsp; [update](#update)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self, page, cid)



**Return Value:** None

[Back to Top](#module-overview)


## \_gen\_info
No description



**Signature:** (self)



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




**Signature:** (self, parent=None, title=None, headers=None, data=None, orient=None, megaconfig=None, side='left', anchor='nw', padx=5, pady=5, expand=False, fill=None)

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




**Signature:** (self, title=None, text=None)

|Parameter|Description|
|---|---|
| \*\*config| options to configure this component.|



**Return Value:** None or something else.

[Back to Top](#module-overview)



