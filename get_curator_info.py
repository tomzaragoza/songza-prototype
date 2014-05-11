from pymongo import MongoClient
from bs4 import BeautifulSoup
from pprint import pprint
import urllib

client = MongoClient()
db = client['songza']
collection = db['curators']

def get_activities():
	""" 
		Return a list of all activities that Songza put together.
	"""

	url = "activities.html"
	source = urllib.urlopen(url).read()

	soup = BeautifulSoup(source)

	activities = []

	for i in soup.find_all('a'):
		activities.append(i.get('href'))

	return activities


def get_curator_playlist(url, curator_name):
	""" 
		Retrieve all playlists that a guest curator has put together.
	"""

	source = urllib.urlopen(url).read()
	soup = BeautifulSoup(source)
	playlists = []

	for i in soup.find_all("li", "browse-playlist"):
		a_element = i.find('a')
		title = a_element.find('h3').text
		description = a_element.find('p', 'browse-playlist-description').text

		playlist_obj = {'title': title, 'curator': curator_name, 'description': description }

		playlists.append(playlist_obj)

	return playlists


def get_curator_info():
	""" 
		Get all guest curators.
	"""

	url = "http://songza.com"
	activities = get_activities()

	curators = []
	all_curator_names = {} # for checking duplicates

	for activity in activities:
		source = urllib.urlopen("http://songza.com" + activity).read()
		soup = BeautifulSoup(source)

		for i in soup.find_all('h4', 'browse-playlist-byline'):

			link = i.find('a')
			if link is not None:
				curator_name = link.find('span').text
				if not curator_name in all_curator_names:
					print curator_name
					all_curator_names[curator_name] = True
					curator_url = url + link.get('href')
					curator_playlist = get_curator_playlist(curator_url, curator_name)

					curator_obj = {'name': curator_name, 'link': curator_url, 'playlists': curator_playlist}

					curators.append(curator_obj)

	return curators

def load_curator_info(curators):
	""" 
		Load curators into Mongo. 
		The curators get saved in a collection called 'curators'.
	"""
	for curator in curators:
		# print "Working on curator {0}".format(curator['curator'])
		collection.insert(curator)

if __name__ == "__main__":
	RUN = False
	if RUN:
		print "Loading Curator information into Mongo"
		load_curator_info(get_curator_info())
