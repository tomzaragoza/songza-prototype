from flask import *
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

client = MongoClient()
db = client['songza']
collection = db['curators']


@app.route("/")
def main():
	filename = "Playlists on Songza.html"
	
	# in this example, use Jesse Sussman
	curator = collection.find_one({'name': 'Jesse Sussman'})


	similar_curators = curator['similar_curators']
	similar_curators.sort()
	similar_curators.reverse()

	final_similar_curators = []
	for curator in similar_curators:
		d = collection.find_one({'name': curator[1]})
		final_similar_curators.append(collection.find_one({'name': curator[1]}))


	return render_template(filename, similar_curators=final_similar_curators)

if __name__ == "__main__":
    app.run()