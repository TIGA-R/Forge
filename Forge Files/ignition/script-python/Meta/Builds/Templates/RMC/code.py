class Template:
	def __init__(self):
		siteName = '' # Update Name  
		### IMPORTANT -> MAKE SURE TO BUILD THE DEVICE IN AUTO'HAN'SOLO AND ENABLE THE DEVICE BEFORE RUNNING FINAL `run` FUNCTION ###
		deviceName = '' # Update Device Name from Autosol
		area = 'South' # List area (North/South)
		documentation = '' # Update Documentation/ticket reference  
		numWells = 0 # Update number of wells
		self.wellTemplate = Meta.Tag.config.TF_RMC_WELL # Update well template
		self.facilityTemplate = Meta.Tag.config.TF_RMC_FACILITY # Update facility template
		self.buildFacility = True # Update to true if facility equipment build out is required
		self.primary_hauler = None # Update with hauler name is tanks are included in the build
		self.fluid_transport = 3 # Update with fluid transport number (1: Piped, 2: Hauled, 3: None) 
		
		#Update with well names. 
		wellDict = {
			1: '',
			2: '',
			3: '',
			4: '',
			5: '',
			6: '',
			7: '',
			8: '',
			9: '',
			10: '',
		}
		
		# Update Number of tanks
		tankDict = {
			'oil tanks': 1,
			'water tanks': 1,
#			'gun barrel tanks': 0,
		}
		
		tankMerrickDict = {
						  #1	 #2     #3     #4 #5	
		#	'oil tanks': [12345, 12346, 12347, 0, 12348], EXAMPLE - DO NOT UNCOMMENT
			'oil tanks': [],
			'water tanks': [],
#			'gun barrel tanks': [],
		}
		
		# Update Number of compressors
		compDict = {
			'gas': 0,
			'vru': 0,
		}
		
		#Update Injection Meter Nums as Necessary
		DPMETER_NUMS = {
		
		}
		
		### WELL-LEVEL EQUIPMENT CONFIGURATION ### 
		# Comment out any equipment that does not apply
		wellEquipDict = {
			1: [  ### Well 1 Equipment ###
			'LP',
#			'HP',
#			'Injection',
			'Oil Meter',
			'Water Meter',
			'LP Separator',
#			'HP Separator',
#			'Injection Valve',
#			'Choke Valve',
#			'Plunger',
			'FOA',
			],
			2: [  ### Well 2 Equipment ###
			'LP',
#			'HP',
#			'Injection',
			'Oil Meter',
			'Water Meter',
			'LP Separator',
#			'HP Separator',
#			'Injection Valve',
#			'Choke Valve',
#			'Plunger',
			'FOA',
			],
			3: [  ### Well 3 Equipment ###
			'LP',
#			'HP',
#			'Injection',
			'Oil Meter',
			'Water Meter',
			'LP Separator',
#			'HP Separator',
#			'Injection Valve',
#			'Choke Valve',
#			'Plunger',
			'FOA',
			],			
		
		}
		
		wellMerrickDict = {
			1: [  ### Well 1 Merrick IDs ###
			0,  # Well
			0,  # LP
#			0,  # HP
#			0,  # Injection
			0,  # Oil Coriolis
			0,  # Water Coriolis
			0,  # LP Separator
#			0,  # HP Separator
#			0,  # Injection Valve
#			0,  # Choke Valve
#			0,  # Plunger
			0,  # FOA
			],
			2: [  ### Well 2 Merrick IDs ###
			0,  # Well
			0,  # LP
#			0,  # HP
#			0,  # Injection
			0,  # Oil Coriolis
			0,  # Water Coriolis
			0,  # LP Separator
#			0,  # HP Separator
#			0,  # Injection Valve
#			0,  # Choke Valve
#			0,  # Plunger
			0,  # FOA
			],
			3: [  ### Well 3 Merrick IDs ###
			0,  # Well
			0,  # LP
#			0,  # HP
#			0,  # Injection
			0,  # Oil Coriolis
			0,  # Water Coriolis
			0,  # LP Separator
#			0,  # HP Separator
#			0,  # Injection Valve
#			0,  # Choke Valve
#			0,  # Plunger
			0,  # FOA
			],
			}
		# comment out equipment that do not apply
		METER_CONFIG = {
		'HP Sales Check': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Check Meter', 'merrickid': 0}, 61],
		'HP Sales': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Sales Meter', 'merrickid': 0}, 62],
		'LP Sales Check': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Check Meter', 'merrickid': 0}, 63],
		'LP Suction Scrubber': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 64],
		'HP Bulk Separator 1': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 65],
		'HP Bulk Separator 2': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 66],
		'LP Bulk Separator 1': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 67],
		'LP Bulk Separator 2': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 68],
		'Fuel Gas': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 69],
		'VRU Discharge': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 70],
		'Compressor 1 Discharge': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 71],
		'Compressor 2 Discharge': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 72],
		'Compressor 3 Discharge': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 73],
		'Compressor 4 Discharge': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 74],
		'Compressor 5 Discharge': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 75],
		'HP Flare': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 76],
		'LP Flare': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 77],
		'Cushion Scrubber': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 78],
		'Buy Back': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 79],
		'Transfer Pump 1': [Meta.Tag.config.TF_RMC_PUMP_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 1],
		'Transfer Pump 2': [Meta.Tag.config.TF_RMC_PUMP_METER, {'type': 'Gas Meter', 'subtype': 'Gas Meter', 'merrickid': 0}, 2],
		}
		
		# comment out equipment that do not apply
		VESSEL_CONFIG = {
		'Satellite Facility Outlet HP Separator': [Meta.Tag.config.TF_RMC_FACILITY_HP_SEP_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'HP Bulk Seperator 1': [Meta.Tag.config.TF_RMC_HP_BULK_SEP_1_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'HP Bulk Seperator 2': [Meta.Tag.config.TF_RMC_HP_BULK_SEP_2_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'LP Bulk Seperator 1': [Meta.Tag.config.TF_RMC_LP_BULK_SEP_1_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'LP Bulk Seperator 2': [Meta.Tag.config.TF_RMC_LP_BULK_SEP_2_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'Test Heater Vessel': [Meta.Tag.config.TF_RMC_TEST_HEATER_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'Heater 1 Vessel': [Meta.Tag.config.TF_RMC_HEATER_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}, 1],
		'Heater 2 Vessel': [Meta.Tag.config.TF_RMC_HEATER_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}, 2],
		'HP Sales Vessel': [Meta.Tag.config.TF_RMC_HP_SALES_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'LP Sales Vessel': [Meta.Tag.config.TF_RMC_LP_SALES_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'Cushion Scrubber Vessel': [Meta.Tag.config.TF_RMC_CUSHION_SCRUBBER_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'LP Suction Scrubber Vessel': [Meta.Tag.config.TF_RMC_LP_SUCTION_SCRUBBER_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'Compressor Blowcase Vessel': [Meta.Tag.config.TF_RMC_COMPRESSOR_BLOWCASE_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'VRT 1 Vessel': [Meta.Tag.config.TF_RMC_VRT_1_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'VRT 2 Vessel': [Meta.Tag.config.TF_RMC_VRT_2_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'Flare Fuel Pot Vessel': [Meta.Tag.config.TF_RMC_FLARE_FUEL_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'HP Flare Vessel': [Meta.Tag.config.TF_RMC_HP_FLARE_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'LP Flare Vessel': [Meta.Tag.config.TF_RMC_LP_FLARE_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		'Satellite Cooler Fuel Skid Vessel': [Meta.Tag.config.TF_RMC_SATELLITE_COOLER_FUEL_SKID_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
		}
		
		# comment out equipment that do not apply
		FLARE_CONFIG = {
		'Flare': [Meta.Tag.config.TF_RMC_FLARE, {'type': 'Flare', 'subtype': 'Flare', 'merrickid': 0}],
		}
		
		### Do Not Modify ###
		COMPRESSOR_CONFIG = {}
		for num in range(compDict['gas']):
			COMPRESSOR_CONFIG['Compressor ' + str(num+1)] = [Meta.Tag.config.TF_RMC_COMPRESSOR, {'type': 'Gas Compressor', 'subtype': 'Gas Compressor', 'merrickid':0}, num+1]
		for num in range(compDict['vru']):
			COMPRESSOR_CONFIG['VRU Compressor ' + str(num+1)] = [Meta.Tag.config.TF_RMC_VRU, {'type': 'Gas Compressor', 'subtype': 'VRU Compressor', 'merrickid':0}, num+1]
		
		### Do Not Modify ###
		TANK_CONFIG = {}
		for num in range(tankDict['oil tanks']):
			TANK_CONFIG['Oil Tank ' + str(num+1)] = [
				Meta.Tag.config.TF_RMC_TANK, 
				{'type': 'Tank', 'subtype': 'Oil Tank', 'merrickid':tankMerrickDict['oil tanks'][num] if len(tankMerrickDict['oil tanks']) > num else 0}, 
				num+1, 
				0, 
				{'_p_GunBarrel': 0}
				] 
		for num in range(tankDict['water tanks']):
			TANK_CONFIG['Water Tank ' + str(num+1)] = [
			Meta.Tag.config.TF_RMC_TANK, 
				{'type': 'Tank', 'subtype': 'Water Tank', 'merrickid':tankMerrickDict['water tanks'][num] if len(tankMerrickDict['water tanks']) > num else 0}, 
				num+1, 
				1, 
				{'_p_GunBarrel': 0}
				]
		try:
			for num in range(tankDict['gun barrel tanks']):
				TANK_CONFIG['Gun Barrel Tank ' + str(num+1)] = [
					Meta.Tag.config.TF_RMC_TANK, 
					{'type': 'Tank', 'subtype': 'Gun Barrel Tank', 'merrickid':tankMerrickDict['gun barrel tanks'][num] if len(tankMerrickDict['gun barrel tanks']) > num else 0}, 
					num+11, 
					0, 
					{'_p_GunBarrel': 1}
					]
		except KeyError:
			pass
			
		# comment out any equipment type that do not apply
		self.upperSiteConfigDict =  {
#			'POC': POC_CONFIG,
			'TANK': TANK_CONFIG,
			'METER': METER_CONFIG,
			'VESSEL': VESSEL_CONFIG,
			'COMPRESSOR': COMPRESSOR_CONFIG,
			'FLARE': FLARE_CONFIG
			}
		
		siteConfigDict = {key.lower(): val.keys() for key, val in self.upperSiteConfigDict.items()}
		self.device = Meta.Tag.Make.build_device(deviceName, siteName, 'wellpilot', area, documentation)
		### Do Not Modify ###  
		self.siteDict = {'well_' + str(idx): {'name':wellDict[idx], 'equip': wellEquipDict[idx], 'mid': wellMerrickDict[idx]} for idx in range(1, numWells + 1)}
		self.siteDict['site'] = siteConfigDict
		self.siteDict['facility'] = self.buildFacility
		self.siteDict['documentation'] = documentation
	
	def well_build(self, well_num, site_dict, dpmeter_dict):
		
		config_dict = {
			'LP': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, 10+well_num],
			'HP': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, 20+well_num],
			'Injection': [Meta.Tag.config.TF_RMC_GAS_METER, {'type': 'Gas Meter', 'subtype': 'Gas Lift Meter', 'merrickid': 0}, 30+well_num],
			'Injection': [Meta.Tag.config.TF_RMC_VALVE, {'type': 'Gas Meter', 'subtype': 'Gas Lift Meter', 'merrickid': 0}, well_num, 0, 0],
			'Auto Choke': [Meta.Tag.config.TF_RMC_VALVE, {'type': 'Gas Meter', 'subtype': 'Gas Lift Meter', 'merrickid': 0}, well_num, 1, 0],
			'Oil Coriolis Meter': [Meta.Tag.config.TF_RMC_OIL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Coriolis Meter', 'merrickid': 0}, 232+well_num],
			'Water Coriolis Meter': [Meta.Tag.config.TF_RMC_WATER_METER, {'type': 'Liquid Meter', 'subtype': 'Water Coriolis Meter', 'merrickid': 0}, 222+well_num],
			'Oil Turbine Meter': [Meta.Tag.config.TF_RMC_OIL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 232+well_num],
			'Water Turbine Meter': [Meta.Tag.config.TF_RMC_WATER_METER, {'type': 'Liquid Meter', 'subtype': 'Water Turbine Meter', 'merrickid': 0}, 222+well_num],
			'LP Separator': [Meta.Tag.config.TF_RMC_VESSEL, {'type': 'Vessel', 'subtype': 'Separator Vessel', 'merrickid': 0}, well_num, 1],
			'HP Separator': [Meta.Tag.config.TF_RMC_VESSEL, {'type': 'Vessel', 'subtype': 'Separator Vessel', 'merrickid': 0}, well_num, 0],
		#	'Plunger': [Meta.Tag.config.TWT_PLUNGER, {'type': 'Plunger', 'subtype': 'Plunger', 'merrickid': 0}, well_num + 180],
		#	'FOA': [Meta.Tag.config.TWT_FACILITY_FIRST_OUT, {'type': 'Facility', 'subtype': 'Facility Well Alarms', 'merrickid': 0}, well_num],
		}
		return config_dict

	def check(self):
		Meta.Tag.Make.SiteBuilder(self.device, self.siteDict, well_config_build=self.well_build, site_configs=self.upperSiteConfigDict, well_adaptor=self.wellTemplate, facility_adaptor=self.facilityTemplate)
		
	def run(self):
		Meta.Tag.Make.SiteBuilder(self.device, self.siteDict, well_config_build=self.well_build, site_configs=self.upperSiteConfigDict, well_adaptor=self.wellTemplate, facility_adaptor=self.facilityTemplate).build(primary_hauler=self.primary_hauler, fluid_transport=self.fluid_transport)