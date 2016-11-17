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

data_file_path_1 = "../csv/msd_final.csv"
fp = os.path.relpath(data_file_path_1, os.curdir)

data_file_path_2 = "../csv/musicbrainz_final.csv"
fp2 = os.path.relpath(data_file_path_2, os.curdir)

matches = 0
usable_data = {}
table_A = open("../csv/tables/candidate.csv", 'w')
table_A.write("ID, Artist, Song, Genre, Tempo, Duration\n")

with open(fp2,'r') as data_file:
	for i,info in enumerate(data_file):
		data = info.split(',')
		title = data[2]
		genre = data[3]
		usable_data[title] = genre


with open(fp,'r') as data_file:

	for i,info in enumerate(data_file):

		data = info.split(',')
		title = data[8]
		
		genre = usable_data.get(title)

		if genre != None:
			matches = matches + 1
			artist = artist.split("/")[0]
			duration = data[4]
			tempo = data[6]
			genre = genre.replace("\n","")
			string = str(matches)+",  "+artist+",  "+title+", " + genre+",  "+tempo+",  "+duration+"\n"
			print(string)
			table_A.write(artist+","+title+","+genre+","+tempo+","+duration+"\n")

