import os

data_file_path_1 = "../csv/msd_merge.csv"
fp = os.path.relpath(data_file_path_1, os.curdir)

table_B = open("../csv/msd_final.csv", 'w')
table_B.write("ID, Album, Artist, Danceability, Danceability, KeySignature, Tempo, TimeSignature, Title, Year\n", )


with open(fp,'r') as data_file:

	for i, info in enumerate(data_file):

		data = info.split(',')
		title = data[8]
		artist = data[2]
		album = data[1]
		#if title.find("\\x") or artist.find("\\x") or album.find("\\x") != -1:
		#	continue

		# change! this may be replacing any b characters 
		title = title.replace("b","")
		title = title.replace("\"", "")
		title = title.replace("\'","")
		artist = artist.replace("b","")
		artist = artist.replace("\"", "")
		artist = artist.replace("\'","")
		album = album.replace("b","")
		album = album.replace("\"", "")
		album = album.replace("\'","")

		table_B.write("b" + str(i) + "," + album + "," + artist + "," + data[3] + "," +
			 data[4] + "," + data[5] + "," + data[6] + "," + data[7] + "," + title + "," + data[9])
