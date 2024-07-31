from system.db import runNamedQuery
from system.tag import write as tag_write, rename

class Meta(object):
	
    def get_name_and_id(self, identifier):
        # Type int identifier assumed to be sql_id
        try:
        	identifier = int(identifier)
        except:
        	pass
        if isinstance(identifier, int):
            self.sql_id = identifier
            if self.sql_id == 0:
            	self.name = ''
            else:
            	self.name = self.get_sql_field('name')
            if self.name is None:
#                raise ValueError('Could not find id in database table %s'%self.table_name)
				self.sql_id = None
        # Type str identifier assumed to be tag or tag path
        elif isinstance(identifier, str) or isinstance(identifier, unicode):
            self.name = identifier
            # Assume string is a tag path if '/' found in string
            if '/' in self.name:
                if self.meta_type == 'equipment':
                    self.sql_id = runNamedQuery('Meta/Equipment/Get/Tag Path', {'tagPath': self.name, 'field': 'id'})
                    self.name = runNamedQuery('Meta/Equipment/Get/Tag Path', {'tagPath': self.name, 'field': 'name'})
                elif self.meta_type in ['facility', 'pad']:
                    self.name = self.name.split('/')[-1]
                    self.sql_id = runNamedQuery('Meta/Site/Get/Name', {'name': self.name, 'field': 'id', 'siteType': self.meta_type})
                    if self.sql_id is None:
                        raise('Could not find %s with name: %s in table %s'%(self.meta_type, self.name, self.table_name))
                else:
                    self.name = self.name.split('/')[-1]
                    self.sql_id = self.get_sql_field('id', name=self.name)
            # Assume string is a unique tag name otherwise
            else:
                if self.meta_type in ['facility', 'pad']:
            	    self.sql_id = runNamedQuery('Meta/Site/Get/Name', {'name': self.name, 'field': 'id', 'siteType': self.meta_type})
            	else:
	                self.sql_id = self.get_sql_field('id', name=self.name)
	                if self.meta_type == 'equipment' and self.sql_id is None:
	                    self.sql_id = runNamedQuery('Meta/Equipment/Get/Tag Name', {'tagPath': self.name, 'field': 'id'})
	                    self.name = runNamedQuery('Meta/Equipment/Get/Tag Name', {'tagPath': self.name, 'field': 'name'})
#            if self.sql_id is None:
#                raise ValueError('Could not find name: %s in database table %s'%(self.name, self.table_name))
    	elif identifier is None:
    		self.sql_id = 0
    		self.name = None
        else:
            raise TypeError('identifier must be of type string or int, received type %s'%type(identifier))

    def get_sql_field(self, field, name=None):
        if name is None:
            return runNamedQuery('Meta/Meta/Get/ID', {'id': self.sql_id, 'field': field, 'tableName': self.table_name})
        else:
            return runNamedQuery('Meta/Meta/Get/Name', {'name': self.name, 'field': field, 'tableName': self.table_name})
    
    def update_sql_field(self, field, value):
        if isinstance(value, int):
            return runNamedQuery('Meta/Meta/Update/Int', {'id': self.sql_id, 'tableName': self.table_name, 'field': field, 'fieldValue': value})
        elif isinstance(value, str) or isinstance(value, unicode):
            return runNamedQuery('Meta/Meta/Update/String', {'id': self.sql_id, 'tableName': self.table_name, 'field': field, 'fieldValue': value})
        elif isinstance(value, float):
            return runNamedQuery('Meta/Meta/Update/Float', {'id': self.sql_id, 'tableName': self.table_name, 'field': field, 'fieldValue': value})
#		elif isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
#		   	return runNamedQuery('Meta/Meta/Update/Datetime', {'id': self.sql_id, 'tableName': self.table_name, 'field': field, 'fieldValue': value})
        else:
            raise TypeError('Type %s is not supported to update sql field'%type(value))
	
    @property
    def sql_id(self):
        if not self.rename:
            # Add project name when relocating to gateway
            # Resolves to None if does-not-exist (null)
            return self.get_sql_field('id')
        else:
            return self._sql_id
        

    @property
    def sql_type(self):
        return self.get_sql_field('type')
    
    @sql_type.setter
    def sql_type(self, value):
        self.update_sql_field('sql_type', value)
    
    @property
    def sql_name(self):
        return self.get_sql_field('name')
    
    @sql_name.setter
    def sql_name(self, value):
    	header = "%s update %s -> %s"%(self.meta_type, self.sql_name, value)
    	body = "%s: %s has been updated to new name: %s"%(self.meta_type, self.sql_name, value)
    	recipients = ["glatimer@mgyoil.com"]
        self.update_sql_field('name', value)
    	system.net.sendEmail(smtpProfile='MGY-Notify', fromAddr='otnotify@mgyoil.com', subject=header, body=body, html=0, to=recipients)

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def sql_id(self):
        return self._sql_id

    @sql_id.setter
    def sql_id(self, value):
        self._sql_id = value
    
    @property
    def created_datetime(self):
        return self.get_sql_field('createdDatetime')
	