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
	curator_names.append({'name': curator['name'], 'featured_artists':curator['featured_artists']})

# Recommend 5 curators to each user
for curator in curator_names:
	print "====================================================="
	print "Retrieve for", curator
	try:
		client.identify(curator['name'])
		for artist in curator['featured_artists']:
			rec = client.get_itemsim_topn("engine2", artist, 10)
			print rec
		# rec = client.get_itemrec_topn("engine1", 5)
		# print rec
	except predictionio.ItemRecNotFoundError as e:
		print 'Caught exception:', e.strerror()