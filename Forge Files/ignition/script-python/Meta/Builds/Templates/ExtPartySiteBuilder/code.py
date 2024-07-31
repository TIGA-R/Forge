
def siteBuild(site,area=None,foreman=None, route=None, thirdParty=None,xrefNum=None, merrickId=None):           
#	for site in siteList:
    Meta.Site.Facility.new(site, area=area, foreman=foreman, route=route, enabled=True,build_default_pad=True)

    baseTagPath = "[North01]North/North01/%s/%s/Meter"%(site, site)
      
    # Properties that will be configured on that Tag.  
    tagName = "%s %s Sales"%(site, thirdParty)  
    typeId = "METER/Data Import/Import Meter v02"  
    tagType = "UdtInstance"  
    # Parameters to pass in.  
    motorNum = ""  
      
    # Configure the Tag.  
    tag = {  
    "name": tagName,  
    "typeId" : typeId,  
    "tagType" : tagType,    
    }  
      
    # Set the collision policy to Abort. That way if a tag already exists at the base path,  
    # we will not override the Tag. If you are overwriting an existing Tag, then set this to "o".  
    collisionPolicy = "a"  
      
    # Create the Tag.  
    system.tag.configure(baseTagPath, [tag], collisionPolicy)
    Meta.Equipment.Equipment.add_equipment_from_tagpath(baseTagPath+'/%s'%tagName,merrick_id=merrickId,
                                        third_party_xref=xrefNum,
                                        third_party_group=thirdParty)
                                        
def meterBuild(site, thirdParty=None,xrefNum=None, merrickId=None):           
#	for site in siteList:
   

	baseTagPath = "[North01]North/North01/%s/%s/Meter"%(site, site)
	 
	# Properties that will be configured on that Tag.  
	tagName = "%s %s Buyback"%(site, thirdParty)  
	typeId = "METER/Data Import/Import Meter v02"  
	tagType = "UdtInstance"  
	# Parameters to pass in.  
	motorNum = ""  
	 
	# Configure the Tag.  
	tag = {  
	"name": tagName,  
	"typeId" : typeId,  
	"tagType" : tagType,    
	}  
	 
	# Set the collision policy to Abort. That way if a tag already exists at the base path,  
	# we will not override the Tag. If you are overwriting an existing Tag, then set this to "o".  
	collisionPolicy = "a"  
	 
	# Create the Tag.  
	system.tag.configure(baseTagPath, [tag], collisionPolicy)
	Meta.Equipment.Equipment.add_equipment_from_tagpath(baseTagPath+'/%s'%tagName,merrick_id=merrickId,
	                                   third_party_xref=xrefNum,
	                                   third_party_group=thirdParty)                                       