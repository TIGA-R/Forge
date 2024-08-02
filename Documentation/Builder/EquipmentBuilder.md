# Equipment Builder
## Summary
To move further towards providing the customer with equipment building capabilities, as well as speeding up and improving the reliability of new tag equipment building, the following method for equipment SCADA production has been developed. The new method is a minimal interface, requiring only a few key pieces of data to automatically produce the desired equipment. The information required mirrors those requested by the field, namely:
1) The desired name of the new equipment
2) The equipment type `adaptor` object, described below
3) The device on which the equipment is programmed
4) The unique instance values for the equipment
	- e.g. Valve Number, or Well Number + LP/HP

## Syntax
### Class
**EquipmentBuilder(name, equipment_adaptor, device_path, \[equipment_parameter], \[equipment_parameter_2])**
- Parameters
	`String` name - The name of the equipment to be built. This will be the name of the tag, as well as the initial metadata name
	`Object` equipment_adaptor - A class object providing configuration information about the equipment. 
	`String` device_path - Full Tag Path of the `remote device` that the equipment is wired to
	`Int` (Optional) equipment_parameter - First parameter of the associated equipment, as defined by the equipment adaptor. `None`(default) if no equipment parameters are defined for the equipment adaptor
	`Int` (Optional) equipment_parameter_2 - Second parameter of the associated equipment, as defined by the equipment adaptor. `None`(default) if a second equipment parameter is not defined for the equipment adaptor

### Methods
**build(\[enabled], \[scada_id], \[merrick_id], \[third_party_xref], \[third_party_group], \[procount_export])**
- Parameters
	`Bool` (optional) enabled - Enable or disable equipment on generation, including tag and metadata. `True` (default)
	`String` (optional) scada_id - Scada ID entered into the metadata. `''` (default)
	`Int` (optional) merrick_id - Merrick ID entered into the metadata. `0` (default)
	`String` (optional) third_party_xref - Third Party Xref value entered into the metadata. `''` (default)
	`String` (optional) third_party_group- Third Party Group value entered into the metadata. `''` (default)
	`Bool` (optional) procount_export - enable or disable procount export on equipment. `False` (default)

### Equipment Adaptor
A class object adding equipment-type-specific implementation details. The following information must be supplied:
- Properties
	- `String` folder - The subfolder in which the equipment tag should be placed
	- `String` suffix - The label to append to the end of the site tamplate tag
	- `String` equipment_parameter\[\_2] - The parameter name on which to assign equipment parameters during instance generation
	- `String` \[device_type]\_template - The path to the template for a given device type from which to inherit from for the template tag
#### device_dict configuration
The \[device_type] referenced above is a call to the value assigned from the `device_dict` at the beginning of the `Meta.Tag.config` file. For each `remote device` `template tag`, a device_dict `key`/`value` pair must be added, which associates the `device type` to the `remote device tag`.
##### Example
```python
device_dict = {  
'Emerson FB 3000 v01': 'fb3000',  
}
```
## Code Examples
### Python - Build Valve Equipment

```python
# Import EquipmentBuilder class from library
from Meta.Tag.Make import EquipmentBuilder  
# Import the Equipment Adaptor from the config page
from Meta.Tag.config import VALVE  

equip_builder = EquipmentBuilder(
	'Sparky H01 Control Valve', # Name of the equipment
	VALVE, # Adaptor Object for the equipment type
	'[North01]North/North01/Sparky Sundevil/Sparky Sundevil/Remote Device/SPARKY_SUNDEVIL_RD', # Tagpath of the remote device (captured by 'copy path' on tag explorer)
	1 # equipment parameter number. In this case, PID number
)  
# Build object below. No metadata is provided in this case, and so default entries are generated
equip_builder.build()
```

### Python - Generate Equipment Adaptor
```python
class VALVE:  
    folder = 'Valve' # Instance folder location defined 
    suffix = 'Valve' # Template tag suffix defined 
    equipment_parameter = '_Valve Num' # Parameter to populate on instance generation of the builder defined
    fb3000_template = 'VALVE/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Valve' # Core template location defined. Remove preceeding tag provider definition (e.g. North01/_TYPES_/)
```
