from flask import *
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

client = MongoClient()
db = client['songza']
collection = db['curators']


@app.route("/")
def main():
	filename = "Playlists on Songza.html"
	# curator = collection.find_one({'name': 'Jesse Sussman'})
	# image_url = curator['image_url']

	# once recommendations have been made, load them here to 
	# pass into the page

	return render_template(filename, curators=[curator])

if __name__ == "__main__":
    app.run()