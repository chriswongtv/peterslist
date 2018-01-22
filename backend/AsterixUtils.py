import requests
import json

ASTERIX_API_URL = "http://localhost:19002/query/service"

HEADERS = { 'content-type': "application/x-www-form-urlencoded",
			'cache-control': "no-cache" }

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

def deleteAsterix(query):
	response = executePeterListQuery(query)
	if response != None:
		status = json.dumps(json.loads(response.text)['status'])
		return status
	return None
