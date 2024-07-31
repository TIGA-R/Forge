from system.db import runNamedQuery
from Meta.Meta import Meta
from Meta.config import FOREMAN_SCRIPT, ROUTE_SCRIPT
from Meta.PYDS import PYDS


class Facility(Meta):
    table_name = 'meta_site'
    meta_type = 'facility'
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.get_name_and_id(self.identifier)
    
    @property
    def procount_midnight(self):
        pcm_enabled = system.db.runNamedQuery('Meta/Meta/Get/ProCount/Midnight/Enabled', {'siteid': self.sql_id})
        pcm_dict = PYDS(pcm_enabled).ds2py()
        if len(pcm_dict['result']) == 1:
            if pcm_dict['result'][0] == True:
                return True
        return False
    
    @procount_midnight.setter
    def procount_midnight(self, value):
        system.db.runNamedQuery('Meta/Meta/Update/ProCount/Midnight/Enable', {'siteid': self.sql_id, 'enabled': value})
    
    @property
    def route(self):
        return self.get_sql_field('route')
    
    @route.setter
    def route(self, value):
        self.update_sql_field('route', value)
        for pad_id in self.pads_set:
            Pad(pad_id).route = value
            
    @property
    def enabled(self):
        return self.get_sql_field('enabled')
    
    @enabled.setter
    def enabled(self, value):
        self.update_sql_field('enabled', value)
        
    @property
    def foreman(self):
        return self.get_sql_field('foreman')
    
    @foreman.setter
    def foreman(self, value):
        self.update_sql_field('foreman', value)
        for pad_id in self.pads_set:
            Pad(pad_id).foreman = value
    
    @property
    def latitude(self):
    	return self.get_sql_field('latitude')
	
	@latitude.setter
	def latitude(self, value):
		self.update_sql_field('latitude', value)
    
    @property
    def merrickid(self):
    	return self.get_sql_field('merrickid')
	
	@merrickid.setter
	def merrickid(self, value):
		self.update_sql_field('merrickid', value)	
		
    @property
    def longitude(self):
    	return self.get_sql_field('longitude')
	
	@latitude.setter
	def latitude(self, value):
		self.update_sql_field('longitude', value)
    
    @property
    def pads_sql_list(self):
        from system.dataset import toPyDataSet
        pads = runNamedQuery('Meta/Site/Get/Pads in Facility', {'facilityID': self.sql_id})

    	pad_set = set()
        for pad in toPyDataSet(pads):
            pad_set.add(str(pad[0]))
        return "(" + ", ".join(pad_set) + ")"
    
    @property
    def pads_set(self):
        from system.dataset import toPyDataSet
        pads = runNamedQuery('Meta/Site/Get/Pads in Facility', {'facilityID': self.sql_id})
        pad_set = set()
        for pad in toPyDataSet(pads):
            pad_set.add(pad[0])
        return pad_set
    
    @classmethod
    def new(cls, name=None, area=None, foreman=None, route=None, enabled=None, build_default_pad=None):
		from system.gui import inputBox
		if name is None:
		    name = inputBox('Enter a Facility name')
		
		# Check if pad name exists
		if cls(name).sql_id is not None:
		    print('Facility name already exists')
		    return cls(name)
		
		# Area
		area_dict = {
			1: 'North',
			'North': 'North',
			'north': 'North',
			2: 'South',
			'South': 'South',
			'south': 'South',
			3: 'Lime Rock',
			'Limerock': 'Lime Rock',
			'limerock': 'Lime Rock',
			'Lime Rock': 'Lime Rock',
			}
		print(type(area))
		if area not in area_dict.keys():
		    area = inputBox('(1) - North\n(2) - South\n(3) - Limerock')
		if area in ['1', '2', '3']:
			area = int(area)
		area = area_dict[area]
		
		# Foreman
		if foreman not in FOREMAN_SCRIPT[area]:
		    if len(FOREMAN_SCRIPT[area])>1:
		        prompt_str = 'Select a foreman: '
		        num = 1
		        for foreman in FOREMAN_SCRIPT[area]:
		            prompt_str += '\n(%s) - %s'%(num, foreman)
		            num += 1
		        foreman = FOREMAN_SCRIPT[area][int(inputBox(prompt_str))-1]
		    else:
		        foreman = FOREMAN_SCRIPT[area][0]
		
		# Route
		if route not in ROUTE_SCRIPT[area]:
		    prompt_str = 'Select a route: '
		    num = 1
		    for route in ROUTE_SCRIPT[area]:
		        prompt_str += '\n(%s) - %s'%(num, route)
		        num += 1
		    route = ROUTE_SCRIPT[area][int(inputBox(prompt_str))-1] if len(ROUTE_SCRIPT[area]) > 1 else ROUTE_SCRIPT[area][0]
		
		# Enabled
		if enabled is None:
		    enabled = int(inputBox('(1) - Enabled\n(0) - Disabled'))
		        
		parameters = {
		    'name': name,
		    'facilityID': None,
		    'enabled': enabled,
		    'type': 'Facility',
		    'area': area,
		    'foreman': foreman,
		    'route': route,
		}
		
		runNamedQuery('Meta/Site/Add/Site', parameters)
		print('Facility added successfully')

		if build_default_pad:
			Pad.new(
		            cls(name).sql_id, 
		            name=name,
		            area=area,
		            foreman=foreman,
		            route=route,
		            enabled=enabled,
		            build_default_pad=True,
		        )

		else:		
			add_pad = inputBox('%s\nWould you like to add a Pad to this facility?\n(0) - No\n(1) - Yes'%(name)) if build_default_pad is None else build_default_pad
			
			if add_pad:
				same_name = inputBox('%s\nWould you like to use the Facility name?\n(0) - No\n(1) - Yes'%(name)) 
			else:
				same_name = False
			if same_name:
			    Pad.new(
			        cls(name).sql_id, 
			        name=name,
			        area=area,
			        foreman=foreman,
			        route=route,
			        enabled=enabled,
			    )
			else:
			    Pad.new(
			        cls(name).sql_id, 
			        area=area,
			        foreman=foreman,
			        route=route,
			        enabled=enabled,
			    )
		return cls(name)

class Pad(Meta):
    table_name = 'meta_site'
    meta_type = 'pad'

    def __init__(self, identifier):
        self.identifier = identifier
        self.get_name_and_id(self.identifier)
    
    @property
    def route(self):
        return self.get_sql_field('route')

    @route.setter
    def route(self, value):
        self.update_sql_field('route', value)
        Metadata.RouteUpdate.updateSiteRoutes(self.sql_id)

    @property
    def foreman(self):
        return self.get_sql_field('foreman')

    @foreman.setter
    def foreman(self, value):
        self.update_sql_field('foreman', value)
    
    @property
    def facility_id(self):
        return self.get_sql_field('facilityID')

    @classmethod
    def new(cls, facility_identifier, name=None, area=None, foreman=None, route=None, enabled=None, build_default_pad=False):
		from system.gui import inputBox
		if name is None:
		    name = inputBox('Enter a Pad name')
		
		# Check if pad name exists
		if cls(name).sql_id is not None:
		    raise('Pad name already exists')
		
		# Area
		area_dict = {
			1: 'North',
			'North': 'North',
			'north': 'North',
			2: 'South',
			'South': 'South',
			'south': 'South',
			3: 'Lime Rock',
			'Limerock': 'Lime Rock',
			'limerock': 'Lime Rock',
			'Lime Rock': 'Lime Rock',
			}
		if area not in area_dict.keys():
		    area = inputBox('(1) - North\n(2) - South\n(3) - Limerock')
		if area in ['1', '2', '3']:
			area = int(area)
		area = area_dict[area]
		
		# Foreman
		if foreman not in FOREMAN_SCRIPT[area]:
		    if len(FOREMAN_SCRIPT[area])>1:
		        prompt_str = 'Select a foreman: '
		        num = 1
		        for foreman in FOREMAN_SCRIPT[area]:
		            prompt_str += '\n(%s) - %s'%(num, foreman)
		            num += 1
		        foreman = FOREMAN_SCRIPT[area][int(inputBox(prompt_str))-1]
		    else:
		        foreman = FOREMAN_SCRIPT[area][0]
		
		# Route
		if route not in ROUTE_SCRIPT[area]:
		    prompt_str = 'Select a route: '
		    num = 1
		    for route in ROUTE_SCRIPT[area]:
		        prompt_str += '\n(%s) - %s'%(num, route)
		        num += 1
		    route = ROUTE_SCRIPT
		    [area][int(inputBox(prompt_str))-1]
		
		# Enabled
		if enabled is None:
		    enabled = int(inputBox('(1) - Enabled\n(0) - Disabled'))
		
		facility_id = Facility(facility_identifier).sql_id
		if facility_id is None:
		    raise('Facility could not be found')
		
		parameters = {
		    'name': name,
		    'facilityID': facility_id,
		    'enabled': enabled,
		    'type': 'Pad',
		    'area': area,
		    'foreman': foreman,
		    'route': route,
		}
		
		runNamedQuery('Meta/Site/Add/Site', parameters)
		print('%s Pad added successfully'%(name))
		if build_default_pad:
			return cls(name)
		add_pad = int(inputBox('%s\nWould you like to add another Pad to this facility?\n(0) - No\n(1) - Yes'%(name)))
		if add_pad:
		    Pad.new(
		        cls(name).sql_id, 
		        area=area,
		        foreman=foreman,
		        route=route,
		    )
		return cls(name)