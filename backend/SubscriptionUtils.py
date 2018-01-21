import requests
import json
from flask import request

from AsterixUtils import *

SUBSCRIBE_JOBS_CHANNEL = 'subscribe to jobChannel({},{},{}) on peterListBroker;'
INSERT_USER_SUBSCRIPTION = 'insert into UserSubscription({"subID": "{}", "userID": "{}"});'
GET_CHANNEL_BY_SUBID = 'SELECT r.result.p FROM {} r WHERE r.subscriptionId = uuid("{}");'
DELETE_CHANNEL_RESULT = 'DELETE from {} r WHERE r.subscriptionId = uuid("{}");'

SUBSCRIBE_API_RESPONSE = "Subscribed userId {} with subscription id {}."

def subscribeToJobsChannel(args):
	jobType = argNullCheck(args.get("jobType"))
	jobIndustry = argNullCheck(args.get("jobIndustry"))
	timeInterval = argNullCheck(args.get("timeInterval"))
	userId = argNullCheck(args.get("userId"))
	if (userId == None):
		return "Argument 'userId' must be provided."

	subscribeString = SUBSCRIBE_JOBS_CHANNEL.format(jobType,jobIndustry,timeInterval)
	resp = queryAsterix(subscribeString)
	
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
	queryString = GET_CHANNEL_BY_SUBID.format(channelResultSet, subId)
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
