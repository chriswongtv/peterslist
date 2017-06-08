from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import requests
app = Flask(__name__)


# Configurable
# Connection string to use
COUCHBASE_CONNSTR = 'couchbase://localhost/postings'
# Password for bucket, if applicable
COUCHBASE_PASSWORD = None

from flask import Flask, g, abort, request, json, make_response, Response
from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery
import couchbase.exceptions as cb_errors
import couchbase.fulltext as FT

app = Flask(__name__)
app.config.from_object(__name__)


DB = 0 # 1 = AsterixDB, 0 = Couchbase

@app.route('/')
def show_index():
	return render_template('index.html')

@app.route('/api/search')
def search():
        return databaseSearch(request.args)

@app.route('/search2/<post_ID>')
def search2(post_ID):
#    response = requests.request("GET","http://localhost:8093/query?statement=SELECT%20text%20from%20postings%20limit%201")
    response = requests.request("GET",'http://localhost:8093/query?statement=SELECT VALUE p FROM postings p WHERE p.postInfo.userID = "'+post_ID+'";')
    return response.text

@app.route('/<post_type>/<int:post_id>')
def show_listing(post_type, post_id):
	# TODO: Pull listing details from db and render the listing detail page
	return render_template('listing.html')

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

@app.route('/housing/<post_id>')
def show_housing(post_id):
	return render_template('housing.html', info=json.loads(getListingInfo(post_id)))

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

## Common Functions

def getListingInfo(id):
	return queryCouchbase('SELECT p FROM postings p WHERE p.postID = "' + id + '";')

def getHousingSearchPayload(args, payload):
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

def databaseSearch(args):
        post_type = args.get('type')
        if (post_type == 'u'):
                payload = 'SELECT VALUE p FROM postings p;'
        else:
                payload = 'SELECT VALUE p FROM postings p WHERE p.postingCategory = "' + post_type + '"'
        if (post_type == 'Housing'):
                payload = getHousingSearchPayload(args, payload)
        if DB:
                return queryAsterix(payload)
        else:
                return queryCouchbase(payload)

def getItemSaleSearchPayload(args, payload):

	category = args.get('category')
	keyword = args.get('keyword')
	
	# if (category is not None):
	# 	payload += ' and p.jobCategory =' + category

	#USE one character off in ASTERIX DB
	# if (title is not None):
	# 	payload += ' and p.postInfo.amount>=' + title
	# if (location is not None):
	# 	payload += ' and p.postInfo.amount<=' + location
	

	payload += ';'
	return payload

def getEventSearchPayload(args, payload):

	category = args.get('category')
	name = args.get('name')
	date = args.get('date')
	
	# if (category is not None):
	# 	payload += ' and p.jobCategory =' + category

	#USE one character off in ASTERIX DB
	# if (title is not None):
	# 	payload += ' and p.postInfo.amount>=' + title
	# if (location is not None):
	# 	payload += ' and p.postInfo.amount<=' + location
	
	payload += ';'
	return payload

def getLostAndFoundSearchPayload(args, payload):	
	keyword = args.get('keyword')
	query = args.get('query') 	# 0 means lost and 1 means found
	
	if (query is not None):
		payload += ' and p.lostOrFound = ' + query

	if(keyword is not None):
		payload += ' and p.itemName = "' + keyword + '"'	

	payload += ';'

	return payload

def getJobSearchPayload(args, payload):

	category = args.get('category')
	title = args.get('title')
	location = args.get('location')
	

	# if (category is not None):
	# 	payload += ' and p.jobCategory =' + category

	#USE one character off in ASTERIX DB
	# if (title is not None):
	# 	payload += ' and p.postInfo.amount>=' + title
	# if (location is not None):
	# 	payload += ' and p.postInfo.amount<=' + location
	
	payload += ';'

	return payload


### Query Functions

def queryCouchbase(query):
        url='http://localhost:8093/query?statement='+query
        response = requests.request("GET",url)
        return json.dumps(json.loads(response.text)['results'])

def queryAsterix(query):
	url = "http://localhost:19002/query/service"

	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'cache-control': "no-cache"
	}

	payload = 'statement=USE PeterList; ' + query

	response = requests.request("POST", url, data=payload, headers=headers)

	return json.dumps(json.loads(response.text)['results'])

if __name__ == '__main__':
	app.run()
