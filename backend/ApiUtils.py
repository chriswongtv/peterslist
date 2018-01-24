
JOBS_FUNCTION = "({jobType},{jobIndustry},{timeInterval})"
EVENT_FUNCTION = "({eventCategory},{eventStartOn},{timeInterval})"
ITEM_SALE_FUNCTION = "({itemCategory},{condition},{priceMin},{priceMax},{timeInterval})"
HOUSING_LEASE_FUNCTION = "({priceMin},{priceMax},{bedroomNumber},{bathroomNumber},{homeType},{size},{dateAvailable},{furnished},{hasParking},{petAllowed},{endDate},{roommates},{timeInterval})"
HOUSING_SALE_FUNCTION = "({priceMin},{priceMax},{bedroomNumber},{bathroomNumber},{homeType},{size},{dateAvailable},{furnished},{parkingNumber},{timeInterval})"

'''
For function:
searchJob(jobType,jobIndustry,timeInterval)
'''
def getJobFunctionArgStr(args):
    jobType = argNullCheck(args.get("jobType"))
    jobIndustry = argNullCheck(args.get("jobIndustry"))
    timeInterval = argNullCheck(args.get("timeInterval"))

    functionArgStr = JOBS_FUNCTION.format(jobType = jobType, jobIndustry = jobIndustry, timeInterval = timeInterval)
    return functionArgStr

'''
For function:
searchEvent(eventCategory,eventStartOn,timeInterval)
'''
def getEventFunctionArgStr(args):
    eventCategory = argNullCheck(args.get("eventCategory"))
    eventStartOn = argNullCheck(args.get("eventStartOn"))
    timeInterval = argNullCheck(args.get("timeInterval"))

    functionArgStr = EVENT_FUNCTION.format(eventCategory = eventCategory,eventStartOn = eventStartOn,timeInterval = timeInterval)
    return functionArgStr

'''
For the function:
searchItemSale(itemCategory,condition,priceMin,priceMax,timeInterval)
'''
def getItemFunctionArgStr(args):
    itemCategory = argNullCheck(args.get("itemCategory"))
    condition = argNullCheck(args.get("condition"))
    priceMin = argNullCheck(args.get("priceMin"))
    priceMax = argNullCheck(args.get("priceMax"))
    timeInterval = argNullCheck(args.get("timeInterval"))

    functionArgStr = ITEM_SALE_FUNCTION.format(itemCategory = itemCategory, condition = condition, priceMin = priceMin,
                                                priceMax = priceMax, timeInterval = timeInterval)
    return functionArgStr

'''
For the function:
searchHousingLease(priceMin,priceMax,bedroomNumber,bathroomNumber,homeType,size,dateAvailable,
                    furnished,hasParking,petAllowed,endDate,roommates,timeInterval)
'''
def getHousingLeaseFunctionArgStr(args):
    priceMin = argNullCheck(args.get("priceMin"))
    priceMax = argNullCheck(args.get("priceMax"))
    bedroomNumber = argNullCheck(args.get("bedroomNumber"))
    bathroomNumber = argNullCheck(args.get("bathroomNumber"))
    homeType = argNullCheck(args.get("homeType"))
    size = argNullCheck(args.get("size"))
    dateAvailable = argNullCheck(args.get("dateAvailable"))
    furnished = argNullCheck(args.get("furnished"))
    hasParking = argNullCheck(args.get("hasParking"))
    petAllowed = argNullCheck(args.get("petAllowed"))
    endDate = argNullCheck(args.get("endDate"))
    roommates = argNullCheck(args.get("roommates"))
    timeInterval = argNullCheck(args.get("timeInterval"))

    functionArgStr = HOUSING_LEASE_FUNCTION.format(priceMin = priceMin,priceMax = priceMax,bedroomNumber = bedroomNumber,
                                                bathroomNumber = bathroomNumber,homeType = homeType,size = size,
                                                dateAvailable = dateAvailable,furnished = furnished,
                                                hasParking = hasParking, petAllowed = petAllowed,
                                                endDate = endDate, roommates = roommates, timeInterval = timeInterval)
    return functionArgStr


'''
For the fuction:
searchHousingSale(priceMin,priceMax,bedroomNumber,bathroomNumber,homeType,size,dateAvailable,
                    furnished,parkingNumber,timeInterval)
'''
def getHousingSaleFunctionArgStr(args):
	priceMin = argNullCheck(args.get("priceMin"))
	priceMax = argNullCheck(args.get("priceMax"))
	bedroomNumber = argNullCheck(args.get("bedroomNumber"))
	bathroomNumber = argNullCheck(args.get("bathroomNumber"))
	homeType = argNullCheck(args.get("homeType"))
	size = argNullCheck(args.get("size"))
	dateAvailable = argNullCheck(args.get("dateAvailable"))
	furnished = argNullCheck(args.get("furnished"))
	parkingNumber = argNullCheck(args.get("parkingNumber"))
	timeInterval = argNullCheck(args.get("timeInterval"))

	functionArgStr = HOUSING_SALE_FUNCTION.format(priceMin = priceMin,priceMax = priceMax,bedroomNumber = bedroomNumber,
                                                bathroomNumber = bathroomNumber,homeType = homeType,size = size,
                                                dateAvailable = dateAvailable,furnished = furnished,
                                                parkingNumber = parkingNumber, timeInterval = timeInterval)
	return functionArgStr

def argNullCheck(argStr):
	if argStr == None:
		return "NULL"
	return '"' + argStr + '"'
