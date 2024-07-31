from Meta.Meta import Meta
from Meta.Site import Facility
from Meta.PYDS import PYDS
from system.db import runNamedQuery

class Well(Meta):
    table_name = 'meta_well'
    meta_type = 'well'
    
    def __init__(self, identifier):
        self.identifier = identifier
        if self.identifier == 'None':
        	self.identifier = None
        self.get_name_and_id(self.identifier)
    
    @property
    def scada_id(self):
        return self.get_sql_field('scadaID')

    @scada_id.setter
    def scada_id(self,value):
        self.update_sql_field('scadaID', str(value))

    @property
    def merrick_id(self):
        return self.get_sql_field('merrickID')

    @merrick_id.setter
    def merrick_id(self, value):
        self.update_sql_field('merrickID', str(value))  
    
    @property
    def site_id(self):
    	return self.get_sql_field('siteID')
    
    @classmethod
    def well_list(cls, facility_id):
        dataset = runNamedQuery('Meta/Well/Get/By Facility', {'siteID': facility_id})
        return PYDS(dataset=dataset).ds2py()['name']
    
    @classmethod
    def add_well(cls, facility_identifier, name, enabled=True, merrick_id=None, scada_id=None):
		# Check if pad name exists
		if cls(name).sql_id is not None:
		    print('Facility name already exists')
		    return cls(name)
		fac_id_dict = {
			str: lambda x: Facility(x).sql_id,
			int: lambda x: x,
			None: None
		}
		facility_id = fac_id_dict[type(facility_identifier)](facility_identifier)
		print(facility_id)
		from system.gui import inputBox
		existing_well = cls(name)
		if existing_well.sql_id is not None and existing_well.site_id == facility_id:
			rename_or_use = int(inputBox('Well name %s already exists in meta_well. Would you like to: \n(1) - Try a new name\n(2) - Use this well?'%existing_well.name))
			if rename_or_use == 1:
				cls.add_well(facility_id, inputBox('Enter a new well name'))
			elif rename_or_use == 2:
				return cls(name)
			else:
				raise('invalid option')
		query_dict = {
		        'facilityID': facility_id,
		        'wellName': name,
		        'enabled': enabled,
		        'merrickID': merrick_id if merrick_id is not None else 0,
		        'scadaID': scada_id if scada_id is not None else '0'
		        }
		runNamedQuery('Meta/Well/Add/Meta Well', query_dict)
		print('%s added to Meta Well successfully'%name)
		return cls(name)
    	  
