import json
import sys
import re

usable_data = open("../csv/usable_data.csv", 'w')
empty = 0
bad_char = 0 

with open('data_merge.json', encoding='utf-8') as dfile:
	data = json.load(dfile)

usable_data.write("ID, Artist, Song, Genre\n")

for i, item in enumerate(data):
	artist = data[i]['artist_name']
	song = data[i]['song_name']
	genre = data[i]['genre']

	if(artist == "" or song == ""):
		empty = empty + 1
	else:
		# Handle non-latin characters
		if re.findall(u"[\u3300-\u33ff]+", song) or re.findall(u"[\u3300-\u33ff]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\ufe30-\ufe4f]+", song) or re.findall(u"[\ufe30-\ufe4f]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\uf900-\ufaff]+", song) or re.findall(u"[\uf900-\ufaff]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\U0002F800-\U0002fa1f]+", song) or re.findall(u"[\U0002F800-\U0002fa1f]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\u30a0-\u30ff]+", song) or re.findall(u"[\u30a0-\u30ff]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\u2e80-\u2eff]+", song) or re.findall(u"[\u2e80-\u2eff]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\u4e00-\u9fff]+", song) or re.findall(u"[\u4e00-\u9fff]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\u3400-\u4dbf]+", song) or re.findall(u"[\u3400-\u4dbf]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\U00020000-\U0002a6df]+", song) or re.findall(u"[\U00020000-\U0002a6df]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\U0002a700-\U0002b73f]+", song) or re.findall(u"[\U0002a700-\U0002b73f]+", artist):
			bad_char = bad_char + 1
		elif re.findall(u"[\U0002b740-\U0002b81f]+", song) or re.findall(u"[\U0002b740-\U0002b81f]+", artist):
			bad_char = bad_char + 1
		else:
			usable_data.write(str(i) + "," + str(artist) + "," + str(song) + "," + str(genre)+"\n")

print('\nRemoved ', bad_char, ' examples because of characters\n')
print('Removed ', empty, ' empty examples\n')
print('Data points traversed: ', i, '\n')