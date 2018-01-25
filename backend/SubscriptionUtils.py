import requests
import json
from flask import request

from AsterixUtils import *

# Asterix Query
SUBSCRIBE_JOBS_CHANNEL = 'subscribe to jobChannel{} on peterListBroker;'
SUBSCRIBE_EVENT_CHANNEL = 'subscribe to eventChannel{} on peterListBroker;'
SUBSCRIBE_ITEM_CHANNEL = 'subscribe to itemSaleChannel{} on peterListBroker;'
SUBSCRIBE_HOUSING_SALE_CHANNEL = 'subscribe to housingSaleChannel{} on peterListBroker;'
SUBSCRIBE_HOUSING_LEASE_CHANNEL = 'subscribe to housingLeaseChannel{} on peterListBroker;'

INSERT_USER_SUBSCRIPTION = 'insert into UserSubscription({{"subID": "{}", "userID": "{}"}});'
GET_CHANNEL_RESULT_BY_SUBID = 'SELECT VALUE r.result FROM {} r WHERE r.subscriptionId = uuid("{}");'
DELETE_CHANNEL_RESULT = 'DELETE from {} r WHERE r.subscriptionId = uuid("{}");'

# API Response Messages
SUBSCRIBE_API_RESPONSE = "Subscribed userId {} with subscription id {}."

def subscribeJobsChannel(functionArgStr, userId):
	subscribeString = SUBSCRIBE_JOBS_CHANNEL.format(functionArgStr)
	return subscribeToChannelAndInsertUser(subscribeString, userId)

def subscribeEventsChannel(functionArgStr, userId):
	subscribeString = SUBSCRIBE_EVENT_CHANNEL.format(functionArgStr)
	return subscribeToChannelAndInsertUser(subscribeString, userId)

def subscribeItemChannel(functionArgStr, userId):
	subscribeString = SUBSCRIBE_ITEM_CHANNEL.format(functionArgStr)
	return subscribeToChannelAndInsertUser(subscribeString, userId)

def subscribeHouseSaleChannel(functionArgStr, userId):
	subscribeString = SUBSCRIBE_HOUSING_SALE_CHANNEL.format(functionArgStr)
	return subscribeToChannelAndInsertUser(subscribeString, userId)

def subscribeHouseLeaseChannel(functionArgStr, userId):
	subscribeString = SUBSCRIBE_HOUSING_LEASE_CHANNEL.format(functionArgStr)
	return subscribeToChannelAndInsertUser(subscribeString, userId)

def subscribeToChannelAndInsertUser(subscribeStr, userId):
	resp = queryAsterix(subscribeStr)
	if resp == None:
		return "Error subscribing to this channel"
	response = json.loads(resp)['results']
	subId = response[0]
	insertUserSubscription(userId, subId)
	return SUBSCRIBE_API_RESPONSE.format(userId, subId)

def insertUserSubscription(userId, subId):
	insertString = INSERT_USER_SUBSCRIPTION.format(subId, userId)
	print(dmlAsterix(insertString))

def getResultUsingSubId(channelResultSet, subId):
	queryString = GET_CHANNEL_RESULT_BY_SUBID.format(channelResultSet, subId)
	result = queryAsterix(queryString)
	return result

'''
Delete all the results with the given sub id from the channelResultDataset
'''
def deleteResultUsingSubId(channelResultSet, subId):
	deleteString = DELETE_CHANNEL_RESULT.format(channelResultSet, subId)
	status = dmlAsterix(deleteString)
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
