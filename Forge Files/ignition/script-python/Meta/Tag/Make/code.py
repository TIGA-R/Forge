from Meta.Tag import config
from Meta.Equipment import Equipment
from Meta.Site import Facility
from Meta.Well import Well

class EquipmentBuilder(object):
	def __init__(
		self, 
		name, 
		equipment_adaptor, 
		device_path,
		equipment_parameter=None, 
		equipment_parameter_2=None,
		equipment_parameter_3=None,
		parameters={}, 
		tag_parameters={},
		documentation=None
		):
		"""
		name                  -> type: str    -> Name listed for tag and metadata
		equipment_adaptor     -> type: object -> Tag adaptor from the Meta.Tag.config file
		device_path           -> type: str    -> Full tag path of the associated device
		equipment_parameter   -> type: int    -> Value of first equipment parameter for equipment adaptor
												 Default: None
		equipment_parameter_2 -> type: int    -> Value of second equipment parameter of equipment adaptor
												 Default: None
		equipment_parameter_3 -> type: int    -> Value of third equipment parameter of equipment adaptor
		 												 Default: None
		parameters            -> type: dict   -> Dictionary of parameters to be assigned to the equipment tag in the form parameter: value
												 ex:{'_p_LP': 1}
												 Default: None
		tag_parameters        -> type: dict   -> Dictionary of custom tag structures, with a dictionary value of the form:
												    {'parameter': str(name of parameter to update), 
												     'enabled': [](list of tags to enable), 
												     'base': formatted str(base tag to format with parameter values), 
												     'addresses': [](list of addresses to update the formatted str with)}
												 ex:{'parameter': '_t_LSH',
												     'enabled': ['Level Safety High', 'Level Safety High (Message)'],
												     'base': 'PMscAct_%d.BLOCK%d_FINAL_RESULT:INT8',
												     'addresses': [64, 1],}
												 Default: {}
		documentation         -> type: str    -> Documentation reference for the equipment
												 Default: None
		"""
		self.name = name
		self.equipment_adaptor = equipment_adaptor
		self.device_path = device_path
		self.equipment_parameter = equipment_parameter
		self.equipment_parameter_2 = equipment_parameter_2
		self.equipment_parameter_3 = equipment_parameter_3
		self.documentation = documentation
		self.parameters = parameters
		self.device_name = self.device_path.split('/')[-1]
		self.facility_folder = '/'.join(self.device_path.split('/')[:-2])+'/'
		self.facility = self.device_path.split('/')[-4]
		
		self.device_config = system.tag.getConfiguration(self.device_path)[0]
		self.device_type_id = self.device_config['typeId']
		assert self.device_type_id.split('/')[0] == 'REMOTE DEVICE', 'Incorrect device path. Could not find "REMOTE DEVICE" base.'
		self.device_type = config.DEVICE_DICT[self.device_type_id.split('/')[1]]
		
		self.area = 'South' if 'South' in self.device_path.split('/')[0] else 'North'
		self.udt_prefix_dict = {'South': '[South01]_types_/', 'North': '[North01]_types_/'}
		self.base_template = self.udt_prefix_dict[self.area] + getattr(self.equipment_adaptor, self.device_type + '_template')
		self.sites_folder = '/'.join(self.base_template.split('/')[:-2])+'/'
		
		# function-provided tag_parameters will take precedence over default tag_parameters from config adaptor object. If neither exists, tag_parameters is an empty dictionary
		self.tag_parameters = tag_parameters if tag_parameters else equipment_adaptor.tag_parameters if hasattr(equipment_adaptor, 'tag_parameters') else {}
		if self.tag_parameters:
			self.parameters.update({tagName: tagDict['base']%tuple(tagDict['addresses']) for tagName, tagDict in self.tag_parameters.items()})
		self.connection = system.db.runNamedQuery('Meta/Equipment/Get/Comms/Connection', {'deviceName': self.device_name})
		
		self.template_path = self.udt_prefix_dict[self.area] + self.base_template
		
		self.template_name = ' '.join([self.facility, self.equipment_adaptor.suffix, str(self.device_order)])
		
		self.instance_tag_path = self.facility_folder + self.equipment_adaptor.folder + '/' + self.name
	
	@property
	def device_id(self):
		return system.db.runNamedQuery('Meta/Equipment/Get/Comms/rd id by tagpath name', {'tagPathName': '/'.join(self.device_path.split('/')[1:])})
	
	@property
	def device_order(self):
		return system.db.runNamedQuery('Meta/Equipment/Get/Comms/Device Order', {'deviceId': self.device_id})
		
	def create_template_folder(self):
		return system.tag.configure(basePath=self.sites_folder, tags={'tagType': 'Folder', 'name': self.facility, 'tags':[{}]}, collisionPolicy="a")
		
	def create_template(self):
		template = {
			'tagType': 'UdtType',
			'typeID': self.base_template,
			'name': self.template_name,
			'parameters': {
				'Channel01': self.connection,
				'Device01': self.device_name,
				'Server': config.SERVER,
			}
		}
		return system.tag.configure(self.sites_folder + '/' + self.facility, tags=template, collisionPolicy="a")
	
	def create_instance_folder(self):
		return system.tag.configure(basePath = self.facility_folder, tags={'tagType': 'Folder', 'name': self.equipment_adaptor.folder, 'tags': [{}] }, collisionPolicy="a")
	
	def enable_tag_blocks(self):
		if not self.tag_parameters:
			return
		enable_tags = []
		for tag_dict in self.tag_parameters.values():
			enable_tags.extend([self.instance_tag_path + '/' + tag + '.enabled' for tag in tag_dict['enable']])
		system.tag.writeBlocking(enable_tags, [1 for _ in range(len(enable_tags))])
			
	def create_instance(self):
		if self.equipment_parameter is not None:
			self.parameters[self.equipment_adaptor.equipment_parameter] = self.equipment_parameter
		if self.equipment_parameter_2 is not None:
			self.parameters[self.equipment_adaptor.equipment_parameter_2] = self.equipment_parameter_2
		if self.equipment_parameter_3 is not None:
					self.parameters[self.equipment_adaptor.equipment_parameter_3] = self.equipment_parameter_3
#		if self.tag_parameters:
#			self.parameters.update(createTagParameters(self.tag_parameters))
		instance = {
			'tagType': 'UdtInstance',
			'typeID': self.sites_folder.replace(self.udt_prefix_dict[self.area], '') + self.facility + '/' + self.template_name,
			'name': self.name,
			'parameters': self.parameters,
			'documentation': self.documentation if self.documentation else '',
		}
		return system.tag.configure(self.facility_folder + '/' + self.equipment_adaptor.folder, tags=instance, collisionPolicy="a")
	
	def create_metadata(
		self, 
		well_identifier=None, 
		equip_type=None, 
		subtype=None, 
		enabled=True, 
		scada_id='', 
		merrick_id=0, 
		third_party_xref='', 
		third_party_group='', 
		procount_export=0,
		primary_hauler=None,
		fluid_transport=None,
	):
		return Equipment.add_equipment_from_tagpath(
			self.instance_tag_path, 
			well_identifier=well_identifier,
			equip_type=equip_type,
			subtype=subtype,
			enabled=enabled, 
			scada_id=scada_id, 
			merrick_id=merrick_id, 
			third_party_xref=third_party_xref, 
			third_party_group=third_party_group, 
			procount_export=procount_export,
			primary_hauler=primary_hauler,
			fluid_transport=fluid_transport,
		)
	
	def build(
		self, 
		well_identifier=None, 
		equip_type=None, 
		subtype=None, 
		enabled=True, 
		scada_id='', 
		merrick_id=0, 
		third_party_xref='', 
		third_party_group='', 
		procount_export=0, 
		primary_hauler=None, 
		fluid_transport=None, 
	):
		"""
		Optional MetaData can be included here:
			well_identifier (str|int)
			equip_type (str)
			subtype (str)
			enabled (bool)
			scada_id (str)
			merrick_id (int)
			third_party_xref (str)
			third_party_group (str)
			procount_export (bool)
			primary_hauler (str)
			fluid_transport(int, id from tbl_meta_properties)
		"""
		self.create_template_folder()
		self.create_template()
		self.create_instance_folder()
		self.create_instance()
		self.enable_tag_blocks()
		Equipment.add_equipment_from_tagpath(self.device_path)
		scada_id = str(merrick_id) if merrick_id and not scada_id else scada_id
		self.create_metadata(
			well_identifier=well_identifier, 
			equip_type=equip_type, 
			subtype=subtype, 
			enabled=enabled, 
			scada_id=scada_id, 
			merrick_id=merrick_id, 
			third_party_xref=third_party_xref, 
			third_party_group=third_party_group, 
			procount_export=procount_export,
			primary_hauler=primary_hauler,
			fluid_transport=fluid_transport,
		)
		return self.facility_folder + '/' + self.equipment_adaptor.folder + '/' + self.name

def createTagParameters(tagParametersDict):
	"""
	tagParametersDict -> type: dict -> Dictionary of custom tag structures, with a dictionary value of the form:
	    {'enabled': [](list of tags to enable), 
	     'base': formatted str(base tag to format with parameter values), 
	     'addresses': [](list of addresses to update the formatted str with)}
	 ex:{'enabled': ['Level Safety High', 'Level Safety High (Message)'],
	     'base': 'PMscAct_%d.BLOCK%d_FINAL_RESULT:INT8',
	     'addresses': [64, 1],}
	RETURNS dict -> parameter: parameterValue
	"""
	return {tagName: tagDict['base']%tuple(tagDict['addresses']) for tagName, tagDict in tagParametersDict.items()}
						
def build_device(device_name, facility_name, device_type, device_area='North', documentation=None):
	"""
	device_name   -> Type: str -> name of the device as listed in Autosol
	facility_name -> Type: str -> name of the facility. Name will be applied to the folders and metadata
	device_type   -> Type: str -> device type as listed in config.TAG_DICT
	device_area   -> Type: str -> 'North'/'North' or 'South'/'south'
	documentation -> Type: str -> (optional) documentation for the remote device tag
	RETURNS remote device tagpath
	"""
	udt_template = config.TAG_DICT[device_type]
	instance_prefix_dict = {
	        'North': '[North01]North/North01/',
	        'north': '[North01]North/North01/',
	        'South': '[South01]South/South01/',
	        'south': '[South01]South/South01/',
	        'Limerock': '[North01]North/North01/',
	        'limerock': '[North01]North/North01/',
	}
	base_path = instance_prefix_dict[device_area]
	instance = {
		'tagType': 'UdtInstance',
		'typeID': udt_template,
		'name': device_name,
		'parameters': {'Device01': device_name, 'Server': config.SERVER},
		'documentation': documentation if documentation is not None else '',
	}
	device_folder = base_path + (facility_name + '/') * 2 + 'Remote Device'
	system.tag.configure(device_folder, tags=instance, collisionPolicy="a")
	return device_folder + '/' + device_name

class SiteBuilder:

	def __init__(self, 
		device, 
		site_dict, 
		facility_name=None, 
		injection_dict=config.DEFAULT_DPMETER_NUMS, 
		well_config_build=config.well_build,
		site_configs={'METER': config.METER_CONFIG, 'TANK': config.TANK_CONFIG, 'POC': config.POC_CONFIG},
		facility_adaptor=config.FACILITY,
		well_adaptor=config.WELL,
		area=None,
		build_default_pad=None,
		enabled=True
		):
		"""
		device          -> Type: str -> full tagpath of device to build from, directly copied from the tag provider
		site_dict       -> Type: dict -> Dictionary containing the mapping of new equipment to be built, with the following layout:
			'well_n'    -> 'name' 					   -> Type: str                -> name of the well. If blank, defaults to `Well n`
					    -> 'equip'					   -> Type: List               -> List of equipment associated with the well. Currently can include: 'LP', 'HP', 'Injection', 'Oil Turbine', 'Water Turbine', 'Oil Coriolis', 'Water Coriolis', 'LP Separator', 'HP Separator'
					    -> (opt)'mid' 				   -> Type: List               -> List of merrickids matching the equipment list, with the first value representing the well itself.
			'site'      -> [equiptype] (e.g. 'meter')  -> Type: List               -> List of site [equiptype]
						-> (opt)'name'				   -> Type: Str                -> Prefix name for site equipment. Defaults to pad foldername if name is not given
					    -> (opt)'documentation'	       -> Type: Str                -> Documentation appended to each site template tag 
		(opt)'facility' -> Type: Bool                  -> If true, adds a facility object to the site
		(opt)'mid'	    -> [equiptype] (e.g. 'meter')  -> Type: List               -> List of merrickids of associated [equiptype] (matching length)
        facility_name   -> Type: str                   -> Name of the prefix for site tags and the site if it is not created yet.
        injection_dict  -> Type: dict                  -> Dictionary of injection meters and numbers
        site_configs    -> Type: dict                  -> 'EQUIPTYPE' (e.g. METER) -> Type: dictionary -> 'name'->List[equipment_adaptor, meta_data dict, (opt)equipment_parameter, (opt)equipment_parameter_2, (opt)equipment_parameter_3]
        well_adaptor   -> Type: equipment adaptor     -> Well object to use for site build
        site_adaptor   -> Type: equipment adaptor     -> Site object to use for site build
		"""
		self.build_default_pad = build_default_pad
		self.enabled = enabled
		self.device = device
		self.site_dict = site_dict
		self.facility = facility_name if facility_name is not None else self.device.split('/')[-4]
		if 'site' not in self.site_dict.keys():
			self.site_dict['site'] = {}
		self.pad = self.site_dict['site']['name'] if 'name' in self.site_dict['site'].keys() else self.device.split('/')[-3]		
		self.area = area if area is not None else self.device.split('/')[-6]	
			
		self.suffix_dict = {
			'LP': 'LP Meter',
			'HP': 'HP Meter',
			'Wellhead': 'Wellhead Meter',
			'Injection': 'Injection Meter',
			'Oil Coriolis': 'Oil Coriolis',
			'Water Coriolis': 'Water Coriolis',
			'Oil Turbine': 'Oil Turbine',
			'Water Turbine': 'Water Turbine',
			'LP Separator': 'LP Separator',
			'HP Separator': 'HP Separator',
			'Injection Valve': 'Injection Valve',
			'Choke Valve': 'Choke Valve',
		}
		
		self.builder_dict = {}
		# Built before the builder dict so that wells are generated prior to other equipment
		self.well_dict = {}
		# A dict for referencing well numbers during equipment creation to bypass manually associating a well id
		self.well_num_name_dict = {}
		for key, val in self.site_dict.items():
			if key == 'facility' and self.site_dict['facility']:
				self.builder_dict[self.facility + ' Facility'] = [facility_adaptor, {'type': 'Facility', 'subtype': 'Facility', 'merrickid': 0}]
			if 'well' in key:
				well_num = int(key.split('_')[-1])
				config_dict = well_config_build(well_num, site_dict, injection_dict)
				# skip well configuration
				if 'well' in self.site_dict[key].keys() and not self.site_dict[key]['well']:
					Well.add_well(
					Facility(device.split('/')[-4]).sql_id, 
					self.site_dict[key]['name'], 
					merrick_id=self.site_dict[key]['mid'][0] if 'mid' in self.site_dict[key].keys() else 0, 
					scada_id=str(self.site_dict[key]['mid'][0]) if 'mid' in self.site_dict[key].keys() else '', 
					)
				# Add well configuration
				else:
					self.well_dict[val['name']] = [well_adaptor, {'type': 'Well', 'subtype': 'Well', 'merrickid': self.site_dict[key]['mid'][0] if 'mid' in self.site_dict[key].keys() else 0}, well_num]
				for idx, equip in enumerate(val['equip']):
					equip_name = ' '.join((val['name'], self.suffix_dict[equip])) if equip in self.suffix_dict.keys() else ' '.join((val['name'], equip))
					self.builder_dict[equip_name] = config_dict[equip]
					if 'mid' in self.site_dict[key].keys():
						self.builder_dict[equip_name][1]['merrickid'] = self.site_dict[key]['mid'][idx+1]
					self.well_num_name_dict[equip_name] = 'well_' + str(well_num)
			if key == 'site':
				for equip_type, val in self.site_dict[key].items():
					if equip_type in ('documentation', 'name'):
						continue
					equip_dict = site_configs[equip_type.upper()]
					for idx, equip in enumerate(val):
						equip_name = ' '.join((self.pad, equip))
						self.builder_dict[equip_name] = equip_dict[equip]
						if 'mid' in self.site_dict.keys():
							try:
								self.builder_dict[equip_name][1]['merrickid'] = self.site_dict['mid'][equip_type][idx]
							except KeyError:
								pass
		
	def build(self, primary_hauler=None, fluid_transport=None):
		facility = Facility.new(self.facility, area=self.area, build_default_pad=self.build_default_pad, enabled=self.enabled)
		Equipment.add_equipment_from_tagpath(self.device, equip_type='Comms', well_identifier=0)
		doc_dict = {}
		if 'documentation' in self.site_dict['site'].keys():
			doc_dict['documentation'] = self.site_dict['site']['documentation']
		for well_name, well_data in self.well_dict.items():
			EquipmentBuilder(
				well_name, 
				well_data[0], 
				self.device, 
				*well_data[2:], 
				**doc_dict
			).build(
				equip_type=well_data[1]['type'], 
				subtype=well_data[1]['subtype'], 
				merrick_id=well_data[1]['merrickid'],
			)
		for equip_name, equip_data in self.builder_dict.items():
			doc_dict = {'parameters': {}}
			if 'documentation' in self.site_dict['site'].keys():
				doc_dict['documentation'] = self.site_dict['site']['documentation']
			if isinstance(equip_data[-1], dict):
				if 'type' not in equip_data[-1].keys():
					doc_dict['parameters'] = equip_data[-1]
					equip_data = equip_data[:-1]
			if equip_name in self.well_num_name_dict.keys():
				well_identifier = self.site_dict[self.well_num_name_dict[equip_name]]['name']
			else:
				well_identifier = 0
#			print('equip name: ' + equip_name)
#			print('equip data: ' + str(equip_data))
#			print(doc_dict)
			if 'tank' in equip_data[1]['type']:
				EquipmentBuilder(
					equip_name, 
					equip_data[0], 
					self.device, 
					*equip_data[2:], 
					**doc_dict
				).build(
					well_identifier=well_identifier, 
					equip_type=equip_data[1]['type'], 
					primary_hauler=primary_hauler, 
					fluid_transport=fluid_transport, 
					subtype=equip_data[1]['subtype'], 
					merrick_id=equip_data[1]['merrickid'] if 'merrickid' in equip_data[1] else 0
				)
			
			else:
				EquipmentBuilder(
					equip_name, 
					equip_data[0], 
					self.device, 
					*equip_data[2:], 
					**doc_dict
				).build(
					well_identifier=well_identifier, 
					equip_type=equip_data[1]['type'], 
					subtype=equip_data[1]['subtype'], 
					merrick_id=equip_data[1]['merrickid'] if 'merrickid' in equip_data[1] else 0,
				)
