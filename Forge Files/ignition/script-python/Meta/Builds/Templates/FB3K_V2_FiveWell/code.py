########################################################################################################################
### IMPORTANT -> MAKE SURE TO BUILD THE DEVICE IN AUTOSOLO AND ENABLE THE DEVICE BEFORE RUNNING FINAL `run` FUNCTION ###
########################################################################################################################
siteName = 'Site Name' # Update Name  
### IMPORTANT -> MAKE SURE TO BUILD THE DEVICE IN AUTOSOLO AND ENABLE THE DEVICE BEFORE RUNNING FINAL `run` FUNCTION ###
deviceName = 'DEVICE_RD' # Update Device Name from Autosol
deviceType = 'fb3000'
area = 'North' # List area (North/South)
documentation = '' # Update Documentation/ticket reference  
numWells = 0 # Update number of wells
primary_hauler = None # Update with hauler name is tanks are included in the build
fluid_transport = 3 # Update with fluid transport number (1: Piped, 2: Hauled, 3: None) 

#Update with well names. 
wellDict = {
	1: '',
	2: '',
	3: '',
	4: '',
	5: '',
	6: '',
}

# Update Number of tanks
tankDict = {
	'oil tanks': 0,
	'water tanks': 0,
	'gun barrel tanks': 0,
}
tankMerrickDict = {
				  #1	 #2     #3     #4 #5	
#	'oil tanks': [12345, 12346, 12347, 0, 12348], EXAMPLE - DO NOT UNCOMMENT
	'oil tanks': [],
	'water tanks': [],
	'gun barrel tanks': [],
}

# Update Number of compressors
compDict = {
	'gas': 0,
	'vru': 0,
}

def well_build(well_num, site_dict, dpmeter_dict):
	
	config_dict = {
	'LP': [Meta.Tag.config.FWT_WELL_DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, well_num, 1],
	'HP': [Meta.Tag.config.FWT_WELL_DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, well_num, 0],
	'Injection': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Lift Meter', 'merrickid': 0}, dpmeter_dict['injection_' + str(well_num)] if 'Injection' in site_dict['well_'+str(well_num)]['equip'] else 0, {'_p_Gas Lift': 1,}],
	'Oil Coriolis': [Meta.Tag.config.FWT_OIL_CORIOLIS, {'type': 'Liquid Meter', 'subtype': 'Oil Coriolis Meter', 'merrickid': 0}, well_num],
	'Water Coriolis': [Meta.Tag.config.FWT_WATER_CORIOLIS, {'type': 'Liquid Meter', 'subtype': 'Water Coriolis Meter', 'merrickid': 0}, well_num],
	'LP Separator': [Meta.Tag.config.FWT_SEPARATOR_VESSEL, {'type': 'Vessel', 'subtype': 'Separator Vessel', 'merrickid': 0}, well_num, 1],
	'HP Separator': [Meta.Tag.config.FWT_SEPARATOR_VESSEL, {'type': 'Vessel', 'subtype': 'Separator Vessel', 'merrickid': 0}, well_num, 0],
	'Injection Valve': [Meta.Tag.config.FWT_VALVE, {'type': 'Control Valve', 'subtype': 'Gas Lift Control Valve', 'merrickid': 0}, well_num, 0],
	'Choke Valve': [Meta.Tag.config.FWT_VALVE, {'type': 'Control Valve', 'subtype': 'Choke Valve', 'merrickid': 0}, well_num, 1],
	}
	return config_dict

#Update Injection Meter Nums as Necessary
DPMETER_NUMS = {
'injection_1': 6,
'injection_2': 7,
'injection_3': 8,
'injection_4': 16,
'injection_5': 17,
}

### WELL-LEVEL EQUIPMENT CONFIGURATION ### 
# Comment out any equipment that does not apply
wellEquipDict = {
	1: [  ### Well 1 Equipment ###
	'LP',
	'HP',
	'Injection',
	'Oil Coriolis',
	'Water Coriolis',
	'LP Separator',
	'HP Separator',
	'Injection Valve',
	'Choke Valve',
	],
	2: [  ### Well 2 Equipment ###
	'LP',
	'HP',
	'Injection',
	'Oil Coriolis',
	'Water Coriolis',
	'LP Separator',
	'HP Separator',
	'Injection Valve',
	'Choke Valve',
	],
	3: [  ### Well 3 Equipment ###
	'LP',
	'HP',
	'Injection',
	'Oil Coriolis',
	'Water Coriolis',
	'LP Separator',
	'HP Separator',
	'Injection Valve',
	'Choke Valve',
	],
	4: [  ### Well 4 Equipment ###
	'LP',
	'HP',
	'Injection',
	'Oil Coriolis',
	'Water Coriolis',
	'LP Separator',
	'HP Separator',
	'Injection Valve',
	'Choke Valve',
	],
	5: [  ### Well 5 Equipment ###
	'LP',
	'HP',
	'Injection',
	'Oil Coriolis',
	'Water Coriolis',
	'LP Separator',
	'HP Separator',
	'Injection Valve',
	'Choke Valve',
	],
	6: [  ### Well 6 Equipment ###
	'LP',
	'HP',
	'Injection',
	'Oil Coriolis',
	'Water Coriolis',
	'LP Separator',
	'HP Separator',
	'Injection Valve',
	'Choke Valve',
	],
}

# Update with associated merrickids
wellMerrickDict = {
	1: [  ### Well 1 Merrick IDs ###
	0,  # Well
	0,  # LP
	0,  # HP
	0,  # Injection
	0,  # Oil Coriolis
	0,  # Water Coriolis
	0,  # LP Separator
	0,  # HP Separator
	0,  # Injection Valve
	0,  # Choke Valve
	],
	2: [  ### Well 2 Merrick IDs ###
	0,  # Well
	0,  # LP
	0,  # HP
	0,  # Injection
	0,  # Oil Coriolis
	0,  # Water Coriolis
	0,  # LP Separator
	0,  # HP Separator
	0,  # Injection Valve
	0,  # Choke Valve
	],
	3: [  ### Well 3 Merrick IDs ###
	0,  # Well
	0,  # LP
	0,  # HP
	0,  # Injection
	0,  # Oil Coriolis
	0,  # Water Coriolis
	0,  # LP Separator
	0,  # HP Separator
	0,  # Injection Valve
	0,  # Choke Valve
	],
	4: [  ### Well 4 Merrick IDs ###
	0,  # Well
	0,  # LP
	0,  # HP
	0,  # Injection
	0,  # Oil Coriolis
	0,  # Water Coriolis
	0,  # LP Separator
	0,  # HP Separator
	0,  # Injection Valve
	0,  # Choke Valve
	],
	5: [  ### Well 5 Merrick IDs ###
	0,  # Well
	0,  # LP
	0,  # HP
	0,  # Injection
	0,  # Oil Coriolis
	0,  # Water Coriolis
	0,  # LP Separator
	0,  # HP Separator
	0,  # Injection Valve
	0,  # Choke Valve
	],
	6: [  ### Well 6 Merrick IDs ###
	0,  # Well
	0,  # LP
	0,  # HP
	0,  # Injection
	0,  # Oil Coriolis
	0,  # Water Coriolis
	0,  # LP Separator
	0,  # HP Separator
	0,  # Injection Valve
	0,  # Choke Valve
	],
}



# comment out equipment that do not apply
METER_CONFIG = {
'Sales NGL': [Meta.Tag.config.FWT_NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 1],
'Cushion NGL': [Meta.Tag.config.FWT_NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 2],
'Suction NGL': [Meta.Tag.config.FWT_NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 3],
'Bulk NGL': [Meta.Tag.config.FWT_NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 4],
'VRU Meter': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'VRU Meter', 'merrickid': 0}, 9],
'HP Sales Check': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Check Meter', 'merrickid': 0}, 10],
'Flare Meter': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Flare Meter', 'merrickid': 0}, 18],
'Fuel Meter': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Fuel Meter', 'merrickid': 0}, 19],
'LP Sales Check': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Check Meter', 'merrickid': 0}, 20],
'Comp 1 Meter': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Comp Meter', 'merrickid': 0}, 21],
'Comp 2 Meter': [Meta.Tag.config.FWT_DPMETER, {'type': 'Gas Meter', 'subtype': 'Comp Meter', 'merrickid': 0}, 22],
'Flare Fox Meter': [Meta.Tag.config.FWT_THERMAL_METER, {'type': 'Gas Meter', 'subtype': 'Thermal Mass Meter', 'merrickid': 0}, 1],
'VRU Fox Meter': [Meta.Tag.config.FWT_THERMAL_METER, {'type': 'Gas Meter', 'subtype': 'Thermal Mass Meter', 'merrickid': 0}, 2],
}

# comment out equipment that do not apply
VESSEL_CONFIG = {
'VRT Vessel': [Meta.Tag.config.FWT_VRT_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'Cushion Vessel': [Meta.Tag.config.FWT_CUSHION_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'Heater 1 Vessel': [Meta.Tag.config.FWT_HEATER1_VESSEL, {'type': 'Vessel', 'subtype': 'Heater Treater Vessel', 'merrickid': 0}, 1],
'Heater 2 Vessel': [Meta.Tag.config.FWT_HEATER2_VESSEL, {'type': 'Vessel', 'subtype': 'Heater Treater Vessel', 'merrickid': 0}, 2],
'LP Flare Vessel': [Meta.Tag.config.FWT_LP_FLARE_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'LP Annulus Vessel': [Meta.Tag.config.FWT_LP_ANNULUS_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'LP Sales Vessel': [Meta.Tag.config.FWT_LP_SALES_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'HP Flare Vessel': [Meta.Tag.config.FWT_HP_FLARE_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'HP Annulus Vessel': [Meta.Tag.config.FWT_HP_ANNULUS_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}], 
'HP Sales Vessel': [Meta.Tag.config.FWT_HP_SALES_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}], 
'LP Gas Scrubber Vessel': [Meta.Tag.config.FWT_LP_GAS_SCRUBBER_VESSEL, {'type': 'Vessel', 'subtype': 'Scrubber Vessel', 'merrickid': 0}],
'Dehy Vessel': [Meta.Tag.config.FWT_DEHY_VESSEL, {'type': 'Vessel', 'subtype': 'Scrubber Vessel', 'merrickid': 0}],
'Blanket Gas Vessel': [Meta.Tag.config.FWT_BLANKET_GAS_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'Dehy Vessel': [Meta.Tag.config.FWT_DEHY_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
'Flare Fuel Vessel': [Meta.Tag.config.FWT_FLARE_FUEL_VESSEL, {'type': 'Vessel', 'subtype': 'Vessel', 'merrickid': 0}],
}

# comment out equipment that do not apply
FLARE_CONFIG = {
'Flare': [Meta.Tag.config.FWT_FLARE, {'type': 'Flare', 'subtype': 'Flare', 'merrickid': 0}, 1],
}

# comment out equipment that do not apply
PUMP_CONFIG = {
'Transfer Pump 1': [Meta.Tag.config.FWT_TRANSFER_PUMP, {'type': 'Pump', 'subtype': 'Transfer Pump', 'merrickid': 0}, 1],
'Transfer Pump 2': [Meta.Tag.config.FWT_TRANSFER_PUMP, {'type': 'Pump', 'subtype': 'Transfer Pump', 'merrickid': 0}, 2],
}

### Do Not Modify ###
COMPRESSOR_CONFIG = {}
for num in range(compDict['gas']):
	COMPRESSOR_CONFIG['Compressor ' + str(num+1)] = [Meta.Tag.config.FWT_COMPRESSOR, {'type': 'Gas Compressor', 'subtype': 'Gas Compressor', 'merrickid':0}, num+1, 0]
for num in range(compDict['vru']):
	COMPRESSOR_CONFIG['VRU Compressor ' + str(num+1)] = [Meta.Tag.config.FWT_COMPRESSOR, {'type': 'Gas Compressor', 'subtype': 'VRU Compressor', 'merrickid':0}, num+1, 1]
if 'air' in compDict and compDict['air']:
	COMPRESSOR_CONFIG['Air Compressor'] = [Meta.Tag.config.FWT_AIR_COMPRESSOR, {'type': 'Air Compressor', 'subtype': 'Air Compressor', 'merrickid':0}]
	
TANK_CONFIG = {}
for num in range(tankDict['oil tanks']):
	TANK_CONFIG['Oil Tank ' + str(num+1)] = [
		Meta.Tag.config.FWT_TANK, 
		{'type': 'Tank', 'subtype': 'Oil Tank', 'merrickid':tankMerrickDict['oil tanks'][num] if len(tankMerrickDict['oil tanks']) > num else 0}, 
		num+1, 
		0, 
		{'_p_Gun Barrel': 0}
		] 
for num in range(tankDict['water tanks']):
	TANK_CONFIG['Water Tank ' + str(num+1)] = [
	Meta.Tag.config.FWT_TANK, 
		{'type': 'Tank', 'subtype': 'Water Tank', 'merrickid':tankMerrickDict['water tanks'][num] if len(tankMerrickDict['water tanks']) > num else 0}, 
		num+1, 
		1, 
		{'_p_Gun Barrel': 0}
		]
for num in range(tankDict['gun barrel tanks']):
	TANK_CONFIG['Gun Barrel Tank ' + str(num+1)] = [
		Meta.Tag.config.FWT_TANK, 
		{'type': 'Tank', 'subtype': 'Gun Barrel Tank', 'merrickid':tankMerrickDict['gun barrel tanks'][num] if len(tankMerrickDict['gun barrel tanks']) > num else 0}, 
		num+1, 
		0, 
		{'_p_Gun Barrel': 1}
		]

FACILITY_PIPELINE_CONFIG = {
	'Facility Pipeline': [Meta.Tag.config.FWT_PIPELINE_FACILITY, {'type': 'Facility', 'subtype': 'Facility Pipeline', 'merrickid': 0}],
}

# comment out any equipment type that do not apply
upperSiteConfigDict =  {
	'TANK': TANK_CONFIG,
	'METER': METER_CONFIG,
	'PUMP': PUMP_CONFIG,
	'VESSEL' : VESSEL_CONFIG,
	'FLARE' : FLARE_CONFIG,
	'COMPRESSOR' : COMPRESSOR_CONFIG,
	'FACILITY' : FACILITY_PIPELINE_CONFIG,
	}

siteConfigDict = {key.lower(): val.keys() for key, val in upperSiteConfigDict.items()}
device = Meta.Tag.Make.build_device(deviceName, siteName, deviceType, area, documentation)
### Do Not Modify ###  
siteDict = {'well_' + str(idx): {'name':wellDict[idx], 'equip': wellEquipDict[idx], 'mid': wellMerrickDict[idx]} for idx in range(1, numWells + 1)}
siteDict['site'] = siteConfigDict
siteDict['facility'] = True
siteDict['documentation'] = documentation


def check():
	Meta.Tag.Make.SiteBuilder(device, siteDict, well_config_build=well_build, site_configs=upperSiteConfigDict, well_adaptor=Meta.Tag.config.FWT_WELL, facility_adaptor=Meta.Tag.config.FWT_FACILITY, injection_dict=DPMETER_NUMS)
	
def run():
	Meta.Tag.Make.SiteBuilder(device, siteDict, well_config_build=well_build, site_configs=upperSiteConfigDict, well_adaptor=Meta.Tag.config.FWT_WELL, facility_adaptor=Meta.Tag.config.FWT_FACILITY, injection_dict=DPMETER_NUMS).build(primary_hauler=primary_hauler, fluid_transport=fluid_transport)
