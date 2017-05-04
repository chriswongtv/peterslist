from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/api/search")
def search():
	post_type = request.form['type']
	search_keyword = request.form['keyword']
	search_filters = request.form['filters']

	# TODO: Perform search query and return result as JSON

@app.route("<[post_type]>/<int:post_id>")
def show_listing(post_type, post_id):
	# TODO: Pull listing details from db and render the listing detail page
	return render_template('listing.html')

if __name__ == "__main__":
	app.run()