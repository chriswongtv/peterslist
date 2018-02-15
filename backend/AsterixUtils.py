import requests
import json

from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ASTERIX_API_URL = environ.get("DB_URL")
HEADERS = { 'content-type': "application/x-www-form-urlencoded",
			'cache-control': "no-cache" }

INSERT_POSTING_STR = 'INSERT INTO Postings({})'
INSERT_USER_STR = 'INSERT INTO User({})'

GET_USERID_BY_EMAIL_PASSWORD = 'SELECT u.userID from User u where u.email = "{}" AND u.password = "{}";'
POSTING_BY_ID_STR = "SELECT VALUE p FROM Postings p WHERE p.postID = {};"

JOBS_FUNCTION_STR = "searchJob{};"
EVENTS_FUNCTION_STR = "searchEvent{};"
ITEMS_FUNCTION_STR = "searchItemSale{};"
HOUSING_SALE_FUNCTION_STR = "searchHousingSale{};"
HOUSING_LEASE_FUNCTION_STR = "searchHousingLease{};"

def executePeterListQuery(query):
	payload = 'statement=USE PeterList; ' + query
	print(payload)
	try:
		response = requests.request("POST", ASTERIX_API_URL, data=payload, headers=HEADERS)
		return response
	except:
		print("Error connecting to the database.")

def queryAsterix(query):
	response = executePeterListQuery(query)
	if response != None:
		return json.dumps(json.loads(response.text))#['results'])
	return None

def dmlAsterix(query):
	response = executePeterListQuery(query)
	if response != None:
		status = json.loads(response.text)['status']
		return status
	return None

def insetPosting(jsonStr):
	statement = INSERT_POSTING_STR.format(jsonStr)
	return queryAsterix(statement)

def insertUser(jsonStr):
	statement = INSERT_USER_STR.format(jsonStr)
	return queryAsterix(statement)

def isValidUser(email, password):
	statement = GET_USERID_BY_EMAIL_PASSWORD.format(email,password)
	response = executePeterListQuery(statement)
	resp_dict = json.loads(response.text)
	resultCount = resp_dict["metrics"]["resultCount"]
	print(resp_dict)
	if resultCount >= 1:
		return json.dumps(resp_dict["results"])
	return "Invalid"

def getPostingById(id):
	queryStr = POSTING_BY_ID_STR.format(id)
	return queryAsterix(queryStr)

###################### SEARCH POSTINGS FUNCTIONS ######################

def searchJobs(functionArgStr):
	function = JOBS_FUNCTION_STR.format(functionArgStr)
	result = queryAsterix(function)
	return result

def searchEvents(functionArgStr):
	function = EVENTS_FUNCTION_STR.format(functionArgStr)
	result = queryAsterix(function)
	return result

def searchItems(functionArgStr):
	function = ITEMS_FUNCTION_STR.format(functionArgStr)
	result = queryAsterix(function)
	return result

def searchHousingSale(functionArgStr):
	function = HOUSING_SALE_FUNCTION_STR.format(functionArgStr)
	result = queryAsterix(function)
	return result

def searchHousingLease(functionArgStr):
	function = HOUSING_LEASE_FUNCTION_STR.format(functionArgStr)
	result = queryAsterix(function)
	return result
