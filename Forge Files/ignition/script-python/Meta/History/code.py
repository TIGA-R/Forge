
def update_udt_history(oldUDTTag, newUDTTag):

	project = 'Magnolia'
	messageHandler =  'Meta.History.UpdateHistory'
	query = """
	select count(tagpath) from sqlth_te where tagpath like '%s%%' 
	"""%oldUDTTag.split(']')[1]
	sqlCount = system.db.runScalerQuery(query, 'Historian01')
	assert sqlCount != 0
	assert sqlCount < 70
	oldUDTTagList = oldUDTTag.split('/').split(']')[1]
	newUDTTagList = newUDTTag.split('/').split(']')[1]
	assert len(oldUDTTagList) == 6
	assert len(newUDTTagList) == 6
	payload = {
		'oldUDTTagList': oldUDTTagList,
		'newUDTTagList': newUDTTagList,
	}
	return system.util.sendMessage(project, messageHandler, payload=payload)
