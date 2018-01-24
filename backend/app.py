from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask_cors import CORS
from flask import Response
import requests
import json

import ApiUtils
import EmailUtils
import SubscriptionUtils
from AsterixUtils import *

app = Flask(__name__,
			static_folder = "../dist/static",
			template_folder = "../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template("index.html")

@app.route('/api/search')
def search():
	data = asterixSearch(request.args)
	response = Response(
		response=data,
		status=200,
		mimetype='application/json'
	)
	return response

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
	return handleSubscription(request.args)

@app.route('/api/unsubscribe', methods=['POST'])
def unsubscribe():
	return handleUnsubscription(request.args)

@app.route('/api/getListing', methods=['GET'])
def getListing():
	data = getListingInfo(request.args)
	response = Response(
		response=data,
		status=200,
		mimetype='application/json'
	)
	return response

@app.route('/signup')
def show_sign_up():
	return render_template('signup.html')

@app.route('/api/signup', methods=['POST'])
def signup():
	email = request.form['email']
	password = request.form['password']
	# TODO: Create account and return UID and access token
	return

@app.route('/login')
def show_login():
	return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	# TODO: Check if email/password is a valid combination
	return

@app.route('/post')
def show_post():
	return render_template('post.html')

@app.route('/api/post', methods=['POST'])
def post():
	# TODO: Insert listing into database
	return

@app.route('/account')
def show_account():
	return render_template('account.html')

@app.route('/api/updateAccount', methods=['POST'])
def update_account():
	# Update user account info in the database
	return

@app.route('/profile')
def show_profile():
	return render_template('profile.html')

@app.route('/api/updateProfile', methods=['POST'])
def update_profile():
	# Update user profile info in the database
	return

@app.route('/api/getUser')
def get_user():
	uid = request.form['uid']
	# Return user info as JSON
	return

def getListingInfo(args):
	postId = ApiUtils.argNullCheck(args.get("id"))
	return getPostingById(postId)

def asterixSearch(args):
	postType = args.get('type')
	if postType == "Jobs":
		jobsFunctionArgs = ApiUtils.getJobFunctionArgStr(args)
		return searchJobs(jobsFunctionArgs)
	elif postType == "Events":
		eventsFunctionArgs = ApiUtils.getEventFunctionArgStr(args)
		return searchEvents(eventsFunctionArgs)
	elif postType == "Items":
		itemsFunctionArgs = ApiUtils.getItemFunctionArgStr(args)
		return searchItems(itemsFunctionArgs)
	elif postType == "HousingSale":
		houseSaleFunctionArgs = ApiUtils.getHousingSaleFunctionArgStr(args)
		return searchHousingSale(houseSaleFunctionArgs)
	elif postType == "HousingLease":
		houseLeaseFunctionArgs = ApiUtils.getHousingLeaseFunctionArgStr(args)
		return searchHousingLease(houseLeaseFunctionArgs)
	return None

################ For Subscriptions using Big Active Data #####################

def handleSubscription(args):
	postType = args.get('type')
	userId = args.get("userId")
	print(json.dumps(args))
	if userId == None:
		return "Argument 'userId' must be provided."
	if postType == "Jobs":
		functionArgs = ApiUtils.getJobFunctionArgStr(args)
		return SubscriptionUtils.subscribeJobsChannel(functionArgs, userId)
	elif postType == "Events":
		functionArgs = ApiUtils.getEventFunctionArgStr(args)
		return SubscriptionUtils.subscribeEventsChannel(functionArgs, userId)
	elif postType == "Items":
		functionArgs = ApiUtils.getItemFunctionArgStr(args)
		return SubscriptionUtils.subscribeItemChannel(functionArgs, userId)
	elif postType == "HousingSale":
		functionArgs = ApiUtils.getHousingSaleFunctionArgStr(args)
		return SubscriptionUtils.subscribeHouseSaleChannel(functionArgs, userId)
	elif postType == "HousingLease":
		functionArgs = ApiUtils.getHousingLeaseFunctionArgStr(args)
		return SubscriptionUtils.subscribeHouseLeaseChannel(functionArgs, userId)
	return None

def handleUnsubscription(args):
	subId = args.get('subId')
	channelName = args.get("channelName")
	if subId == None or channelName == None:
		return "Provide both arguments: 'subId' and 'channelName'"
	status = SubscriptionUtils.unsubscribeFromChannel(subId, channelName)
	print("in app.py", status)
	if status == True:
		return "Successfully unsubscribed id {} from channel {}".format(subId, channelName)
	else:
		return "Error occured when unsubscribing id {} from channel {}".format(subId, channelName)
	#SubscriptionUtils.deleteSubIdFromUserSubscription(subId)

@app.route('/brokerNotifications', methods=['POST'])
def handleBrokerNotification():
	notificationJsonString = list(request.form.to_dict().keys())[0]
	notificationDict = json.loads(notificationJsonString)
	channelName = notificationDict["channelName"]
	channelResultSet = channelName + "Results"
	subId = notificationDict["subscriptionIds"][0]
	# Get results using the subscription id
	subIdResults = json.loads(SubscriptionUtils.getResultUsingSubId(channelResultSet, subId))["results"]
	userId = SubscriptionUtils.getUserIdUsingSubId(subId)

	# Send Email
	emailBody = EmailUtils.generateEmailHtmlStrFromResults(subIdResults, subId, channelName)
	print(emailBody)
	EmailUtils.sendEmail(emailBody, userId)

	# Delete all the results
	SubscriptionUtils.deleteResultUsingSubId(channelResultSet, subId)
	return "Success"

if __name__ == '__main__':
	app.run()
