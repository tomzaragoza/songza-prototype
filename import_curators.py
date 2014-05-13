import predictionio
from pymongo import MongoClient

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

client = predictionio.Client(appkey="pEkluvus5TXkyO6MR9t4HDRDq4ZkXLLigaG7hXckIVRDfwRxTfFiTSh3YvgQQ8uR")

mongo = MongoClient()
db = mongo['songza']
collection = db['curators']

curator_names = []



artist_used = {}

for curator in collection.find():
	# User Data
	client.create_user(curator['name'])
	
	# Item data
	print "Loading featured artists for {0}...".format(curator['name'])

	for featured_artist in curator['featured_artists']:
		# if featured_artist not in artist_used:
		#	artist_used[featured_artist] = True

		client.create_item(featured_artist, ('featured_artist',)) # recommend similar artists
		# client.create_item(curator['name'], ('curator',)) # recommend similar curators

		# Record that the current curator made this playlist with a certain artist, "liked"
		client.identify(curator['name'])
		client.record_action_on_item('like', featured_artist)

		# else: # just to see if there are any overlapping featured artists
		# 	print featured_artist, "USED"


client.close()
