# New Facility Buildout
## Realtime Tag Provider Layout
Currently, a new `Facility` is generated as a folder inside the `tag provider` associated with the `Facility Area`, i.e. `North01`, `South01`.
### Namespacing
For folder structuring, the tag provider is laid out in the heirarchy:
1) `Area` 
	* `North`/`South`
2)  `Area Section` 
	* For future expansion potential. 
	* Currently only `North01`/`South01`
3) `Facility`  
	* Future facilities expected to match 1-1 the Metadata naming
	* Legacy cases exist
4)  `Pad` **Building the tag provider to this point is recommended for new Facility Buildout**
	* Future Pads expected to be a 1-1 with Facilities
	* Legacy structure have instances of {many->one} {`Facility`->`Pad`} cases
	* **TO DO**: Heirarchy to this point to be built by MetaData Scripting
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
		* `Wells`
			* `Well`
			* `Frac Water Well`
6) `Equipment`
	* The functional tags which 
### Tag Provider Diagram
![image](https://github.com/user-attachments/assets/a546c9f4-fb2b-4043-93dc-1264d9eb6e2c)

## Metadata Structure
### Database Structure
Facility information for Ignition is stored in the `Metadata01` database, on the `Meta_Site` table. `Meta_Site` stores data for both `Facility` and `Pad` objects. `Pad` data is connected to `Facility` by PK/FK relationship:

![image](https://github.com/user-attachments/assets/11b553a9-7a2d-4cb6-bc8b-2a55cdbb5ce5)

As mentioned above, it is anticipated moving forward that all `Facilities` will have a single `Pad` instance, representing a one-to-one relationship.
### Generating new Facility Instances
New `Facility` and `Pad` instances are built in Metadata by script:
#### Meta.Site.Facility.new
##### Description
Generates a script to populate a new facility instance, and, optionally, a child pad instance as well
##### Syntax
```python
Meta.Site.Facility.new(name=None, area=None, foreman=None, route=None, enabled=None)
```
* Parameters
	* String `name` - The name of the `Facility`. If `None`, a prompt will be raised to generate one
	* String[`North`, `South`] `area` - The name of the `area` the `Facility` falls under. If `None`, a prompt will be raised to select one
	* String `foreman` - The name of the `Foreman` overseeing the new site. If `None`, a prompt will be raised to select one
	* String `route` - The name of the route this Facility is connected to. If `None`, a prompt will be raised to select one
	* Boolean `enabled` - Bit to determine if the facility is enabled or not
* Returns:
	* Facility - The instance of the Facility object
##### Code Example
###### Build Facility without data
```python
'''
This script will start a new Facility Generation process with a series of pop-ups to generate a new facility instance. After completing, you will be prompted whether you want to build a Pad as well, and the Pad will be generated automatically if chosen
'''
from Meta.Site import Facility
Facility.new()

```
###### Build Facility with data
```python
'''
This script will produce a new facility instantly, and then prompt the user whether to build an associated Pad
'''
from Meta.Site import Facility

Facility.new('Test Facility', 'North', 'Bob Jones', '90X', True)

```
