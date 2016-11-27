import os

data_file_path_1 = "../../csv/MSD/msd_full.csv"
fp = os.path.relpath(data_file_path_1, os.curdir)

table_B = open("../../csv/msd_final_2.csv", 'w')
table_B.write("ID,album,artist,danceability,duration,keysignature,tempo,timesignature,title,year\n")


with open(fp,'r') as data_file:

	for i, info in enumerate(data_file):

		data = info.split(',')
		try:
			title = data[8]
			artist = data[2]
			album = data[1]
		except:
			print("Removed\n")
		
		title = title.replace("\"b'", "")
		title = title.replace("\"b\"", "")
		title = title.replace("'\"", "")		
		title = title.replace("\"\"", "")

		artist = artist.replace("\"b'", "")
		artist = artist.replace("\"b\"", "")
		artist = artist.replace("'\"", "")		
		artist = artist.replace("\"\"", "")

		album = album.replace("\"b'", "")
		album = album.replace("\"b\"", "")
		album = album.replace("'\"", "")		
		album = album.replace("\"\"", "")

		try:
			table_B.write("b" + str(i) + "," + album + "," + artist + "," + data[3] + "," +
			data[4] + "," + data[5] + "," + data[6] + "," + data[7] + "," + title + "," + data[9])
		except:
			print("Removed\n")
