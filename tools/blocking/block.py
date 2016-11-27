import os
import pprint

path_msd = os.path.join(os.getcwd(), "../../csv/msd_final.csv" )
path_musicbrainz = path_b = os.path.join(os.getcwd(), "../../csv/musicbrainz_final.csv")
invert_idx = {}

# Construct inverted index. String Tokens
with open(path_msd, 'r') as data_file:
    itr = iter(data_file)
    next(itr)
    for i, line in enumerate(itr):
        data = line.split(",")
        ID = data[0]
        artist = data[2]
        prefix = artist[:2]
        if invert_idx.get(prefix) == None:
            invert_idx[prefix] = {}
            invert_idx[prefix][ID] = artist
        else:
            invert_idx[prefix][ID] = artist

pprint.pprint(invert_idx)

#with open(path_musicbrainz, 'r') as data_file:
#	itr = iter(data_file)
#	next(itr)
#	for i, line in enumerate(itr)
#		data = line.split(",")



