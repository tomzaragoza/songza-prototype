from pymongo import MongoClient
from bs4 import BeautifulSoup
from pprint import pprint
import urllib

client = MongoClient()
db = client['songza']
curators_coll = db['curators']
featured_artists_coll = db['featured_artists']

def get_similar_curators():
	""" 
		A simple, naive, and sadly inefficient way to calculate similar curators.
		Basically, which curators have the most featured artists in common are
		considered similar curators.

	"""
	curators = list(curators_coll.find())
	curator_names = [curator['name'] for curator in curators]
	compare_names = [curator['name'] for curator in curators]

	# this is the ugliest thing I've ever written
	for name in curator_names:

		curator_similar_counts = []
		compare_names.remove(name)
		for compare_name in compare_names:

			similar_count = 0

			for artist in featured_artists_coll.find():
				if name in artist['curators'] and compare_name in artist['curators']:

					similar_count += 1

			if similar_count > 0:
				curator_similar_counts.append((similar_count, compare_name))
		
		curators_coll.update({'name': name}, {'$set': {'similar_curators': curator_similar_counts}})


if __name__ == "__main__":
	get_similar_curators()