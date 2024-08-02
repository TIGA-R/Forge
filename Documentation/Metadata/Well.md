# New Well Buildout
## Realtime Tag Provider Layout
Currently, a new `Well` is generated as a `UDT Tag` inside the `tag provider`, under the `Wells` folder in the associated `Pad` 
### Namespacing
For folder structuring, the tag provider is laid out in the following heirarchy:
1) `Area` 
	* `North`/`South`
2)  `Area Section` 
	* For future expansion potential. 
	* Currently only `North01`/`South01`
3) `Facility`  
	* Future facilities expected to match 1-1 the Metadata naming
	* Legacy cases exist
4)  `Pad` 
	* Future Pads expected to be a 1-1 with Facilities
	* Legacy structure have instances of {many->one} {`Facility`->`Pad`} cases
	* **FUTURE**: Heirarchy to this point to be built by Facility MetaData Scripting
5) `Equipment Type`
	* Roughly follows Metadata part type, but not strictly
	* Folder/Metadata `type` relationship:
		* `Compressor`
			* `Gas Compressor`
			* `Air Compressor`
		* `Facility`
			* `Facility`
		* `Flare`
			* `Flare`
		* `Meter`
			* `Liquid Meter`
			* `LACT Meter`
			* `Gas Meter`
		* `POC`
			* `POC`
		* `Plunger`
			* `Plunger`
		* `Remote Device`
			* `Comms`
		* `Tank`
			* `Tank`
		* `Valve`
			* `Control Valve`
		* `Vessel`
			* `Vessel`
		* `Wells` **It is recommended to build out this folder and place the well equipment object here if well data will be brought into the site.**
			* `Well`
			* `Frac Water Well`
6) `Equipment` **Also recommended to build out a well tag when well data exists for the site**
	* The functional tags which 
### Tag Provider Diagram
![image](https://github.com/user-attachments/assets/cfb6cbf8-90c6-4388-9b3e-a134b6236dd1)
## Metadata Structure
### Database Structure
Well information for Ignition is stored in the `Metadata01` database, on the `Meta_Well` table. `Meta_Well` stores data for `Well` objects. `Well` data is connected to `Facility` by PK/FK relationship:
![image](https://github.com/user-attachments/assets/5ab7cb0b-4f60-4298-9e4e-5817674c6e91)


### Generating new Well Instances
New `Well` instances are built in Metadata by script in one of two ways:

#### Meta.Site.Well.add_well
##### Description
Generates a new well instance in `Metadata`
##### Syntax
```python
Meta.Well.Well.add_well(facility_id, name, enabled=True)

```
* Parameters
	* Int `facility_id` - `primary key` -> `id` of the `Facility` object in Metadata. 
	* String `name` - The name of the `well`. 
	* Boolean `enabled` - Bit to determine if the `well` is enabled or not
* Returns:
	* Well - The instance of the Well object
##### Code Example
###### Build Well
```python
'''
This script will generate a new well instance in metadata. If the name is found in the meta_site table, you will be prompted to rename or cancel.
'''
from Meta.Well import Well
Well.new_well(1234, 'Test Well 1')

```

#### Meta.Site.Equipment.add_equipment_from_tagpath
##### Description
Generates new equipment in metadata. When used with a `well` tag, triggers a generation of a new well object if the well does not exist
##### Syntax
```python
Meta.Equipment.Equipment.add_equipment_from_tagpath(
													tagpath, 
													type=None,  
				                                    pad_identifier=None,  
				                                    well_identifier=None,
				                                    scada_id=None,  
				                                    merrick_id=None,  
				                                    third_party_xref=None,  
				                                    third_party_group=None,  
				                                    procount_export=None,
				                                    enabled=True,   
				                                    )
```
* Parameters
	* String `tagpath` - Tagpath string of the associated object
	* String `type` (optional) - Name of the equipment type. If None, will be prompted to select type from a list
	* identifier[string, int] `pad_identifier` (optional) - Name (string) or id (int) of the associated pad
	* identifier[string, int] `well_identifier` (optional) - Name (string) or id (int) of the associated well
	* String `scada_id` (optional) - ScadaID of the associated equipment. In future equipment, will always be equivalent to `merrick_id`
	* Int `merrick_id` (optional) - MerrickID of the associated equipment, assigned from P2
	* String `third_party_xref` (optional) - Reference number from 3rd party vendor to generate data from their datastore postings
	* String `third_party_group` (optional) - Third party vendor from whom the data is coming
	* Bool `procount_export` (optional) - Set true to generate data posting to procount
	* Bool `enabled` (optional, default True) - Set true to enable data in Ignition
* Returns
	* Equipment - The instance of the equipment in Metadata
##### Code Example
###### Build Equipment without data

```python
'''
This script will start a new Equipment Generation process with a series of pop-ups to generate a new equipment instance. In the case of a well equipment object, this script will attempt to map the equipment to the well object if it exists, or prompt you to map or build a new well object
'''
from Meta.Equipment import Equipment
Equipment.add_equipment_from_tagpath(
	'[North01]North/North01/Test Facility/Test Facility/Wells/Test Well 1H',
)

```
###### Build Equipment with data
```python
'''
Same as above. In this case, much of the data will be pre-populated, reducing the amount of pop-up configuration.
'''
from Meta.Equipment import Equipment
Equipment.add_equipment_from_tagpath(
	'[North01]North/North01/Test Facility/Test Facility/Wells/Test Well 1H',
	type='Well',  
	pad_identifier='Test Facility', 
	scada_id='13375',  
	merrick_id=13375,  
	third_party_xref="",  
	third_party_group="",  
	procount_export=False,
	enabled=True, 
)

```
