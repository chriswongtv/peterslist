from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import requests
import json
app = Flask(__name__)

DB = 1 # 1 = AsterixDB, 0 = Couchbase

@app.route('/')
def show_index():
	return render_template('index.html')

@app.route('/api/search')
def search():
	if (DB):
		return asterixSearch(request.args)

@app.route('/housing/<post_id>')
def show_housing(post_id):
	return render_template('housing.html', info=json.loads(getListingInfo(post_id)))

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
	post_type = args.get('type')

	if (post_type == 'u'):
		payload = 'SELECT VALUE p FROM Postings p;'
	else:
		payload = 'SELECT VALUE p FROM Postings p WHERE p.postingCategory = "' + post_type + '"'

	if (post_type == 'Housing'):
		payload = getAsterixHousingSearchPayload(args, payload)
	if (post_type == 'Job'):
		payload = getAsterixJobSearchPayload(args, payload)
	if (post_type == 'Event'):
		payload = getAsterixEventSearchPayload(args, payload)
	if (post_type == 'ItemSale'):
		payload = getAsterixItemSaleSearchPayload(args, payload)
	if (post_type == 'LostFound'):
		payload = getAsterixLostAndFoundSearchPayload(args, payload)

	return queryAsterix(payload)

def getAsterixHousingSearchPayload(args, payload):
	room_type = args.get('room_type')
	start_price = args.get('start_price')
	end_price = args.get('end_price')
	movein_date = args.get('movein_date')
	parking = args.get('parking')
	bathroom = args.get('bathroom')
	pets = args.get('pets')
	roommates = args.get('roommates')

	if (room_type is not None):
		payload += ' and p.housingCategory =' + room_type
	if (start_price is not None):
		payload += ' and p.postInfo.amount>=' + start_price
	if (end_price is not None):
		payload += ' and p.postInfo.amount<=' + end_price
	# if (movein_date is not None):
		# TODO: Add move in date filter
	if (parking is not None):
		payload += ' and p.hasParking = ' + parking
	if (bathroom is not None):
		payload += ' and p.bathroomType = ' + bathroom
	if (pets is not None):
		payload += ' and p.petAllowed = ' + pets
	if (roommates is not None):
		if (roommates == 3):
			payload += ' and p.roomates > ' + 3
		else:
			payload += ' and p.roomates = ' + roommates

	payload += ';'

	return payload

def getAsterixJobSearchPayload(args, payload):

	category = args.get('category')
	title = args.get('title')
	location = args.get('location')
	
	if (category is not None):
		payload += ' and p.jobCategory = "' + category + '"'
	

	payload += ';'

	return payload

def getAsterixEventSearchPayload(args, payload):

	category = args.get('category')
	name = args.get('name')
	date = args.get('date')

	if (category is not None):
		payload += ' and p.eventCategory = "' + category + '"'
	
	

	payload += ';'

	return payload

def getAsterixItemSaleSearchPayload(args, payload):

	category = args.get('category')
	keyword = args.get('keyword')

	f (category is not None):
		payload += ' and p.itemCategory = "' + category + '"'
	

	payload += ';'

	return payload

def getAsterixLostAndFoundSearchPayload(args, payload):

	
	keyword = args.get('keyword')
	query = args.get('query') 
	
	if (query is not None):
		payload += ' and p.lostOrFound = "' + query + '"'

	if(keyword is not None):
		payload += ' and p.itemName = "' + keyword + '"'

	payload += ';'

	return payload

def queryAsterix(query):
	url = "http://localhost:19002/query/service"

	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'cache-control': "no-cache"
	}

	payload = 'statement=USE PeterList; ' + query

	response = requests.request("POST", url, data=payload, headers=headers)

	return json.dumps(json.loads(response.text)['results'])

def getListingInfo(id):
	return queryAsterix('SELECT p FROM Postings p WHERE p.postID = "' + id + '";')

if __name__ == '__main__':
	app.run()
