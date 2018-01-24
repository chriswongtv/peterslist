import requests
import json

ASTERIX_API_URL = "http://localhost:19002/query/service"

HEADERS = { 'content-type': "application/x-www-form-urlencoded",
			'cache-control': "no-cache" }

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
		return json.dumps(json.loads(response.text)['results'])
	return None

def dmlAsterix(query):
	response = executePeterListQuery(query)
	if response != None:
		status = json.dumps(json.loads(response.text)['status'])
		return status
	return None

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
