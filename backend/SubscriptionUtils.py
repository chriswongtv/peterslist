import requests
import json
from flask import request

from AsterixUtils import *

# Asterix Query
SUBSCRIBE_JOBS_CHANNEL = 'subscribe to jobChannel({},{},{}) on peterListBroker;'
SUBSCRIBE_HOUSING_SALE_CHANNEL = 'subscribe to housingSaleChannel({},{},{},{},{},{},{},{},{},{}) on peterListBroker;'


INSERT_USER_SUBSCRIPTION = 'insert into UserSubscription({"subID": "{}", "userID": "{}"});'
GET_CHANNEL_RESULT_BY_SUBID = 'SELECT r.result.p FROM {} r WHERE r.subscriptionId = uuid("{}");'
DELETE_CHANNEL_RESULT = 'DELETE from {} r WHERE r.subscriptionId = uuid("{}");'

# API Response Messages
SUBSCRIBE_API_RESPONSE = "Subscribed userId {} with subscription id {}."

def subscribeToJobsChannel(args):
	jobType = argNullCheck(args.get("jobType"))
	jobIndustry = argNullCheck(args.get("jobIndustry"))
	timeInterval = argNullCheck(args.get("timeInterval"))
	userId = argNullCheck(args.get("userId"))
	if (userId == None):
		return "Argument 'userId' must be provided."

	subscribeString = SUBSCRIBE_JOBS_CHANNEL.format(jobType,jobIndustry,timeInterval)
	return subscribeToChannelAndInsertUser(subscribeString, userId)

def subscribeToHousingSaleChannel(args):
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
	userId = argNullCheck(args.get("userId"))

	if (userId == None):
		return "Argument 'userId' must be provided."

	subscribeStr = SUBSCRIBE_HOUSING_SALE_CHANNEL.format(priceMin,priceMax,bedroomNumber,
														bathroomNumber,homeType,size,dateAvailable,
														furnished,parkingNumber,timeInterval)
	return subscribeToChannelAndInsertUser(subscribeStr, userId)

def subscribeToChannelAndInsertUser(subscribeStr, userId):
	resp = queryAsterix(subscribeStr)
	if resp == None:
		return "Error subscribing to this channel"
	response = json.loads(resp)
	subId = response[0]
	insertUserSubscription(userId, subId)
	return SUBSCRIBE_API_RESPONSE.format(userId, subId)

def insertUserSubscription(userId, subId):
	insertString = INSERT_USER_SUBSCRIPTION.format(subId, userId)
	queryAsterix(insertString)

def getResultUsingSubId(channelResultSet, subId):
	queryString = GET_CHANNEL_RESULT_BY_SUBID.format(channelResultSet, subId)
	result = queryAsterix(queryString)
	return result

'''
Delete all the results with the given sub id from the channelResultDataset
'''
def deleteResultUsingSubId(channelResultSet, subId):
	deleteString = DELETE_CHANNEL_RESULT.format(channelResultSet, subId)
	status = deleteAsterix(deleteString)
	return status

'''
Send email using the MailGun API
'''
def sendEmail(result, emailAddress):
	return True

######################## Helper Functions ######################
def argNullCheck(argStr):
	if argStr == None:
		return "NULL"
	return '"' + argStr + '"'
