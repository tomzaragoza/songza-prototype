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

for curator in collection.find():
	# User Data
	client.create_user(curator['name'])
	
	# Item data
	for playlist in curator['playlists']:

		# 1 indicates item type ID, in this case, a playlist
		client.create_item(playlist['title'], ('1',))

		# Record that the current curator made this playlist
		client.identify(curator['name'])
		client.record_action_on_item('like', playlist['title'])

client.close()