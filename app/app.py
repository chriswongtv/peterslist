from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import requests
app = Flask(__name__)

DB = 1 # 1 = AsterixDB, 0 = Couchbase

@app.route('/')
def show_index():
	return render_template('index.html')

@app.route('/api/search')
def search():
	if (DB):
		return asterixSearch(request.args)

def asterixSearch(args):
	post_type = args.get('type')

	if (post_type == 'u'):
		payload = 'statement=USE PeterList; SELECT VALUE p FROM Postings p;'
	else:
		payload = 'statement=USE PeterList; SELECT VALUE p FROM Postings p WHERE p.postingCategory = "' + post_type + '"'

	if (post_type == 'Housing'):
		payload = getAsterixHousingSearchPayload(args, payload)

	url = "http://localhost:19002/query/service"

	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'cache-control': "no-cache"
	}

	response = requests.request("POST", url, data=payload, headers=headers)

	return response.text

def getAsterixHousingSearchPayload(args, payload):
	room_type = args.get('room_type')
	start_price = args.get('start_price')
	end_price = args.get('end_price')
	movein_date = args.get('movein_date')
	parking = args.get('parking')
	bathroom = args.get('bathroom')
	pets = args.get('pets')

	if (room_type is not None ):
		payload += ' and p.housingCategory =' + room_type
	if (start_price is not None ):
		payload += ' and p.postInfo.amount>=' + start_price
	if (end_price is not None ):
		payload += ' and p.postInfo.amount<=' + end_price
	if (parking is not None ):
		payload += ' and p.hasParking = ' + parking
	if (bathroom is not None ):
		payload += ' and p.bathroomType = ' + bathroom
	if (pets is not None ):
		payload += ' and p.petAllowed = ' + pets

	payload += ';'

	return payload

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

if __name__ == '__main__':
	app.run()
