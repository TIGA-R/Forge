import warnings
SERVER = 'ACM01'

DEVICE_DICT = {
'Emerson FB 3000 v01': 'fb3000',
'Fisher ROC Ethernet v02': 'fisher800',
'WellPilot v01': 'wellpilot',
'Emerson FB 2000 v01': 'fb2000',
'EprodEXS1000 Serial v01': 'exs1000',
'Emerson ROC Ethernet v02': 'emerson107',
'RealFloPPLUS v01': 'scadapack',
'Modbus TCP v02': 'modbus',
'ABB Totalflow v02': 'totalflow',
'ABB Totalflow RMC': 'totalflow',
'Eprod8800 Serial v01': 'eprod8800',
'Modbus EMIT v01': 'modbus_emit',
'Smarten Modbus TCP v01' : 'smarten',
}

def equipment_adaptor(cls):
	cls.__repr__ = 'Equipment Adaptor: %s'%cls.__name__
	if not hasattr(cls, 'folder'):
		raise AttributeError('%s EquipmentAdaptor: Object must include `folder` attribute.'%cls.__name__)
	if not isinstance(cls.folder, str):
		raise TypeError('%s EquipmentAdaptor: Correct folder type to str type.'%cls.__name__)
	if not hasattr(cls, 'suffix'):
		raise AttributeError('%s EquipmentAdaptor: Object must include `folder` attribute.'%cls.__name__)
	if not isinstance(cls.suffix, str):
		raise TypeError('%s EquipmentAdaptor: Correct suffix type to str type.'%cls.__name__)
	has_template = False
	device_type_list = [val for val in DEVICE_DICT.values()]
	for attr in cls.__dict__.keys():
		if not 'template' in attr:
			continue
		has_template = True
		device_type = attr.split('_')[0]
		if device_type not in device_type_list:
			raise TypeError('%s EquipmentAdaptor: No device type defined in DEVICE_DICT for template: %s'%(cls.__name__, device_type))
		if 'Sites/_Meta' not in getattr(cls, attr):
			raise AttributeError('%s EquipmentAdaptor: Template tag: %s needs to be relocated to a Sites/_Meta folder structure'%(cls.__name__, attr))
		if '_types_/' in getattr(cls, attr):
			raise AttributeError('%s EquipmentAdaptor: Template tag: %s needs to be genericized to remove tag provider source (remove [Tag Provider]_types_/ prefix)'%(cls.__name__, attr))
	if not has_template:
		raise AttributeError('%s EquipmentAdaptor: No template defined for this equipment adaptor'%cls.__name__)
	return cls

TAG_DICT = {val: 'REMOTE DEVICE/' + key for key, val in DEVICE_DICT.items()}

DEFAULT_DPMETER_NUMS = {
'injection_1': 7,
'injection_2': 8,
'injection_3': 17,
'injection_4': 18,
'injection_5': 21,
'injection_6': 22,
'injection_7': 23,
'injection_7': 24,
}
###### EquipmentBuilder Configs ######

### Compressor ###
@equipment_adaptor
class COMPRESSOR:
	"""
	equipment_parameter: _Comp Num (int)
	"""
	folder = 'Compressor'
	suffix = 'Compressor'
	equipment_parameter = '_e_Comp Num'
	equipment_parameter_2 = '_p_Engineering'
	fb3000_template = 'COMPRESSOR/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Compressor'
	exs1000_template = 'COMPRESSOR/EProdEXS1000/Sites/_Meta/EProdEXS1000 Core Compressor'
	scadapack_template = 'COMPRESSOR/RealFloPPLUS/Sites/_Meta/RealFloPPLUS Compressor v01'
	emerson107_template = 'COMPRESSOR/EMERSON107/Sites/_Meta/Emerson107 Core Compressor'
	wellpilot_template = 'COMPRESSOR/WELLPILOTRPOC/Sites/_Meta/WellPilot Core Compressor'
	totalflow_template = 'COMPRESSOR/TotalFlow/Sites/_Meta/TotalFlow TIGA Core Compressor'
	fisher800_template = 'COMPRESSOR/Fisher 800/Sites/_Meta/Fisher800 Core Compressor'
	modbus_template = 'COMPRESSOR/Modbus/Sites/_Meta/Modbus TIGA Core Compressor'
	eprod8800_template = 'COMPRESSOR/EProd 8800/Sites/_Meta/EProd8800 Compressor v01'
	modbus_emit_template = 'COMPRESSOR/Modbus/Sites/_Meta/Modbus EMIT Compressor'
	

@equipment_adaptor
class VRU_COMPRESSOR:
	"""
	equipment_parameter: _Comp Num (int)
	"""
	folder = 'Compressor'
	suffix = 'VRU Compressor'
	equipment_parameter = '_Comp Num'
	fb3000_template = 'COMPRESSOR/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core VRU Compressor'
	totalflow_template = 'COMPRESSOR/Totalflow/Sites/_Meta/Totalflow Core VRU Compressor'

### James Croft Template ###
@equipment_adaptor
class PTW_COMPRESSOR:
	"""
	James Croft Template
	equipment_parameter: _e_Comp Num (int)
	equipment_parameter_2: _e_VRU (bool, 0/1)
	"""
	folder = 'Compressor'
	suffix = 'FWT Compressor'
	equipment_parameter = '_e_Comp Num'
	equipment_parameter_2 = '_e_VRU'
	fb3000_template = 'COMPRESSOR/EmersonFB3000/Sites/_Meta/EmersonFB3000 Plunger Transition Compressor'

@equipment_adaptor
class FWT_COMPRESSOR:
	"""
	equipment_parameter: _e_Comp Num (int)
	equipment_parameter_2: _e_VRU (bool, 0/1)
	"""
	folder = 'Compressor'
	suffix = 'FWT Compressor'
	equipment_parameter = '_e_Comp Num'
	equipment_parameter_2 = '_e_VRU'
	fb3000_template = 'COMPRESSOR/EmersonFB3000/Sites/_Meta/FB3000 Five Well Compressor'
	
@equipment_adaptor
class FWT_AIR_COMPRESSOR:
	folder = 'Compressor'
	suffix = 'FWT Air Compressor'
	fb3000_template = 'COMPRESSOR/EmersonFB3000/Sites/_Meta/FB3000 Five Well Air Compressor'

### Facility ###

@equipment_adaptor
class FACILITY:
	folder = 'Facility'
	suffix = 'Facility'
	fisher800_template = 'FACILITY/Fisher 800/Sites/_Meta/Fisher 800 TIGA Core Flat Facility'
	fb3000_template = 'FACILITY/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Facility'
	emerson107_template = 'FACILITY/EMERSON107/Sites/_Meta/Emerson107 Core Facility'
	totalflow_template = 'FACILITY/Totalflow/Sites/_Meta/TotalFlow TIGA Core Facility'

@equipment_adaptor
class FACILITY_PIPELINE:
	folder = 'Facility' 
	suffix = 'Facility Pipeline'
	fb3000_template = 'FACILITY/EmersonFB3000/Sites/_Meta/EmersonFB3000 Core Facility Pipeline'
	fisher800_template = 'FACILITY/Fisher 800/Sites/_Meta/Fisher 800 Facility Pipeline'


@equipment_adaptor
class FACILITY_FIRST_OUT:
	"""
	equipment_parameter: _Well Num (int)
	"""
	folder = 'Facility'
	suffix = 'Alarms'
	fb3000_template = 'WELL/EmersonFB3000/Sites/_Meta/EmersonFB3000 First Out Alarm'
	fisher800_template = 'WELL/Fisher 800/Sites/_Meta/Fisher 800 First Out Alarm'
	emerson107_template = 'WELL/Emerson107/Sites/_Meta/Emerson107 First Out Alarm'
	equipment_parameter = '_Well Num'

@equipment_adaptor
class FWT_FACILITY:
	folder = 'Facility'
	suffix = 'FWT Facility'
	fb3000_template = 'FACILITY/EmersonFB3000/Sites/_Meta/FB3000 Five Well Facility'

@equipment_adaptor
class FWT_FACILITY_PIPELINE:
	folder = 'Facility' 
	suffix = 'FWT Facility Pipeline'
	fb3000_template = 'FACILITY/EmersonFB3000/Sites/_Meta/FB3000 Five Well Facility Pipeline'

@equipment_adaptor
class TWT_FACILITY:
	folder = 'Facility'
	suffix = 'FWT Facility'
	totalflow_template = 'FACILITY/Totalflow/Sites/_Meta/TotalFlow TWT Facility'

@equipment_adaptor
class TWT_FACILITY_FIRST_OUT:
	"""
	equipment_parameter: _Well Num (int)
	"""
	folder = 'Facility'
	suffix = 'Alarms'
	totalflow_template = 'WELL/Totalflow/Sites/_Meta/TotalFlow TWT First Out Alarm'
	equipment_parameter = '_Well Num'
### Flare ###

@equipment_adaptor
class FLARE:
	"""
	equipment_parameter: _Flare (bool)
	"""
	folder = 'Flare'
	suffix = 'Flare'
	equipment_parameter = '_Flare'
	fb3000_template = 'FLARE/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Flare'
	totalflow_template = 'FLARE/TotalFlow/Sites/_Meta/TotalFlow TIGA Core Flare'

@equipment_adaptor
class FWT_FLARE:
	"""
	equipment_parameter: _e_Flare Num (int)
	"""
	folder = 'Flare'
	suffix = 'FWT Flare'
	equipment_parameter = '_e_Flare Num'
	fb3000_template = 'FLARE/EmersonFB3000/Sites/_Meta/FB3000 Five Well Flare'

### James Croft Template ###
@equipment_adaptor
class PTW_FLARE:
	"""
	James Croft Template
	equipment_parameter: _e_Flare Num (int)
	"""
	folder = 'Flare'
	suffix = 'PTW Flare'
	equipment_parameter = '_e_Flare Num'
	fb3000_template = 'FLARE/EmersonFB3000/Sites/_Meta/EmersonFB3000 Plunger Transition Flare'

### Meters ###
@equipment_adaptor
class DPMETER:
	"""
	equipment_parameter: __Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'DPMeter'
	equipment_parameter = '__Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core DPMeter'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core DPMeter'
	emerson107_template = 'METER/EMERSON107/Sites/_Meta/Emerson107 Core DPMeter'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Gas Meter'
	scadapack_template = 'METER/RealFloPPLUS/Sites/_Meta/RealFloPPLUS Core DPMeter'

@equipment_adaptor
class WELL_DPMETER:
	"""
	equipment_parameter: _Well Num (int)
	equipment_parameter_2: _LP (bool)
	"""
	folder = 'Meter'
	suffix = 'DPMeter'
	equipment_parameter = '_Well Num'
	equipment_parameter_2 = '_LP'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core DPMeter'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core DPMeter'
	emerson107_template = 'METER/EMERSON107/Sites/_Meta/Emerson107 Core DPMeter'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Gas Meter'

@equipment_adaptor
class FWT_DPMETER:
	"""
	equipment_parameter: _e_Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'FWT DPMeter'
	equipment_parameter = '_e_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/FB3000 Five Well DPMeter'

@equipment_adaptor
class FWT_WELL_DPMETER:
	"""
	equipment_parameter: _p_Well Num (int)
	equipment_parameter_2: _p_LP (bool)
	"""
	folder = 'Meter'
	suffix = 'FWT DPMeter'
	equipment_parameter = '_p_Well Num'
	equipment_parameter_2 = '_p_LP'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/FB3000 Five Well DPMeter'

@equipment_adaptor
class VORTEX_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Vortex Meter'
	equipment_parameter = '_Meter Num'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core Vortex Meter'

@equipment_adaptor
class CORIOLIS_METER:
	"""
	equipment_parameter: __Coriolis Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Coriolis Meter'
	equipment_parameter = '__Coriolis Meter Num'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core Coriolis Meter'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Coriolis'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Liquid Meter'
	
@equipment_adaptor
class OIL_CORIOLIS_METER:
	"""
	equipment_parameter: __Coriolis Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Oil Coriolis Meter'
	equipment_parameter = '__Coriolis Meter Num'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Oil Coriolis Meter'
	
@equipment_adaptor
class CORIOLIS_METER_PMSC:
	"""
	equipment_parameter: __Coriolis Meter Num (int)
	equipment_parameter_2: _Water (bool)
	"""
	folder = 'Meter'
	suffix = 'Coriolis Meter'
	equipment_parameter = '__Coriolis Meter Num'
	equipment_parameter_2 = '_Water'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Coriolis - PMscAccum'

@equipment_adaptor
class FWT_OIL_CORIOLIS:
	"""
	equipment_parameter: _p_Well Num (int)
	"""
	folder = 'Meter'
	suffix = 'FWT Oil Coriolis'
	equipment_parameter = '_p_Well Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/FB3000 Five Well Oil Coriolis'

@equipment_adaptor
class FWT_WATER_CORIOLIS:
	"""
	equipment_parameter: _p_Well Num (int)
	"""
	folder = 'Meter'
	suffix = 'FWT Water Coriolis'
	equipment_parameter = '_p_Well Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/FB3000 Five Well Water Coriolis'

@equipment_adaptor
class TWT_WELL_LIQUID_METER:
	"""
	equipment_parameter: _p_Meter Num (int)
	equipment_parameter_2: _p_Water (bool, 0/1)
	"""
	folder = 'Meter'
	suffix = 'FWT Coriolis'
	equipment_parameter = '_p_Meter Num'
	equipment_parameter_2 = '_p_Water'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TWT Liquid Meter'

@equipment_adaptor
class TWT_LIQUID_METER:
	"""
	equipment_parameter: _e_AppConfig (int)
	"""
	folder = 'Meter'
	suffix = 'FWT Coriolis'
	equipment_parameter = '_e_AppConfig'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TWT Liquid Meter'
	
@equipment_adaptor
class TURBINE_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Turbine Meter'
	equipment_parameter = '_Meter Num'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core Turbine Meter'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Turbine'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Liquid Meter'
	
@equipment_adaptor
class WATER_TURBINE_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Water Turbine Meter'
	equipment_parameter = '_Meter Num'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Water Turbine Meter'

@equipment_adaptor
class LR_TURBINE_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Turbine Meter'
	equipment_parameter = '_Meter Num'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow LimeRock Liquid Meter'

@equipment_adaptor
class FWT_WATER_TURBINE:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'FWT Turbine Meter'
	equipment_parameter = '_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Turbine'

@equipment_adaptor
class SWD_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'SWD Meter'
	equipment_parameter = '_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core SWD'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core SWD Meter'

@equipment_adaptor
class LACT_METER:
	"""
	equipment_parameter: _Lact Num (int)
	"""
	folder = 'Meter'
	suffix = 'LACT Meter'
	equipment_parameter = '_Lact Num'
	fb2000_template = 'METER/EmersonFB2000/Sites/_Meta/EmersonFB2000 TIGA Core LACT Meter v01'

	### TO DO: Flat Sales Meter creation utility addition ###	
#class SALES_METER:
#	folder = 'Meter'
#	suffix = 'Sales Meter'

@equipment_adaptor
class WELL_TURBINE_METER:
	"""
	equipment_parameter: _Well Num (int)
	equipment_parameter_2: _Water
	"""
	folder = 'Meter'
	suffix = 'Turbine Meter'
	equipment_parameter = '_Well Num'
	equipment_parameter_2 = '_Water'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core Turbine Meter'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Turbine'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Liquid Meter'

@equipment_adaptor
class WELL_CORIOLIS_METER:
	"""
	equipment_parameter: _Well Num (int)
	equipment_parameter_2: _Water
	"""
	folder = 'Meter'
	suffix = 'Coriolis Meter'
	equipment_parameter = '_Well Num'
	equipment_parameter_2 = '_Water'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core Coriolis Meter'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Coriolis'

@equipment_adaptor
class VORTEX_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Vortex Meter'
	equipment_parameter = '_Meter Num'
	fisher800_template = 'METER/Fisher 800/Sites/_Meta/Fisher 800 Core Vortex Meter'

@equipment_adaptor
class THERMAL_METER:
	"""
	equipment_parameter: _e_Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Thermal Mass Meter'
	equipment_parameter = '_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Thermal Mass Meter'

@equipment_adaptor
class FWT_THERMAL_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Thermal Mass Meter'
	equipment_parameter = '_e_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/FB3000 Five Well Thermal Mass Meter'

@equipment_adaptor
class NGL_METER:
	"""
	equipment_parameter: _Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'NGL Meter'
	equipment_parameter = '_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core NGL Meter'

@equipment_adaptor
class FWT_NGL_METER:
	"""
	equipment_parameter: _e_Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'FWT NGL Meter'
	equipment_parameter = '_e_Meter Num'
	fb3000_template = 'METER/EmersonFB3000/Sites/_Meta/FB3000 Five Well NGL Meter'

### Pumps ###
@equipment_adaptor
class PUMP:
	"""
	equipment_parameter: _Pump Num (int)
	"""
	folder = 'Pump'
	suffix = 'Pump'
	equipment_parameter = '_Pump Num'
	fb3000_template = 'PUMP/EmersonFB3000/Sites/_Meta/EmersonFB3000 Core Pump'
	exs1000_template = 'PUMP/EProdEXS1000/Sites/_Meta/EProdEXS1000 Core Pump'
	totalflow_template = 'PUMP/TotalFlow/Sites/_Meta/TotalFlow TIGA Core Pump'

@equipment_adaptor
class FWT_TRANSFER_PUMP:
	"""
	equipment_parameter: _e_Pump Num (int)
	"""
	folder = 'Pump'
	suffix = 'FWT Transfer Pump'
	equipment_parameter = '_e_Pump Num'
	fb3000_template = 'PUMP/EmersonFB3000/Sites/_Meta/FB3000 Five Well Transfer Pump'

@equipment_adaptor
class SWD_PUMP:
	folder = 'Pump'
	suffix = 'SWD Pump'
	fisher800_template = 'PUMP/Fisher 800/Sites/_Meta/Fisher 800 Core SWD Pump'

### Tanks ###
@equipment_adaptor
class TANK:
	"""
	equipment_parameter: _Tank Num (int)
	equipment_parameter_2: _Water (bool)
	"""
	folder = 'Tank'
	suffix = 'Tank'
	equipment_parameter = '_Tank Num'
	equipment_parameter_2 = '_Water'
	fisher800_template = 'TANK/Fisher 800/Sites/_Meta/Fisher 800 TIGA Core TANK'
	fb3000_template = 'TANK/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Tank'
	wellpilot_template = 'TANK/WELLPILOTRPOC/Sites/_Meta/WellPilot TIGA Core Tank'
	exs1000_template = 'TANK/EProdEXS1000/Sites/_Meta/EProdEXS1000 Core Tank'
	emerson107_template = 'TANK/EMERSON107/Sites/_Meta/Emerson107 Core Tank'
	modbus_template = 'TANK/Modbus Logic ACM/Sites/_Meta/Modbus Logic ACM TIGA Core Tank'
	totalflow_template = 'TANK/Totalflow/Sites/_Meta/TotalFlow LimeRock Tank'
	scadapack_template = 'TANK/RealFloPPLUS/Sites/_Meta/RealFloPPLUS Core Tank'
	eprod8800_template = 'TANK/EProd 8800/Sites/_Meta/EPROD 8800 TIGA Core Tank'
	
@equipment_adaptor
class REFERENCE_TANK:
	"""
	equipment_parameter: Reference Tank (string)
	"""
	folder = 'Tank'
	suffix = 'Reference Tank'
	equipment_parameter = 'Reference Tank'
	fisher800_template = 'TANK/Fisher 800/Sites/_Meta/Reference Tank'
	fb3000_template = 'TANK/EmersonFB3000/Sites/_Meta/Reference Tank'
	wellpilot_template = 'TANK/WELLPILOTRPOC/Sites/_Meta/Reference Tank'
	exs1000_template = 'TANK/EProdEXS1000/Sites/_Meta/Reference Tank'
	emerson107_template = 'TANK/EMERSON107/Sites/_Meta/Reference Tank'
	totalflow_template = 'TANK/TotalFlow/Sites/_Meta/Reference Tank'
	scadapack_template = 'TANK/RealFloPPLUS/Sites/_Meta/Reference Tank'
	eprod8800_template = 'TANK/EProd 8800/Sites/_Meta/Reference Tank'

@equipment_adaptor
class FWT_TANK:
	"""
	equipment_parameter: _p_Tank Num (int)
	equipment_parameter_2: _p_Water (bool)
	"""
	folder = 'Tank'
	suffix = 'Tank'
	equipment_parameter = '_p_Tank Num'
	equipment_parameter_2 = '_p_Water'
	fb3000_template = 'TANK/EmersonFB3000/Sites/_Meta/FB3000 Five Well Tank'
	
@equipment_adaptor
class BULLET_TANK:
	"""
	equipment_parameter: _p_Tank Num (int)
	equipment_parameter_2: _p_Water (bool)
	"""
	folder = 'Tank'
	suffix = 'Tank'
	equipment_parameter = '_p_Tank Num'
	equipment_parameter_2 = '_p_Water'
	fb3000_template = 'TANK/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Bullet Tank'

@equipment_adaptor
class TWT_TANK:
	"""
	equipment_parameter: _Tank Num (int)
	equipment_parameter_2: _Water (bool, 0/1)
	"""
	folder = 'Tank'
	suffix = 'Tank'
	equipment_parameter = '_Tank Num'
	equipment_parameter_2 = '_Water'
	totalflow_template = 'TANK/Totalflow/Sites/_Meta/TotalFlow TWT Tank'
	
### PLUNGER ###
@equipment_adaptor
class PLUNGER:
	"""
	equipment_parameter: Plunger Instance Number (int, 1+, ROC800 0+)
	"""
	folder = 'Plunger'
	suffix = 'Plunger'
	equipment_parameter = 'Plunger Instance Number'
	fb3000_template = 'PLUNGER/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Plunger'
	totalflow_template = 'PLUNGER/Totalflow/Sites/_Meta/Totalflow Plunger Lift Controller'
	scadapack_template = 'PLUNGER/RealFloPPLUS/Sites/_Meta/RealFloPPLUS Core Plunger'
	fisher800_template = 'PLUNGER/Fisher800/Sites/_Meta/ROC800 TIGA Core Plunger'

class TWT_PLUNGER:
	"""
	equipment_parameter: _e_AppConfig (int, 1+)
	"""
	folder = 'Plunger'
	suffix = 'Plunger'
	equipment_parameter = '_e_AppConfig'
	totalflow_template = 'PLUNGER/Totalflow/Sites/_Meta/Totalflow Plunger'
	
### POC ###
@equipment_adaptor
class POC:
	folder = 'POC'
	suffix = 'POC'
	wellpilot_template = 'POC/WELLPILOTRPOC/Sites/_Meta/Wellpilot TIGA Core POC'
	smarten_template = 'POC/Smarten/Sites/_Meta/Smarten TIGA Core POC'
	eprod8800_template = 'POC/EProd 8800/Sites/_Meta/EPROD 8800 LimeRock POC'

### Valves ###
@equipment_adaptor
class VALVE:
	"""
	equipment_parameter: _Valve Num (int)
	equipment_parameter_2: _Choke (bool)
	"""
	# Works for Choke valves and Control Valves
	folder = 'Valve' 
	suffix = 'Valve'
	equipment_parameter = '_Valve Num'
	equipment_parameter_2 = '_Choke'
	fb3000_template = 'VALVE/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Valve'
	fisher800_template = 'VALVE/Fisher 800/Sites/_Meta/Fisher 800 Core Valve'
	emerson107_template = 'VALVE/EMERSON107/Sites/_Meta/Emerson107 TIGA Core Valve'
	totalflow_template = 'VALVE/Totalflow/Sites/_Meta/Totalflow Carizo Core Valve'

@equipment_adaptor
class WELL_VALVE:
	"""
	equipment_parameter: _Well Num (int)
	equipment_parameter_2: _Choke
	"""
	folder = 'Valve' 
	suffix = 'Valve'
	equipment_parameter = '_Well Num'
	equipment_parameter_2 = '_Choke'
	fb3000_template = 'VALVE/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Valve'
	fisher800_template = 'VALVE/Fisher 800/Sites/_Meta/Fisher 800 Core Valve'
	emerson107_template = 'VALVE/EMERSON107/Sites/_Meta/Emerson107 TIGA Core Valve'
	totalflow_template = 'VALVE/Totalflow/Sites/_Meta/Totalflow Carizo Core Valve'

@equipment_adaptor
class FWT_VALVE:
	"""
	equipment_parameter: _p_Well Num (int)
	equipment_parameter_2: _p_LP
	"""
	# Works for Choke valves and Control Valves
	folder = 'Valve' 
	suffix = 'FWT Valve'
	equipment_parameter = '_p_Well Num'
	equipment_parameter_2 = '_p_LP'
	fb3000_template = 'VALVE/EmersonFB3000/Sites/_Meta/FB3000 Five Well Valve'
	
@equipment_adaptor
class BYPASS_VALVE:
	"""
	equipment_parameter: _Valve Num (int)
	"""
	# Works for Choke valves and Control Valves
	folder = 'Valve' 
	suffix = 'Valve'
	equipment_parameter = '_Valve Num'
	fisher800_template = 'VALVE/Fisher 800/Sites/_Meta/Fisher 800 Core Bypass Valve'	
	
### FWT Vessel ###
VESSEL_BASE = 'PMscAct_%d.BLOCK%d_FINAL_RESULT:INT8'
VESSEL_AI_BASE = 'PMeqUsrDf_%d.DOUBLE_%d_VALUE:DOUBLE'
STOCK_VESSEL_PARAMETERS = {
'_t_High Setpoint': {'enable': ['High Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Low Setpoint': {'enable': ['Low Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Pressure': {'enable': ['Pressure'],
		'base': VESSEL_AI_BASE,},
'_t_Temperature': {'enable': ['Temperature'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety High': {'enable': ['Level Safety High', 'Level Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low': {'enable': ['Level Safety Low', 'Level Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety High Oil': {'enable': ['Level Safety High Oil', 'Level Safety High Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Oil': {'enable': ['Level Safety Low Oil', 'Level Safety Low Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Water': {'enable': ['Level Safety Low Water', 'Level Safety Low Water (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety High': {'enable': ['Pressure Safety High', 'Pressure Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety Low': {'enable': ['Pressure Safety Low', 'Pressure Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety High': {'enable': ['Temperature Safety High', 'Temperature Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety Low': {'enable': ['Temperature Safety Low', 'Temperature Safety Low (Message)'],
		'base': VESSEL_BASE,},
		}

MODIFIED_VESSEL_PARAMETERS = {
'_t_High Setpoint': {'enable': ['High Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Low Setpoint': {'enable': ['Low Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Pressure': {'enable': ['Pressure'],
		'base': VESSEL_AI_BASE,},
'_t_Temperature': {'enable': ['Temperature'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety High': {'enable': ['Level Safety High', 'Level Safety High (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety Low': {'enable': ['Level Safety Low', 'Level Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety High Oil': {'enable': ['Level Safety High Oil', 'Level Safety High Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Oil': {'enable': ['Level Safety Low Oil', 'Level Safety Low Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Water': {'enable': ['Level Safety Low Water', 'Level Safety Low Water (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety High': {'enable': ['Pressure Safety High', 'Pressure Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety Low': {'enable': ['Pressure Safety Low', 'Pressure Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety High': {'enable': ['Temperature Safety High', 'Temperature Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety Low': {'enable': ['Temperature Safety Low', 'Temperature Safety Low (Message)'],
		'base': VESSEL_BASE,},
		}

PMEQ_VESSEL_PARAMETERS = {
'_t_High Setpoint': {'enable': ['High Setpoint'],
		 'base': VESSEL_AI_BASE,},
'_t_Low Setpoint': {'enable': ['Low Setpoint'],
		 'base': VESSEL_AI_BASE,},
'_t_Pressure': {'enable': ['Pressure'],
		'base': VESSEL_AI_BASE,},
'_t_Temperature': {'enable': ['Temperature'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety High': {'enable': ['Level Safety High', 'Level Safety High (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety Low': {'enable': ['Level Safety Low', 'Level Safety Low (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety High Oil': {'enable': ['Level Safety High Oil', 'Level Safety High Oil (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety Low Oil': {'enable': ['Level Safety Low Oil', 'Level Safety Low Oil (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Level Safety Low Water': {'enable': ['Level Safety Low Water', 'Level Safety Low Water (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Pressure Safety High': {'enable': ['Pressure Safety High', 'Pressure Safety High (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Pressure Safety Low': {'enable': ['Pressure Safety Low', 'Pressure Safety Low (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Temperature Safety High': {'enable': ['Temperature Safety High', 'Temperature Safety High (Message)'],
		'base': VESSEL_AI_BASE,},
'_t_Temperature Safety Low': {'enable': ['Temperature Safety Low', 'Temperature Safety Low (Message)'],
		'base': VESSEL_AI_BASE,},
}

def mergeDicts(dict1, dict2):
	mergedDict = dict1.copy()
	mergedDict.update(dict2)
	return mergedDict

@equipment_adaptor
class VESSEL:
	"""
	equipment_parameter: __Separator Adder (int)
	"""
	folder = 'Vessel'
	suffix = 'Vessel'
	equipment_parameter = '__Separator Adder'
	fisher800_template = 'VESSEL/Fisher 800/Sites/_Meta/Fisher 800 TIGA Core Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Separator Vessel'
	emerson107_template = 'VESSEL/Emerson107/Sites/_Meta/Emerson107 Core Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TIGA Core Vessel'

@equipment_adaptor
class WELL_VESSEL:
	"""
	equipment_parameter: _Well Num (int)
	equipment_parameter_2: _LP (bool)
	"""
	folder = 'Vessel'
	suffix = 'Vessel'
	equipment_parameter = '_Well Num'
	equipment_parameter_2 = '_LP'
	fisher800_template = 'VESSEL/Fisher 800/Sites/_Meta/Fisher 800 TIGA Core Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Separator Vessel'
	emerson107_template = 'VESSEL/Emerson107/Sites/_Meta/Emerson107 Core Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TIGA Core Vessel'

@equipment_adaptor
class PMEQ_VESSEL:
	"""
	equipment_parameter: _Double (int)
	equipment_parameter_2: _PMeq (int)
	"""
	folder = 'Vessel'
	suffix = 'Vessel'
	equipment_parameter = '_Double'
	equipment_parameter_2 = '_PMeq'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/EmersonFB3000 Core Vessel - PMeq'

@equipment_adaptor
class HEATER_VESSEL:
	"""
	equipment_parameter: _Heater Num (int)
	equipment_parameter_2: _PMeq (int)
	"""
	folder = 'Vessel'
	suffix = 'Vessel'
	equipment_parameter = '_Heater Num'
	equipment_parameter_2 = '_PMeq'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/EmersonFB3000 Core Heater Vessel'
	

@equipment_adaptor
class PIPELINE_VESSEL:
	"""
	equipment_parameter: _Vessel Adder (int)
    """
	folder = 'Vessel'
	suffix = 'Pipeline Vessel'
	equipment_parameter = '_Vessel Adder'
	fisher800_template = 'VESSEL/Fisher 800/Sites/_Meta/Fisher 800 Core Pipeline Vessel' 

@equipment_adaptor
class FWT_SEPARATOR_VESSEL:
	"""
	equipment_parameter: _e_Well Num (int)
	equipment_parameter_2: _e_LP (bool)
	"""
	folder = 'Vessel'
	suffix = 'FWT Separator Vessel'
	equipment_parameter = '_e_Well Num'
	equipment_parameter_2 = '_e_LP'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Separator Vessel'

@equipment_adaptor
class FWT_VRT_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure Safety High': [64, 1],
	    'Pressure Safety Low': [65, 1],
	    'Level Safety High': [11, 12],
	    'Pressure': [15, 10],
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_V2_VRT_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well V2 Vessel'
	tag_map = {
	    'Level Safety High': [11, 12],
	    'Pressure': [15, 10],
	}
	tag_parameters = {'_t_' + key: mergeDicts(PMEQ_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_BLANKET_GAS_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure': [15, 12],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}
	
@equipment_adaptor
class FWT_V2_BLANKET_GAS_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well V2 Vessel'
	tag_map = {'Pressure': [15, 12],
	}
	tag_parameters = {'_t_' + key: mergeDicts(PMEQ_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_CUSHION_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure Safety High': [56, 1],
	    'Pressure Safety Low': [57, 1],
	    'Level Safety High': [60, 1],
	    'Level Safety Low': [61, 1],
	    'Pressure': [15, 9],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_HEATER1_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Heater Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Heater Vessel'
	equipment_parameter = '_e_Vessel Number'
	tag_map = {'Pressure Safety High': [52, 1],
	    'Pressure Safety Low': [53, 1],
	    'Pressure': [15, 8],
	    'Temperature': [21, 4],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}
	
@equipment_adaptor
class FWT_HEATER2_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Heater Vessel'
	equipment_parameter = '_e_Vessel Number'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Heater Vessel'
	tag_map = {'Pressure Safety High': [54, 1],
	    'Pressure Safety Low': [55, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_LP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Level Safety High': [51, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

class FWT_V2_LP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well V2 Vessel'
	tag_map = {
		'Level Safety High': [12, 2],
	}
	tag_parameters = {'_t_' + key: mergeDicts(PMEQ_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_LP_ANNULUS_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure Safety High': [49, 1],
	    'Pressure Safety Low': [50, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_LP_SALES_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure Safety High': [45, 1],
	    'Pressure Safety Low': [46, 1],
		'Temperature Safety High': [47, 1],
	    'Temperature Safety Low': [47, 2],
		'Level Safety High': [48, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_V2_LP_SALES_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well V2 Vessel'
	tag_map = {
		'Pressure': [15, 4],
		'Temperature': [15, 5],
		'Level Safety High': [12, 3],
	}
	tag_parameters = {'_t_' + key: mergeDicts(PMEQ_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_HP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Level Safety High': [44, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

class FWT_V2_HP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well V2 Vessel'
	tag_map = {
		'Level Safety High': [12, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(PMEQ_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_HP_ANNULUS_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure Safety High': [42, 1],
	    'Pressure Safety Low': [43, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_HP_SALES_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure Safety High': [38, 1],
	    'Pressure Safety Low': [39, 1],
		'Temperature Safety High': [40, 1],
	    'Temperature Safety Low': [40, 2],
		'Level Safety High': [41, 1],
		'Pressure': [15, 6],
		'Temperature': [15, 7],
		
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_LP_GAS_SCRUBBER_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Pressure': [15, 2],
		    'Temperature': [15, 3],
		'Level Safety High': [12, 6],
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_DEHY_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Temperature': [15, 11],
		'Temperature Safety High': [72, 1],
		'Temperature Safety Low': [72, 2],
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}
	
@equipment_adaptor
class FWT_DEHY_2_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Temperature': [16, 4],
		'Temperature Safety Low': [72, 4],
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_FLARE_FUEL_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Level Safety High': [12, 8]
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_SCAV_DUMP_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Level Safety High': [12, 11]
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_SCAV_INLET1_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Level Safety High': [12, 12]
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class FWT_SCAV_INLET2_VESSEL:
	folder = 'Vessel'
	suffix = 'FWT Vessel'
	fb3000_template = 'VESSEL/EmersonFB3000/Sites/_Meta/FB3000 Five Well Vessel'
	tag_map = {'Level Safety High': [13, 1]
	}
	tag_parameters = {'_t_' + key: mergeDicts(MODIFIED_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

### TWT Vessel ###
VESSEL_BASE = '%d.%d.%d'
#VESSEL_AI_BASE = 'PMeqUsrDf_%d.DOUBLE_%d_VALUE:DOUBLE'
VESSEL_ALARM_BASE = '%d.%d.%d:UI1'
STOCK_VESSEL_PARAMETERS = {
'_t_High Setpoint': {'enable': ['High Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Low Setpoint': {'enable': ['Low Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Pressure': {'enable': ['Pressure'],
		'base': VESSEL_BASE,},
'_t_Temperature': {'enable': ['Temperature'],
		'base': VESSEL_BASE,},
'_t_Level Safety High': {'enable': ['Level Safety High', 'Level Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low': {'enable': ['Level Safety Low', 'Level Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety High Oil': {'enable': ['Level Safety High Oil', 'Level Safety High Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Oil': {'enable': ['Level Safety Low Oil', 'Level Safety Low Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Water': {'enable': ['Level Safety Low Water', 'Level Safety Low Water (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety High': {'enable': ['Pressure Safety High', 'Pressure Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety Low': {'enable': ['Pressure Safety Low', 'Pressure Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety High': {'enable': ['Temperature Safety High', 'Temperature Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety Low': {'enable': ['Temperature Safety Low', 'Temperature Safety Low (Message)'],
		'base': VESSEL_BASE,},
		}

VESSEL_ALARM_PARAMETERS = {
'_t_High Setpoint': {'enable': ['High Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Low Setpoint': {'enable': ['Low Setpoint'],
		 'base': VESSEL_BASE,},
'_t_Pressure': {'enable': ['Pressure'],
		'base': VESSEL_BASE,},
'_t_Temperature': {'enable': ['Temperature'],
		'base': VESSEL_BASE,},
'_t_Level Safety High': {'enable': ['Level Safety High', 'Level Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low': {'enable': ['Level Safety Low', 'Level Safety Low (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety High Oil': {'enable': ['Level Safety High Oil', 'Level Safety High Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Oil': {'enable': ['Level Safety Low Oil', 'Level Safety Low Oil (Message)'],
		'base': VESSEL_BASE,},
'_t_Level Safety Low Water': {'enable': ['Level Safety Low Water', 'Level Safety Low Water (Message)'],
		'base': VESSEL_BASE,},
'_t_Pressure Safety High': {'enable': ['Pressure Safety High', 'Pressure Safety High (Message)'],
		'base': VESSEL_ALARM_BASE,},
'_t_Pressure Safety Low': {'enable': ['Pressure Safety Low', 'Pressure Safety Low (Message)'],
		'base': VESSEL_ALARM_BASE,},
'_t_Temperature Safety High': {'enable': ['Temperature Safety High', 'Temperature Safety High (Message)'],
		'base': VESSEL_BASE,},
'_t_Temperature Safety Low': {'enable': ['Temperature Safety Low', 'Temperature Safety Low (Message)'],
		'base': VESSEL_BASE,},
		}

@equipment_adaptor
class TWT_SEPARATOR_VESSEL:
	"""
	equipment_parameter: _p_Meter Num (int)
	"""
	folder = 'Vessel'
	suffix = 'FWT Separator Vessel'
	equipment_parameter = '_p_Meter Num'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Separator Vessel'

@equipment_adaptor
class TWT_HP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Level Safety High': [9, 17, 8],
	'Pressure': [9, 17, 0],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TWT_LP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Level Safety High': [9, 17, 9],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TWT_HEATER_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Level Safety High': [9, 17, 12],
	'Pressure': [9, 17, 2],
	'Temperature': [9, 17, 19],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}	

@equipment_adaptor
class TWT_FUEL_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Level Safety High': [9, 17, 13],
	'Pressure': [9, 17, 3],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}	

@equipment_adaptor
class TWT_VRT_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Level Safety High': [9, 17, 14],
	'Pressure': [9, 17, 4],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}	


@equipment_adaptor
class TWT_TANK_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Pressure': [9, 17, 1],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}	
	
@equipment_adaptor
class TWT_VRU_SCRUBBER_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Level Safety High': [9, 17, 16],
	'Pressure': [9, 17, 17],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}	

@equipment_adaptor
class TWT_PIPELINE_VESSEL:
	folder = 'Vessel'
	suffix = 'TWT Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow TWT Vessel'
	tag_map = {'Pressure': [9, 17, 20],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

### Totalflow Mass Config ##
@equipment_adaptor
class TF_RMC_FACILITY_PIPELINE:
	folder = 'Facility'
	suffix = 'Facility Pipeline'
	totalflow_template = 'FACILITY/Totalflow/Sites/_Meta/TotalFlow RMC Facility Pipeline' 

@equipment_adaptor
class TF_RMC_FACILITY:
	folder = 'Facility'
	suffix = 'Facility'
	totalflow_template = 'FACILITY/Totalflow/Sites/_Meta/TotalFlow RMC Facility'

@equipment_adaptor
class TF_RMC_FLARE:
	folder = 'Flare'
	suffix = 'Flare'
	totalflow_template = 'FLARE/Totalflow/Sites/_Meta/TotalFlow RMC Flare' 

@equipment_adaptor
class TF_RMC_PUMP:
	"""
	equipment_parameter: _e_Pump Num (int)
	"""
	folder = 'Pump'
	suffix = 'Pump'
	equipment_parameter = '_e_Pump Num'
	totalflow_template = 'PUMP/Totalflow/Sites/_Meta/Totalflow RMC Pump' 	
	
@equipment_adaptor
class TF_RMC_FACILITY_HP_SEP_VESSEL:
	folder = 'Vessel'
	suffix = 'Facility Outlet HP Separator Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 7],
	'Pressure': [9, 0, 8],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}
	
@equipment_adaptor
class TF_RMC_HP_BULK_SEP_1_VESSEL:
	folder = 'Vessel'
	suffix = 'HP Bulk Separator 1 Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Pressure': [9, 0, 12],
	'Level Safety High': [9, 0, 13],
	'Level Safety Low': [9, 0, 14],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_HP_BULK_SEP_2_VESSEL:
	folder = 'Vessel'
	suffix = 'HP Bulk Separator 2 Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Pressure': [9, 0, 15],
	'Level Safety High': [9, 0, 16],
	'Level Safety Low': [9, 0, 17],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_LP_BULK_SEP_1_VESSEL:
	folder = 'Vessel'
	suffix = 'LP Bulk Separator 1 Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Separator Vessel' 
	tag_map = {'Pressure': [9, 0, 18],
	'Level Safety High': [9, 0, 19],
	'Level Safety Low': [9, 0, 20],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_LP_BULK_SEP_2_VESSEL:
	folder = 'Vessel'
	suffix = 'LP Bulk Separator 2 Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Separator Vessel' 
	tag_map = {'Pressure': [9, 0, 21],
	'Level Safety High': [9, 0, 22],
	'Level Safety Low': [9, 0, 23],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}
	
@equipment_adaptor
class TF_RMC_TEST_HEATER_VESSEL:
	folder = 'Vessel'
	suffix = 'Test Heater Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Pressure': [9, 0, 26],
	'Level Safety High': [9, 0, 25],
	'Temperature': [9, 0, 24],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_HP_SALES_VESSEL:
	folder = 'Vessel'
	suffix = 'HP Sales Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 37],
	'Pressure': [9, 0, 38],
	'Temperature': [9, 0, 39],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_LP_SALES_VESSEL:
	folder = 'Vessel'
	suffix = 'LP Sales Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 40],
	'Pressure': [9, 0, 41],
	'Temperature': [9, 0, 42],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_CUSHION_SCRUBBER_VESSEL:
	folder = 'Vessel'
	suffix = 'Cushion Scrubber Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 43],
	'Pressure': [9, 0, 44],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_LP_SUCTION_SCRUBBER_VESSEL:
	folder = 'Vessel'
	suffix = 'LP Suction Scrubber Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 45],
	'Pressure': [9, 0, 46],
	'Temperature': [9, 0, 47],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor 
class TF_RMC_COMPRESSOR_BLOWCASE_VESSEL:
	folder = 'Vessel'
	suffix = 'Compressor Blowcase Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 48],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_VRT_1_VESSEL:
	folder = 'Vessel'
	suffix = 'VRT 1 Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 69],
	'Pressure': [9, 0, 70],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_VRT_2_VESSEL:
	folder = 'Vessel'
	suffix = 'VRT 2 Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 71],
	'Pressure': [9, 0, 72],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_FLARE_FUEL_POT_VESSEL:
	folder = 'Vessel'
	suffix = 'Flare Fuel Pot Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 75],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_HP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'HP Flare KO Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 76],
	'Pressure': [9, 0, 77],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_LP_FLARE_VESSEL:
	folder = 'Vessel'
	suffix = 'LP Flare KO Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 78],
	'Pressure': [9, 0, 79],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_DEHY_VESSEL_1:
	folder = 'Vessel'
	suffix = 'Dehy Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Temperature': [9, 0, 35],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_DEHY_VESSEL_2:
	folder = 'Vessel'
	suffix = 'Dehy Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Temperature': [9, 0, 36],
	}
	tag_parameters = {'_t_' + key: mergeDicts(STOCK_VESSEL_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_SATELLITE_COOLER_FUEL_SKID_VESSEL:
	folder = 'Vessel'
	suffix = 'Satellite Cooler Fuel Skid Vessel'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Vessel' 
	tag_map = {'Level Safety High': [9, 0, 99],
	'Pressure': [9, 0, 100],
	'Pressure Safety High': [94, 122, 71],
	'Pressure Safety Low': [94, 122, 72],
	}
	tag_parameters = {'_t_' + key: mergeDicts(VESSEL_ALARM_PARAMETERS['_t_' + key], {'addresses': val}) for key, val in tag_map.items()}

@equipment_adaptor
class TF_RMC_HEATER_VESSEL:
	"""
	equipment_parameter: _p_Heater Num (int)
	"""
	folder = 'Vessel'
	suffix = 'Heater Vessel'
	equipment_parameter = '_p_Heater Num'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Heater Vessel'
	
@equipment_adaptor
class TF_RMC_COMPRESSOR:
	"""
	equipment_parameter: _e_Comp Num (int)
	"""
	folder = 'Compressor'
	suffix = 'Compressor'
	equipment_parameter = '_e_Comp Num'
	totalflow_template = 'COMPRESSOR/Totalflow/Sites/_Meta/Totalflow RMC Compressor'
	
@equipment_adaptor
class TF_RMC_VRU:
	"""
	equipment_parameter: _e_Comp Num (int)
	"""
	folder = 'Compressor'
	suffix = 'VRU'
	equipment_parameter = '_e_Comp Num'
	totalflow_template = 'COMPRESSOR/Totalflow/Sites/_Meta/Totalflow RMC VRU'

@equipment_adaptor
class TF_RMC_AIR_COMP:
	"""
	equipment_parameter: _e_Comp Num (int)
	"""
	folder = 'Compressor'
	suffix = 'Air Comp'
	equipment_parameter = '_e_Comp Num'
	totalflow_template = 'COMPRESSOR/Totalflow/Sites/_Meta/Totalflow RMC Air Compressor'

@equipment_adaptor
class TF_RMC_TANK:
	"""
	equipment_parameter: _e_Tank Num (int)
	equipment_parameter_2: _p_Water (0,1)
	"""
	folder = 'Tank'
	suffix = 'Tank'
	equipment_parameter = '_e_Tank Num'
	equipment_parameter_2 = '_p_Water'
	totalflow_template = 'TANK/Totalflow/Sites/_Meta/TotalFlow RMC Tank'

@equipment_adaptor
class TF_RMC_WELL:
	"""
	equipment_parameter: _e_Well Num (int)
	"""
	folder = 'Well'
	suffix = 'Well'
	equipment_parameter = '_e_Well Num'
	totalflow_template = 'WELL/Totalflow/Sites/_Meta/TotalFlow RMC Well'

@equipment_adaptor
class TF_RMC_VALVE:
	"""
	equipment_parameter: _e_Well Num (int)
	equipment_parameter_2: _p_Choke (0,1)
	equipment_parameter_3: _p_Pressure (0,1)
	"""
	folder = 'Valve'
	suffix = 'Valve'
	equipment_parameter = '_e_Well Num'
	equipment_parameter_2 = '_p_Choke'
	equipment_parameter_3 = '_p_Pressure'
	totalflow_template = 'VALVE/Totalflow/Sites/_Meta/Totalflow RMC Valve'

@equipment_adaptor
class TF_RMC_VESSEL:
	"""
	equipment_parameter: _e_Well Num (int)
	equipment_parameter_2: _p_LP (0,1)
	"""
	folder = 'Vessel'
	suffix = 'Vessel'
	equipment_parameter = '_e_Well Num'
	equipment_parameter_2 = '_p_LP'
	totalflow_template = 'VESSEL/Totalflow/Sites/_Meta/Totalflow RMC Separator Vessel'
	
@equipment_adaptor
class TF_RMC_GAS_METER:
	"""
	equipment_parameter: _e_AppConfig (int)
	"""
	folder = 'Meter'
	suffix = 'Gas Meter'
	equipment_parameter = '_e_AppConfig'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow RMC Gas Meter'

@equipment_adaptor
class TF_RMC_OIL_METER:
	"""
	equipment_parameter: _e_AppConfig (int)
	equipment_parameter_2: _e_Well Num (int)
	equipment_parameter_3: _p_Coriolis (int)
	"""
	folder = 'Meter'
	suffix = 'Oil Meter'
	equipment_parameter = '_e_AppConfig'
	equipment_parameter_2 = '_e_Well Num'
	equipment_parameter_3 = '_p_Coriolis'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow RMC Oil Meter'	

@equipment_adaptor
class TF_RMC_WATER_METER:
	"""
	equipment_parameter: _e_AppConfig (int)
	equipment_parameter_2: _e_Well Num (int)
	equipment_parameter_3: _p_Coriolis (int)
	"""
	folder = 'Meter'
	suffix = 'Water Meter'
	equipment_parameter = '_e_AppConfig'
	equipment_parameter_2 = '_e_Well Num'
	equipment_parameter_3 = '_p_Coriolis'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow RMC Water Meter'	

@equipment_adaptor
class TF_RMC_PUMP_METER:
	"""
	equipment_parameter: _p_Pump Meter Num (int)
	"""
	folder = 'Meter'
	suffix = 'Pump Meter'
	equipment_parameter = '_p_Pump Meter Num'
	totalflow_template = 'METER/TotalFlow G4XFC/Sites/_Meta/TotalFlow RMC Pump Meter'	
	
### Well ###
@equipment_adaptor
class WELL:
	"""
	equipment_parameter: _Well Num (int)
	"""
	folder = 'Well'
	suffix = ''
	equipment_parameter = '_Well Num'
	fb3000_template = 'WELL/EmersonFB3000/Sites/_Meta/EmersonFB3000 TIGA Core Well'
	wellpilot_template = 'WELL/WELLPILOTRPOC/Sites/_Meta/WellPilot TIGA Core Well' 
	exs1000_template = 'WELL/EProdEXS1000/Sites/_Meta/EprodEXS1000 Core Well'
	totalflow_template = 'WELL/TotalFlow G4XFC/Sites/_Meta/TotalFlow TIGA Core Well'
	emerson107_template = 'WELL/Emerson107/Sites/_Meta/Emerson107 Core Well'
	modbus_template = 'WELL/Modbus Click/Sites/_Meta/Modbus TIGA Core Well'
	totalflow_template = 'WELL/Totalflow/Sites/_Meta/Totalflow Core Well'
	scadapack_template = 'WELL/RealFloPPlus/Sites/_Meta/RealFloPPLUS Core Well'
	smarten_template = 'WELL/Smarten/Sites/_Meta/Smarten Core Well'
	
@equipment_adaptor
class FWT_WELL:
	"""
	equipment_parameter: _e_Well Num (int)
	"""
	folder = 'Well'
	suffix = 'FWT Well'
	equipment_parameter = '_e_Well Num'
	fb3000_template = 'WELL/EmersonFB3000/Sites/_Meta/EmersonFB3000 Five Well'

@equipment_adaptor
class TWT_WELL:
	"""
	equipment_parameter: _Well Num (int)
	"""
	folder = 'Well'
	suffix = 'TWT Well'
	equipment_parameter = '_Well Num'
	totalflow_template = 'WELL/Totalflow/Sites/_Meta/TotalFlow TWT Well'
	
### James Croft Template ###
@equipment_adaptor
class PTW_WELL:
	"""
	James Croft Template
	equipment_parameter: _Well Num (int)
	"""
	folder = 'Well'
	suffix = 'PTW Well'
	equipment_parameter = '_Well Num'
	fb3000_template = 'WELL/EmersonFB3000/Sites/_Meta/EmersonFB3000 Plunger Transition Well'
	
###### SiteBuilder Configs ######
### Meter ###
METER_CONFIG = {
'Sales NGL': [NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 1],
'Cushion NGL': [NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 2],
'Suction NGL': [NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 3],
'Bulk NGL': [NGL_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, 4],
}
TANK_CONFIG = {}
for num in range(6):
	TANK_CONFIG['Oil Tank ' + str(num+1)] = [TANK, {'type': 'Tank', 'subtype': 'Oil Tank', 'merrickid':0}, num+1, 0] 
	TANK_CONFIG['Water Tank ' + str(num+1)] = [TANK, {'type': 'Tank', 'subtype': 'Water Tank', 'merrickid':0}, num+1, 1]

POC_CONFIG = {'POC': [POC, {'type': 'POC', 'subtype': 'POC', 'merrickid': 0}]}


def well_build(well_num, site_dict, dpmeter_dict):
	
	config_dict = {
	'LP': [WELL_DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, well_num, 1],
	'Wellhead': [WELL_DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, well_num, 1],
	'HP': [WELL_DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Wellhead Meter', 'merrickid': 0}, well_num, 0],
	'Injection': [DPMETER, {'type': 'Gas Meter', 'subtype': 'Gas Lift Meter', 'merrickid': 0}, dpmeter_dict['injection_' + str(well_num)] if 'Injection' in site_dict['well_'+str(well_num)]['equip'] else 0, {'_Gas Lift': 1,}],
	'Oil Coriolis': [WELL_CORIOLIS_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Coriolis Meter', 'merrickid': 0}, well_num, 0],
	'Water Coriolis': [WELL_CORIOLIS_METER, {'type': 'Liquid Meter', 'subtype': 'Water Coriolis Meter', 'merrickid': 0}, well_num, 1],
	'Oil Turbine': [WELL_TURBINE_METER, {'type': 'Liquid Meter', 'subtype': 'Oil Turbine Meter', 'merrickid': 0}, well_num, 0],
	'Water Turbine': [WELL_TURBINE_METER, {'type': 'Liquid Meter', 'subtype': 'Water Turbine Meter', 'merrickid': 0}, well_num, 1],
	'LP Separator': [WELL_VESSEL, {'type': 'Vessel', 'subtype': 'Separator Vessel', 'merrickid': 0}, well_num, 1],
	'HP Separator': [WELL_VESSEL, {'type': 'Vessel', 'subtype': 'Separator Vessel', 'merrickid': 0}, well_num, 0],
	'Injection Valve': [WELL_VALVE, {'type': 'Control Valve', 'subtype': 'Control Valve', 'merrickid': 0}, well_num, 0],
	'Choke Valve': [WELL_VALVE, {'type': 'Control Valve', 'subtype': 'Choke Valve', 'merrickid': 0}, well_num, 1],
	}
	return config_dict
