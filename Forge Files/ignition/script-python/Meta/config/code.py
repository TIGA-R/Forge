from system.db import runNamedQuery
from collections import OrderedDict
subtype_dict = {
    'Comms':           ['Remote Device',],
    'Plunger':         ['Plunger',],
    'Gas Compressor':  ['Gas Compressor', 'VRU Compressor'],
    'Flare':           ['Flare', 'Combustor'],
    'Facility':        ['Facility','Facility Well Alarms', 'Facility Pipeline','River Data'],
    'Liquid Meter':    ['Fluid Turbine Meter', 'Oil Coriolis Meter', 'Oil Turbine Meter', 'Oil Vortex Meter', 
                        'SWD Meter', 'Water Coriolis Meter', 'Water Turbine Meter', 'Water Vortex Meter'],
    'Well':            ['Well',],
    'Control Valve':   ['Gas Lift Control Valve', 'Choke Valve', 'Bypass Valve', 'Pressure Control Valve',],
    'Tank':            ['Oil Tank', 'Water Tank', 'Expansion Tank', 'Chemical Tank', 'Bullet Tank', 'Gun Barrel Tank',],
    'Pump':            ['Chemical Pump', 'Chemical Pump Controller', 'SWD', 'Transfer Pump', 'HPump', 'Pump Run Time',],
    'Gas Meter':       ['Gas Lift Meter', 'Gas Wellhead Meter', 'Fuel Meter', 'Check Meter', 
                        'Gas Bulk Meter', 'VRU Meter', 'Blower Meter', 'Sales Meter', 'Cushion Meter', 'NGL Meter',
                        'Thermal Mass Meter', 'Buyback Meter', 'Flare Meter', 'Gas Test Meter','Comp Meter', 'JT Meter',],
    'Rollup':          ['Rollup',],
    'Frac Water Well': ['Frac Water Well',],
    'Air Compressor':  ['Air Compressor',],
    'LACT Meter':      ['LACT Unit',],
    'Vessel':          ['Fuel Vessel', 'Heater Treater Vessel', 'Separator Vessel', 'Tank Vessel', 
                        'Vessel', 'Vessel Pipeline', 'Scrubber Vessel'],
    'POC':             ['POC',],
    'ESP':             ['ESP',],
}

type_field_dict = {     
    'Comms':          {
                       'wellid':          'Optional',
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },
    'Plunger':        {
                       'wellid':          True,
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },
    'Gas Compressor': {
                       'wellid':          'Optional',
                       'enumeration':     True,
                       'merrickid':       True,
                       'scadaid':         True,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },
    'Flare':          {
                       'wellid':          'Optional',
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },
    'Facility':       {
                       'wellid':          False,
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },  
    'Liquid Meter':   {
                       'wellid':          'Optional',
                       'enumeration':     True,
                       'merrickid':       True,
                       'scadaid':         True,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  True,    
                    },                 
    'Well':           {
                       'wellid':          True,
                       'enumeration':     False,
                       'merrickid':       True,
                       'scadaid':         True,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  True,    
                    },   
    'Control Valve':  {
                       'wellid':          'Optional',
                       'enumeration':     True,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },   
    'Tank':           {
                       'wellid':          'Optional',
                       'enumeration':     True,
                       'merrickid':       True,
                       'scadaid':         True,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': True,
                       'procountexport':  True, 
                       'fluidtransport':  True,
                       'hauler':          True,   
                    },      
    'Pump':           {
                       'wellid':          'Optional',
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },    
    'Gas Meter':      {
                       'wellid':          'Optional',
                       'enumeration':     True,
                       'merrickid':       True,
                       'scadaid':         True,
                       'thirdpartyxref':  True,
                       'thirdpartygroup': True,
                       'procountexport':  True,    
                    },  
    'Rollup':         {
                       'wellid':          False,
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },    
    'Frac Water Well':  {
                       'wellid':          'Optional',
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  True,    
                    },  
    'Air Compressor':   {
                       'wellid':          'Optional',
                       'enumeration':     True,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },  
    'LACT Meter':     {
                       'wellid':          False,
                       'enumeration':     True,
                       'merrickid':       True,
                       'scadaid':         True,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  True,    
                    },    
    'Vessel':         {
                       'wellid':          'Optional',
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },     
    'POC':            {
                       'wellid':          'Optional',
                       'enumeration':     False,
                       'merrickid':       False,
                       'scadaid':         False,
                       'thirdpartyxref':  False,
                       'thirdpartygroup': False,
                       'procountexport':  False,    
                    },    
}




FOREMAN_SCRIPT = {
    'North': [
        'JEROMIE WELLS',
        'BRIAN TRACY',
        'BRENT MICHALAK',
        'RICK HARP',
        'RYAN HARRINGTON',
    ],
    'South': [
        'JEREMY NEWMAN',
    ],

}

from system.dataset import toPyDataSet
FOREMAN = {}
ROUTE = {}
for area in toPyDataSet(runNamedQuery('Navigation/Well Dropdown/Area')):
	FOREMAN[str(area[0])] = lambda x: runNamedQuery('Navigation/Overview Dropdown/Get Foreman',{  
	        'site': '%',  
	        'facilityID': '%',  
	        'area': x,  
	        'route': '%',  
	        })
	ROUTE[str(area[0])] = lambda x: runNamedQuery('Navigation/Overview Dropdown/Get Route',{  
	        'site': '%',  
	        'facilityID': '%',  
	        'area': x,  
	        'foreman': '%',  
	        })

#FOREMAN = {  
#    'North': runNamedQuery('Navigation/Overview Dropdown/Get Foreman',{  
#        'site': '%',  
#        'facilityID': '%',  
#        'area': 'North',  
#        'route': '%',  
#        }),  
#    'South': runNamedQuery('Navigation/Overview Dropdown/Get Foreman',{  
#        'site': '%',  
#        'facilityID': '%',  
#        'area': 'South',  
#        'route': '%',  
#        }),  
#    }

ROUTE_SCRIPT = {
    'North': [
        '14A',
        '14B',
        '14C',
        '14D',
        '14E',
        '14F',
        '14G',
        '14H',
        '14L',
        '14O',
        '14P',
        '14Q',
        '14R',
        '14S',
        '14W',
        '15-RAM',
        '15A',
        '15B',
        '15F',
        '15J',
        '15N',
        '15R',
        '15S',
        '15T',
        '15U',
        '15W',
        '21C',
        '22B',
        '22D',
        '22E',
        '22F',
        '22H',
        '22I',
        '22N',
        '22P',
        '22R',
        '22S',
        '22W',
        'Daylight',
        '23M',
    ],
    'South': [
        'Gillett Route 1',
        'Gillett Route 2',
        'Gillett Route 3',
        'Gillett Route 4',
        'Gillett Route 5',
    ],
    'Lime Rock': ['Lime Rock'],
}

#ROUTE = {  
#    'North': runNamedQuery('Navigation/Overview Dropdown/Get Route',{  
#        'site': '%',  
#        'facilityID': '%',  
#        'area': 'North',  
#        'foreman': '%',  
#        }),  
#    'South': runNamedQuery('Navigation/Overview Dropdown/Get Route',{  
#        'site': '%',  
#        'facilityID': '%',  
#        'area': 'South',  
#        'foreman': '%',  
#        }),  
#    }
    
METADATA_ALLOWED_ROLES = ['app_ignition_foremen_p', 'adm_ignition_p', 'app_ignition_autotechs_p']
    
FACILITY_FRONT_TO_BACK = {
	'Name': 'sql_name',
	'Route': 'route',
	'Foreman': 'foreman',
	'Enabled': 'enabled',
	'Procount Midnight': 'procount_midnight',
	'Latitude': 'latitude',
	'Longitude': 'longitude',
	'Merrick ID': 'merrickid',
}

FACILITY_FRONT_CONFIG = {
	'Name': str,
	'Route': ROUTE,
	'Foreman': FOREMAN,
	'Enabled': bool,
	'Procount Midnight': bool,
	'Latitude': float,
	'Longitude': float,
	'Merrick ID': int,
}

FACILITY_CONTEXT = {
	'Route': 'Area',
	'Foreman': 'Area',
}


EQUIPMENT_FRONT_TO_BACK = {
	'Name': 'sql_name',
	'Type': 'sql_type',
	'SubType': 'subtype',
	'SCADA ID': 'scada_id',
	'Merrick ID': 'merrick_id',
#	'Enumeration': 'enumeration',
	'Enabled': 'enabled',
	'Procount Export': 'procount_export',
	'Sequence': 'sequence',
	'Created Datetime': 'created_datetime',
	'Pad': 'pad_id',
	'Well': 'well',
	'3rd Party XRef': 'third_party_xref',
	'3rd Party Group': 'third_party_group',
	'ProCount Midnight': 'procount_midnight',
	'Tag Path': 'tag_path_full',
	'Fluid Transport': 'fluid_transport',
}

TYPES = runNamedQuery('Overview/EquipmentSummary/EquipmentType')
from system.dataset import toPyDataSet
SUBTYPES = {}
for equip_type in toPyDataSet(TYPES):
	SUBTYPES[str(equip_type[0])] = lambda x: runNamedQuery('Meta/Equipment/Get/Subtype by Type', {'type': x})

PADS = runNamedQuery('Meta/Site/Get/All Pad IDs')
WELLS = {}
for pad_id in toPyDataSet(PADS):
	WELLS[pad_id[0]] = lambda x: runNamedQuery('Meta/Well/Get/By Facility', {'siteID': Meta.Site.Pad(x).facility_id})

fluid_transport_dataset = system.db.runNamedQuery('Meta/Equipment/Get/Fluid Transports')
#FLUID_TRANSPORT = {fluid_transport_dataset.getValueAt(i, 0): fluid_transport_dataset.getValueAt(i, 1) for i in range(fluid_transport_dataset.getRowCount())}

EQUIPMENT_FRONT_CONFIG = {
	'Name': str,
#	'Type': None,
	'SubType': SUBTYPES,
	'SCADA ID': str,
	'Merrick ID': int,
#	'Enumeration': int,
	'Enabled': bool,
	'Procount Export': bool,
	'Sequence': int,
	'Created Datetime': None,
	'Tag Path': None,
	'Well': WELLS,
	'3rd Party XRef': str,
	'3rd Party Group': str, 
	'ProCount Midnight': bool,
	'Fluid Transport': fluid_transport_dataset,
}

EQUIPMENT_CONTEXT = {
	'SubType': 'Type',
	'Well': 'Pad',
}
