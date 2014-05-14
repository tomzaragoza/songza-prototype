from pymongo import MongoClient
from bs4 import BeautifulSoup
from pprint import pprint
import urllib

client = MongoClient()
db = client['songza']
curators_coll = db['curators']
featured_artists_coll = db['featured_artists']

def get_activities():
	""" 
		Return a list of all activities that Songza put together.
	"""

	url = "static/activities.html"
	source = urllib.urlopen(url).read()

	soup = BeautifulSoup(source)

	activities = []

	for i in soup.find_all('a'):
		activities.append(i.get('href'))

	return activities


def get_curator_image(url):
	source = urllib.urlopen(url).read()
	soup = BeautifulSoup(source)
	image_element = soup.find('img', 'browse-profile-image')
	image_src = image_element.get('src')
	
	return image_src


def get_curator_details(url, curator_name):
	""" 
		Retrieve all playlists that a guest curator has put together.
	"""

	source = urllib.urlopen(url).read()
	soup = BeautifulSoup(source)
	
	location = soup.find('h5', 'browse-profile-location').text
	bio = soup.find('h3', 'browse-profile-bio').text

	try:
		# Just in case it doesn't exist
		website = soup.find('a', 'browse-profile-url').get('href')
	except:
		website = ''

	playlists = []
	featured = []
	for i in soup.find_all("li", "browse-playlist"):
		a_element = i.find('a')
		title = a_element.find('h3').text
		description = a_element.find('p', 'browse-playlist-description').text
		playlist_featured = a_element.find('p', 'browse-playlist-featured').text
		playlist_image_url = a_element.find('img', 'browse-playlist-image').get('src')

		for artist in playlist_featured.split(','):
			artist_name = artist.replace('\n', '').replace('w/', '').strip() 
			if artist_name not in featured:
				featured.append(artist_name)

		# TODO: need playlist image url, curator's website url
		playlist_obj = {
							'title': title, 
							'playlist_image_url': playlist_image_url,
							'curator': curator_name, 
							'description': description
						}

		playlists.append(playlist_obj)

	return {	
				'playlists': playlists, 
				'location': location, 
				'bio': bio, 
				'website': website, 
				'featured': featured
			}


def get_curators():
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

					curator_details = get_curator_details(curator_url, curator_name)
					curator_playlist = curator_details['playlists']
					curator_location = curator_details['location']
					curator_bio = curator_details['bio']
					curator_website = curator_details['website']

					featured_artists = curator_details['featured']

					curator_image = get_curator_image(curator_url)

					curator_obj = {
									'name': curator_name, 
									'location': curator_location,
									'featured_artists': featured_artists,
									'bio': curator_bio,
									'website': curator_website,
									'link': curator_url, 
									'playlists': curator_playlist,
									'image_url': curator_image,
									'similar_curators': []
								}

					curators.append(curator_obj)

	return curators

def load_curator_info(curators):
	""" 
		Load curators into Mongo. 
		The curators get saved in a curators called 'curators'.
	"""
	for curator in curators:
		# print "Working on curator {0}".format(curator['curator'])
		curators_coll.insert(curator)


def load_featured_artists(curators):
	""" 
		Load featured artists and the curators that have used them
		into Mongo.
	"""
	for curator in curators:

		for artist in curator['featured_artists']:
			featured_artist_obj = featured_artists_coll.find_one({'name': artist})

			if not featured_artist_obj:
				# make sure I dont have to make a completely new dictionary here
				featured_artist_obj = {}
				featured_artist_obj['name'] = artist
				featured_artist_obj['curators'] = [curator['name']]
				featured_artists_coll.insert(featured_artist_obj)
			else:
				if curator['name'] not in featured_artist_obj['curators']:
					featured_artist_obj['curators'].append(curator['name'])
					featured_artists_coll.update({'name': artist}, featured_artist_obj, upsert=True)


if __name__ == "__main__":
	RUN = True
	if RUN:
		print "Loading Curator information into Mongo"
		curators = get_curators()
		load_curator_info(curators)
		load_featured_artists(curators)
