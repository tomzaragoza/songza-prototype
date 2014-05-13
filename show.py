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
	curator_names.append(curator['name'])

# Recommend 5 curators to each user
for curator in curator_names:
    print "Retrieve top 10 recommendations for Curator", curator
    try:
        client.identify(curator)
        rec = client.get_itemrec_topn("engine1", 10)
        print rec
    except predictionio.ItemRecNotFoundError as e:
        print 'Caught exception:', e.strerror()