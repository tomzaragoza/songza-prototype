from get_curator_info import *
from naive_similarity import *

if __name__ == "__main__":
	RUN = True
	if RUN:
		print "Loading curator and featured artists information into Mongo..."
		curators = get_curators()
		load_curator_info(curators)
		load_featured_artists(curators)

		get_similar_curators()