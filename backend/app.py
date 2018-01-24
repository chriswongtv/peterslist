from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask_cors import CORS
import requests
import json

import SubscriptionUtils
import ApiUtils
from AsterixUtils import *

app = Flask(__name__,
			static_folder = "../dist/static",
			template_folder = "../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

DB = 1 # 1 = AsterixDB, 0 = Couchbase

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template("index.html")

@app.route('/api/search')
def search():
	if (DB):
		return asterixSearch(request.args)

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
	return handleSubscription(request.args)

@app.route('/api/unsubscribe', methods=['POST'])
def unsubscribe():
	return

@app.route('/api/getListing')
def getListing():
	return getListingInfo(request.args.get('id'))

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

def getListingInfo(id):
	return queryAsterix('SELECT p FROM Postings p WHERE p.postID = "' + id + '";')

################ For Subscriptions using Big Active Data #####################

def handleSubscription(args):
	postType = args.get('type')
	userId = args.get("userId")
	if (userId == None):
		return "Argument 'userId' must be provided."
	if postType == "Jobs":
		functionArgs = ApiUtils.getJobFunctionArgStr(args)
		return SubscriptionUtils.subscribeJobsChannel(functionArgs, userId)
	elif postType == "Events":
		functionArgs = ApiUtils.getEventFunctionArgStr(args)
		return SubscriptionUtils.getEventFunctionArgStr(functionArgs, userId)
	elif postType == "Items":
		functionArgs = ApiUtils.getItemFunctionArgStr(args)
		return SubscriptionUtils.getItemFunctionArgStr(functionArgs, userId)
	return None

@app.route('/brokerNotifications', methods=['POST'])
def handleBrokerNotification():
	notificationJsonString = list(request.form.to_dict().keys())[0]
	notificationDict = json.loads(notificationJsonString)

	channelResultSet = notificationDict["channelName"] + "Results"
	subId = notificationDict["subscriptionIds"][0]
	# Get results using the subscription id
	subIdResults = json.loads(SubscriptionUtils.getResultUsingSubId(channelResultSet, subId))
	#for i in subIdResults:
	#	print(i["p"]["jobIndustry"])

	#TODO sendEmail(subIdResults, emailAddress)

	# Delete all the results
	SubscriptionUtils.deleteResultUsingSubId(channelResultSet, subId)
	return subIdResults

if __name__ == '__main__':
	app.run()
