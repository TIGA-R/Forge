from system.tag import getConfiguration, configure


class EditTag(object):
	MERGE_OVERWRITE = "m"
	OVERWRITE = "o"
	
	def __init__(self, tagpath):
		self.tagpath = tagpath
		self.config = getConfiguration(tagpath)[0]
		self.name = self.config['name']
		self.base_path = self.tagpath.rsplit('/', 1)[0]
		self.base = {'name': self.name}
	
	@property
	def binding(self):
		return self.config['opcItemPath'].binding
	
	@binding.setter
	def binding(self, val):
		from com.inductiveautomation.ignition.common.config import BoundValue
#		print('here')
		try: 
			bound_value = BoundValue(self.config['opcItemPath'].bindType, val)
		except KeyError:
			bound_value = BoundValue('parameter', val)
#		print(bound_value)
#		print(self.config)
		self.binding_config = self.base
		self.binding_config['opcItemPath'] = bound_value
		self.binding_config['enabled'] = True
		print(configure(self.base_path, [self.binding_config], self.MERGE_OVERWRITE))
	
	@property
	def alarm_message_tag(self):
		if '(Message)' in self.name:
			return self
		message_tagpath = self.tagpath + ' (Message)'
		return EditTag(message_tagpath)
	
	@property
	def base_alarm(self):
		from copy import copy
		base_alarm_dict = copy(self.alarm_message_tag.base)
		base_alarm_dict['alarms'] = [{}]
		return base_alarm_dict
	
	@property
	def expression(self):
		return self.alarm_message_tag.config['expression']
	
	@property
	def alarm_name(self):
		return self.alarm_message_tag.config['alarms'][0]['name']
	
	@property
	def active_condition(self):
		return self.alarm_message_tag.config['alarms'][0]['activeCondition']
	
	@property
	def alarm_flag(self):
		try:
			return self.active_condition['value'].split('=')[1].split(',')[0].strip(' ")\'')
		except KeyError:
			return None
	
	# In hindsight, this was a bad idea
#	@alarm_flag.setter
#	def alarm_flag(self, val):
#		if int(val[0]) not in [0, 1]:
#			raise('Alarm flag key value must be 0 or 1')
#		if int(val[0]) == self.normal_key:
#			reverse_value = 0 if int(val[0]) == 1 else 1
#			self.normal_flag = self.normal_flag.replace(val[0], str(reverse_value))
#		self.alarm_flag_update = self.base_alarm
#		self.alarm_flag_update['alarms'][0]['name'] = self.alarm_name
#		self.alarm_flag_update['alarms'][0]['activeCondition'] = self.active_condition
#		self.alarm_flag_update['alarms'][0]['activeCondition']['value'] = self.alarm_flag_update['alarms'][0]['activeCondition']['value'].replace(self.alarm_flag, val)
#		self.alarm_flag_update['expression'] = self.expression.replace(self.alarm_flag, val)
#		print(configure(self.base_path, [self.alarm_flag_update], self.MERGE_OVERWRITE))
	
	@property
	def alarm_msg(self):
		if self.alarm_flag is None:
			return None
		return self.alarm_flag.split(' - ')[1]
	
	@property
	def alarm_key(self):
		if self.alarm_flag is None:
			return None
		self._alarm_key = int(self.alarm_flag.split(' - ')[0])
		if self._alarm_key not in [0,1]:
			raise('Alarm key did not return 0 or 1 value!')
		return self._alarm_key
	
	@property
	def normal_key(self):
		if self.alarm_key is None:
			return None
		return 0 if self.alarm_key == 1 else 1
	
	@property
	def normal_msg(self):
		if self.normal_key is None:
			return None
		self._normal_msg = self.expression.split(unicode(self.normal_key))[1]
		self._normal_msg = self._normal_msg.split(',')[0]
		self._normal_msg = self._normal_msg.strip(' -")\')')
		return self._normal_msg
	
	@property
	def normal_flag(self):
		if self.normal_key is None:
			return None
		return str(self.normal_key) + ' - ' + self.normal_msg
	
	# In hindsight, this was a bad idea too
#	@normal_flag.setter
#	def normal_flag(self, val):
#		self.normal_flag_update = self.alarm_message_tag.base
#		self.normal_flag_update['expression'] = self.expression.replace(self.normal_flag, val)
#		print(configure(self.base_path, [self.normal_flag_update], self.MERGE_OVERWRITE))
	
	def update_alarm_params(self, alarm_key, alarm_msg, normal_msg):
		"""
		param_dict:
		->'alarm_key'->[0 or 1]
		->'alarm_msg'->String
		->'normal_msg'->String
		"""
		from copy import copy
		assert self.normal_flag is not None, "Not an alarm-configurable tag"
		
		new_alarm_flag = str(alarm_key) + ' - ' + alarm_msg
		self.flag_update = copy(self.base_alarm)
		self.flag_update['alarms'][0]['name'] = self.alarm_name
		self.flag_update['alarms'][0]['enabled'] = True
		self.flag_update['alarms'][0]['activeCondition'] = self.active_condition
		self.flag_update['alarms'][0]['activeCondition']['value'] = self.flag_update['alarms'][0]['activeCondition']['value'].replace(self.alarm_flag, new_alarm_flag)
		if alarm_key == self.alarm_key:
			self.flag_update['expression'] = copy(self.expression).replace(self.normal_msg, normal_msg).replace(self.alarm_flag, new_alarm_flag)
		else:
			self.flag_update['expression'] = copy(self.expression).replace(self.alarm_msg, normal_msg).replace(self.normal_flag, new_alarm_flag)
		self.flag_update['enabled'] = True
		print(configure(self.base_path, [self.flag_update], self.MERGE_OVERWRITE))