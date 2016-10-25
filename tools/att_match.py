##############################################################
#	
#   Script for merging matches from scraped csv table 
#   and data_dump csv. The merged table combines valuable  
# 	attributes from both tables to form 
#
#	This script also takes some stats on table data
#   
#   Garritt Moede
#


import os


#data_file_path_1 = "../csv/dump_CSV_sample.csv"
data_file_path_1 = "../csv/MSD/msd_6.csv"
fp = os.path.relpath(data_file_path_1, os.curdir)

data_file_path_2 = "../csv/usable_data.csv"
fp2 = os.path.relpath(data_file_path_2, os.curdir)

matches = 0
usable_data = {}
table_A = open("../csv/tables/table_6.csv", 'w')
table_A.write("Artist, Song, Genre, Tempo, Duration\n")

with open(fp2,'r') as data_file:
	for i,info in enumerate(data_file):
		data = info.split(',')
		title = data[2]
		genre = data[3]
		usable_data[title] = genre


## TY FOR NOT HITTING WORST CASE, WHY IS THIS AS FAST AS IT IS?

with open(fp,'r') as data_file:

	for i,info in enumerate(data_file):

		data = info.split(',')
		title = data[8]
		title = title.replace("b","")
		title = title.replace("\"", "")
		title = title.replace("\'","")
		
		genre = usable_data.get(title)

		if genre != None:
			matches = matches + 1
			artist = data[2].replace("b","")
			artist = artist.replace("\"", "")
			artist = artist.replace("\'", "")
			artist = artist.split("/")[0]
			duration = data[4]
			tempo = data[6]
			genre = genre.replace("\n","")
			string = str(matches)+",  "+artist+",  "+title+",  "+genre+",  "+tempo+",  "+duration+"\n"
			print(string)
			table_A.write(artist+","+title+","+genre+","+tempo+","+duration+"\n")

