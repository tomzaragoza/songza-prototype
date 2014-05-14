from flask import *
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

client = MongoClient()
db = client['songza']
collection = db['curators']


@app.route("/")
def main():
	return redirect(url_for('curators'))


@app.route("/curators")
def curators():
	filename = "curators.html"
	all_curators = collection.find()

	return render_template(filename, all_curators=all_curators)


@app.route("/curator/<name>")
def curator_page(name):

	filename = "curator_profile.html"

	curator_obj = collection.find_one({'name': name})

	# Get similar curators
	similar_curators = curator_obj['similar_curators']
	similar_curators.sort()
	similar_curators.reverse()

	final_similar_curators = []

	for curator in similar_curators:
		d = collection.find_one({'name': curator[1]})
		final_similar_curators.append(collection.find_one({'name': curator[1]}))

	return render_template(filename, curator=curator_obj, similar_curators=final_similar_curators, playlists=curator_obj['playlists'])


if __name__ == "__main__":
    app.run(debug=True, port=5000)