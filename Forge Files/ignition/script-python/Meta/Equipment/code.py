from Meta.Meta import Meta
from Meta.PYDS import PYDS
from Meta.Site import Pad, Facility
from system.tag import writeBlocking as tag_write, rename
from system.db import runNamedQuery
from Meta.Well import Well
from Meta.config import subtype_dict, type_field_dict

class Equipment(Meta):
    table_name = 'meta_equipment'
    meta_type = 'equipment'

    def __init__(self, identifier):
        self.identifier = identifier
        self.get_name_and_id(self.identifier)

    def well_name_list(self):
        well_name_ds = runNamedQuery('Meta/Equipment/Get Wells', {'siteID': self.site_id})
        well_name_list = PYDS(dataset=well_name_ds).ds2py()['name']
        return well_name_list
        
    def rename_reset_history(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('new_name must be of type str')
        old_tag_path = self.tag_path_full
        # Rename Tag
        rename(old_tag_path, new_name)
        new_tag_path_list = old_tag_path.split('/')[:-1] 
        new_tag_path_list.append(new_name)
        self.new_tag_path = "/".join(new_tag_path_list)
        # Rename tag path in SQL
        self.update_sql_field('tagPathFull', self.new_tag_path)
        # Rename tag name in SQL
        self.update_sql_field('name', new_name)
        self.name = new_name
	
	# Renames metadata only
    def rename_keep_history(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('new_name must be of type str')
        # Rename name in SQL
        self.update_sql_field('name', new_name)
        self.name = new_name
    
    def rename_migrate_history(self, new_name):
    	self.rename_reset_history(new_name)
    	
    	print(query)
    
    def move_migrate_history(self, new_folder):
    	pass
    
    def take_legacy_history(self, legacy_tagpath):
    	pass
                            
    @property 
    def site_id(self):
        return self.get_sql_field('siteID')

    @property
    def tag_path(self):
        return self.get_sql_field('tagPathFull')
    
    @tag_path.setter
    def tag_path(self, value):
    	return self.update_sql_field('tagPathFull', value)

    @property
    def well_id(self):
        # Look up SQL table well ID
        well_id = self.get_sql_field('wellID')
        # If well id is 0, look for well name in equipment name
        ### Bugged out on Ozark well. Need to review before reimplementing###
    #        if well_id == 0:
    #            for well in self.well_name_list():
    #                # If well name is in the equipment name, update the well ID to match the well well-ID
    #                if well in self.name:
    #                    self.update_sql_field('wellID', Equipment(well).well_id)
    #                    # Re-query the table to return the new well ID
    #                    well_id = self.get_sql_field('wellID')
        return well_id

    @well_id.setter
    def well_id(self, value):
        # well set to tag path/name
        if isinstance(value, str):
            self.update_sql_field('wellID', Equipment(value).well_id)
        # well set to id number
        else:
            self.update_sql_field('wellID', value)

    @property
    def site(self):
        return Pad(self.site_id)

    @property
    def scada_id(self):
        return self.get_sql_field('scadaID')

    @scada_id.setter
    def scada_id(self,value):
        if self.sql_type == 'Well':
            if self.well_id:
                Well(self.well_id).scada_id = str(value)
        self.update_sql_field('scadaID', str(value))

    @property
    def merrick_id(self):            
        return self.get_sql_field('merrickID')

    @merrick_id.setter
    def merrick_id(self, value):
        if self.sql_type == 'Well':
            if self.well_id:
                Well(self.well_id).merrick_id = str(value)
        self.update_sql_field('merrickID', str(value))

    @property
    def enabled(self):
        return self.get_sql_field('enabled')

    @enabled.setter
    def enabled(self, value):
        if value in [0,1]:
            self.update_sql_field('enabled', value)
            print(self.tag_path)
            tag_write([self.tag_path+'.enabled'], [value])
            if self.merrick_id:
            	self.procount_export = value
        else:
            raise ValueError('Must enter 0 or 1')

    @property
    def enumeration(self):
        return self.get_sql_field('enumeration')

    @enumeration.setter
    def enumeration(self, value):
        self.update_sql_field('enumeration', int(value))   

    @property
    def sequence(self):
        return self.get_sql_field('sequence')

    @sequence.setter
    def sequence(self, value):
        self.update_sql_field('sequence', int(value))  
   
    @property
    def tag_path_full(self):
        return self.get_sql_field('tagPathFull')

    @tag_path_full.setter
    def tag_path_full(self, value):
        self.update_sql_field('tagPathFull', value)
    
    @property
    def procount_export(self):
        return self.get_sql_field('proCountExport')

    @procount_export.setter
    def procount_export(self, value):
        self.update_sql_field('proCountExport', value)
            
    @property
    def subtype(self):
        return self.get_sql_field('subtype')

    @subtype.setter
    def subtype(self, value):
        self.update_sql_field('subtype', value)
    
    @property
    def pad_id(self):
    	return self.get_sql_field('siteID')
    
    @property
    def facility_id(self):
    	return Pad(self.pad_id).facility_id
    
    @property
    def well_id(self):
    	return self.get_sql_field('wellID')
    
    @well_id.setter
    def well_id(self, value):
    	self.update_sql_field('wellID', value)
    
    @property
    def well(self):
    	return Well(self.well_id).sql_name
    
    @well.setter
    def well(self, value):
    	self.well_id = Well(value).sql_id
    
    @property
    def third_party_xref(self):
    	return self.get_sql_field('thirdPartyXref')
    
    @third_party_xref.setter
    def third_party_xref(self, value):
    	self.update_sql_field('thirdPartyXref', value)
    
    @property
    def third_party_group(self):
    	return self.get_sql_field('thirdPartyGroup')
    	
    @third_party_group.setter
    def third_party_group(self, value):
    	self.update_sql_field('thirdPartyGroup', value)
    
    @property
    def procount_midnight(self):
        return self.get_sql_field('ProCountMidnight')

    @procount_midnight.setter
    def procount_midnight(self, value):
        self.update_sql_field('ProCountMidnight', value)
    
    @property
    def fluid_transport(self):
        return system.db.runNamedQuery('Meta/Equipment/Get/Fluid Transport', parameters={'id': self.sql_id})

    @fluid_transport.setter
    def fluid_transport(self, value):
        system.db.runNamedQuery('Meta/Equipment/Update/Fluid Transport', parameters={'id': self.sql_id, 'transportType': value})
    
    @property
    def tag_path_full(self):
        return self.get_sql_field('tagPathFull')
    
    @classmethod
    def add_equipment_from_tagpath(cls, tagpath, equip_type=None, subtype=None,
                                    pad_identifier=None,
                                    well_identifier=None,
                                    enabled=True,
#                                    enumeration=None,
                                    scada_id=None,
                                    merrick_id=None,
                                    third_party_xref=None,
                                    third_party_group=None,
                                    fluid_transport = None,
                                    primary_hauler = None,
                                    procount_export=None):
        if system.db.runNamedQuery('Meta/Equipment/Exists', {'tagPathFull': tagpath}):
        	device = system.tag.readBlocking([tagpath + '/Parameters.Device01'])[0].value
	    	messageHandler = 'Meta.Equipment.updateDevice'
	    	system.util.sendMessage('Magnolia', messageHandler, payload={'device': device, 'siteid': cls(tagpath).site_id, 'id': cls(tagpath).sql_id})
        	return cls(tagpath)
        
        from system.gui import inputBox
        equipment_name = tagpath.split('/')[-1]
        facility_identifier = tagpath.split('/')[-4]
        def equip_input_box(prompt):
        	header = '%s:\n'%equipment_name
        	return inputBox(header+prompt)
        # Type Retrieval
        print equip_type
        if equip_type not in subtype_dict.keys():
            type_list_str = 'Select a type from the following: '
            num = 1
            for type_key in subtype_dict.keys():
                type_list_str += '\n(%s) - %s'%(num,type_key)
                num += 1
            equip_type = subtype_dict.keys()[int(equip_input_box(type_list_str))-1]
            if equip_type not in subtype_dict:
                raise('%s type not found as a valid type'%equip_type)
        
        # Subtype Retrieval
        sub_type = subtype
        subtype_list = subtype_dict[equip_type]
        if sub_type not in subtype_list:
	        if len(subtype_list) == 1:
	            sub_type = subtype_list[0]
	        else:
	            dialog_string = 'Select a subtype number from the following: '
	            num = 1
	            for subtype in subtype_list:
	                dialog_string += '\n(%s) - %s'%(num, subtype)
	                num += 1
	            selection_num = int(equip_input_box(dialog_string)) - 1
	            sub_type = subtype_list[selection_num]
        print(tagpath)
        # Pad ID Retrieval
        if pad_identifier is None:
            pad_identifier = tagpath.split('/')[-3]
        pad_id = Pad(pad_identifier).sql_id
        if pad_id is None:
            pad_identifier = equip_input_box('Could not determine pad from tagpath. Enter pad name or ID:')
            pad_id = Pad(pad_identifier).sql_id
            if pad_id is None:
                raise('Failed to determine pad ID')
                
        #Special Case: Add Well
        if equip_type == "Well":
        	well_check = Well(equipment_name).sql_id
        	print well_check
        	if (well_check is None) or int(Well(well_check).site_id) != int(Pad(pad_id).facility_id):
        		add_or_not = int(equip_input_box('Well name was not found in meta_well. Would you like to create a new well record?\n(1) - Yes\n(2) - No'))
        		if add_or_not == 1:
        			new_well = Well.add_well(Facility(facility_identifier).sql_id, equipment_name, merrick_id=merrick_id, scada_id=scada_id)
        			well_identifier = new_well.sql_id
				if well_identifier and (not merrick_id) and (not scada_id):
					well_mid = Well(well_identifier).merrick_id
					if well_mid:
						merrick_id = well_mid
						scada_id = str(well_mid)
        
        # Well ID Retrieval
        if type_field_dict[equip_type]['wellid']:
            if well_identifier is None:
                facility_id = Facility(facility_identifier).sql_id
                well_list = Well.well_list(facility_id)
                if len(well_list) > 0:
                    select_string = 'Select a well: '
                    num = 1
                    for well in well_list:
                        select_string += '\n(%s) - "%s"'%(num, well)
                        num += 1
                    if type_field_dict[equip_type]['wellid'] == 'Optional':
                        select_string += '\n(0) - No Well'
                    well_num = equip_input_box(select_string)
                    well_num = int(well_num)
                    if well_num == 0:
                    	well_id = 0
                    else:
                    	well_id = Well(well_list[well_num-1]).sql_id
                else:
                    well_identifier = equip_input_box('Enter a well identifier (name or id)')
                    try:
                        well_identifier = int(well_identifier)
                        well_id = Well(well_identifier).sql_id
                    except:
                        well_id = Well(well_identifier).sql_id
            else:
                well_id = Well(well_identifier).sql_id
            if well_id is None:
                if type_field_dict[equip_type]['wellid'] == 'Optional':
                    well_id = 0
                else:
                    raise('Could not find well ID from identifier')
        else:
            well_id = 0
        
        if type_field_dict[equip_type]['merrickid'] and merrick_id is None:
            merrick_id = equip_input_box('Enter a merrick ID value')

        if type_field_dict[equip_type]['scadaid'] and scada_id is None:
            scada_id = equip_input_box('Enter a scada ID value')
        
        if type_field_dict[equip_type]['thirdpartyxref'] and third_party_xref is None:
            third_party_xref = equip_input_box('Enter a third party XRef value')

        if type_field_dict[equip_type]['thirdpartygroup'] and third_party_group is None:
            third_party_group = equip_input_box('Enter a third party group value')
        
        if type_field_dict[equip_type]['procountexport'] and procount_export is None:
            procount_export = int(equip_input_box('Procount Export? (1 or 0)'))
        else:
            procount_export = False
        if type_field_dict[equip_type].get('fluidtransport') and fluid_transport is None:
        	process_function_query = system.db.runQuery("""
        	select id, propertyName from metadata01.dbo.tbl_meta_properties
        	where propertytype='Fluid Transport'
        	""")
        	prompt =  '\n'.join('%s: %s'%(i[0], i[1]) for i in process_function_query)
        	fluid_transport = int(equip_input_box(prompt))
        
        if type_field_dict[equip_type].get('hauler') and primary_hauler is None \
        and fluid_transport == 2:
        	hauler_query = system.db.runQuery("""
        	SELECT distinct hauler FROM metadata01.dbo.meta_hauler_xref
        	""")
        	hauler_list = [[idx, name[0]] for idx, name in enumerate(hauler_query)]
        	hauler_dict = {idx: name[0] for idx, name in enumerate(hauler_query)}
        	prompt = '\n'.join('%s: %s'%(i[0], i[1]) for i in hauler_list)
        	primary_hauler = hauler_dict[int(equip_input_box(prompt))]
        else:
        	primary_hauler = None
        
        if ' LP ' in equipment_name:
        	process_function = 'LP'
        elif ' HP ' in equipment_name:
        	process_function = 'HP'
        else:
        	process_function = ''

        parameters = {
            'padID': pad_id,
            'wellID': well_id,
            'enabled': enabled,
            'equipmentName': equipment_name,
            'type': equip_type,
            'subType': sub_type,
            'enumeration': 0,
            'tagPathFull': tagpath,
            'merrickID': merrick_id,
            'scadaID': scada_id,
            'thirdPartyXref': third_party_xref,
            'thirdPartyGroup': third_party_group,
            'proCountExport': procount_export,
            'processFunction': process_function,
            'hauler': primary_hauler,
            'fluidTransport': fluid_transport,
            'procountMidnight': 1,
        }
        runNamedQuery('Meta/Equipment/Add/Equipment', parameters)
        if primary_hauler is not None:
        	parameters = {
        		'hauler': primary_hauler,
        		'equipId': cls(tagpath).sql_id,
        	}
        	runNamedQuery('Meta/Equipment/Add/Hauler', parameters)
        print('%s added successfully'%equipment_name)
        if equip_type == 'Comms':
        	system.db.runNamedQuery('Meta/Export/Insert/Build RD Record', {'equipId': cls(tagpath).sql_id, 'facilityId': pad_id, 'acmId': system.db.runScalarQuery("select objectid from ACM_DEVICE_VIEW where devicename='%s'"%equipment_name)})
        	device = equipment_name
        else:
        	device = system.tag.readBlocking([tagpath + '/Parameters.Device01'])[0].value
    	messageHandler = 'Meta.Equipment.updateDevice'
    	system.util.sendMessage('Magnolia', messageHandler, payload={'device': device, 'siteid': cls(tagpath).site_id, 'id': cls(tagpath).sql_id})
    	system.util.sendMessage('Magnolia', 'Meta.Equipment.updateRoute', payload={'tagpath': tagpath})
        if not enabled:
        	cls(tagpath).enabled = 0
        return cls(tagpath)
        

def get_all_tags_by_type(equip_type):
	return system.dataset.toPyDataSet(runNamedQuery('Meta/Equipment/Get/Tags/By Type', {'type': equip_type})).getColumnAsList(0)