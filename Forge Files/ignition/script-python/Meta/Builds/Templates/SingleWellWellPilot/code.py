class Template:
	def __init__(self):
		siteName = '' # Update Name  
		### IMPORTANT -> MAKE SURE TO BUILD THE DEVICE IN AUTOSOLO AND ENABLE THE DEVICE BEFORE RUNNING FINAL `run` FUNCTION ###
		deviceName = '' # Update Device Name from Autosol
		area = 'North' # List area (North/South)
		documentation = '' # Update Documentation/ticket reference  
		numWells = 0 # Update number of wells
		self.wellTemplate = Meta.Tag.config.WELL # Update well template
		self.facilityTemplate = Meta.Tag.config.FACILITY # Update facility template
		self.buildFacility = False # Update to true if facility equipment build out is required
		self.primary_hauler = None # Update with hauler name is tanks are included in the build
		self.fluid_transport = 3 # Update with fluid transport number (1: Piped, 2: Hauled, 3: None) 
		
		#Update with well names. 
		wellDict = {
			1: '',
		}
		
		# Update Number of tanks
		tankDict = {
			'oil tanks': 1,
			'water tanks': 1,
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
		
		#Update Injection Meter Nums as Necessary
		DPMETER_NUMS = {
		
		}
		
		### WELL-LEVEL EQUIPMENT CONFIGURATION ### 
		# Comment out any equipment that does not apply
		wellEquipDict = {
			1: [  ### Well 1 Equipment ###
		
			],
		
		}
		
		wellMerrickDict = {
			1: [  ### Well 1 Merrick IDs ###
			0, # Well MerrickID
			],}
			
				### TO DO: Flat Sales Meter creation utility addition ###	
		## comment out equipment that do not apply
		#METER_CONFIG = {
		#'Sales Meter': [Meta.Tag.config.SALES_METER, {'type': 'Gas Meter', 'subtype': 'Sales Meter', 'merrickid': 0}],
		#}
		POC_CONFIG = {
		'POC': [Meta.Tag.config.POC, {'type': 'POC', 'subtype': 'POC', 'merrickid': 0}],
		}
		
		### Do Not Modify ###
		COMPRESSOR_CONFIG = {}
		for num in range(compDict['gas']):
			COMPRESSOR_CONFIG['Compressor ' + str(num+1)] = [Meta.Tag.config.COMPRESSOR, {'type': 'Gas Compressor', 'subtype': 'Gas Compressor', 'merrickid':0}, num+1]
		for num in range(compDict['vru']):
			COMPRESSOR_CONFIG['VRU Compressor ' + str(num+1)] = [Meta.Tag.config.VRU_COMPRESSOR, {'type': 'Gas Compressor', 'subtype': 'VRU Compressor', 'merrickid':0}, num+1]
		
		### Do Not Modify ###
		TANK_CONFIG = {}
		for num in range(tankDict['oil tanks']):
			TANK_CONFIG['Oil Tank ' + str(num+1)] = [
				Meta.Tag.config.TANK, 
				{'type': 'Tank', 'subtype': 'Oil Tank', 'merrickid':tankMerrickDict['oil tanks'][num] if len(tankMerrickDict['oil tanks']) > num else 0}, 
				num+1, 
				0, 
				{'_p_GunBarrel': 0}
				] 
		for num in range(tankDict['water tanks']):
			TANK_CONFIG['Water Tank ' + str(num+1)] = [
			Meta.Tag.config.TANK, 
				{'type': 'Tank', 'subtype': 'Water Tank', 'merrickid':tankMerrickDict['water tanks'][num] if len(tankMerrickDict['water tanks']) > num else 0}, 
				num+1, 
				1, 
				{'_p_GunBarrel': 0}
				]
		for num in range(tankDict['gun barrel tanks']):
			TANK_CONFIG['Gun Barrel Tank ' + str(num+1)] = [
				Meta.Tag.config.TANK, 
				{'type': 'Tank', 'subtype': 'Gun Barrel Tank', 'merrickid':tankMerrickDict['gun barrel tanks'][num] if len(tankMerrickDict['gun barrel tanks']) > num else 0}, 
				num+1, 
				0, 
				{'_p_GunBarrel': 1}
				]
				
		# comment out any equipment type that do not apply
		self.upperSiteConfigDict =  {
			'POC': POC_CONFIG,
			'TANK': TANK_CONFIG,
		#	'METER': METER_CONFIG,
			'COMPRESSOR' : COMPRESSOR_CONFIG,
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
		}
		return config_dict

	def check(self):
		Meta.Tag.Make.SiteBuilder(self.device, self.siteDict, well_config_build=self.well_build, site_configs=self.upperSiteConfigDict, well_adaptor=self.wellTemplate, facility_adaptor=self.facilityTemplate)
		
	def run(self):
		Meta.Tag.Make.SiteBuilder(self.device, self.siteDict, well_config_build=self.well_build, site_configs=self.upperSiteConfigDict, well_adaptor=self.wellTemplate, facility_adaptor=self.facilityTemplate).build(primary_hauler=self.primary_hauler, fluid_transport=self.fluid_transport)