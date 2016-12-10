import pandas as pd
from pprint import pprint

## A Table Hash Indexes ##
a_table = {}
df_a = pd.DataFrame.from_csv("../../csv/musicbrainz_final.csv")
for index, row in df_a.iterrows():
	if a_table.get(row.name) == None:
		a_table[row.name] = row
print("A Done")

## B Table Hash ##
b_table = {}
df_b = pd.DataFrame.from_csv("../../csv/msd_final.csv")
for index, row in df_b.iterrows():
	if b_table.get(row.name) == None:
		b_table[row.name] = row
print("B Done")


## BEGIN MERGE PROCESS ##
matches = pd.DataFrame.from_csv("../../csv/matching/matches.csv")
golden_tups = []

for index, row in matches.iterrows():
 	## Query Index for each table ##
 	b_id = row['ltable_ID']
 	ser_b = b_table.get(b_id)
 	a_id = row['rtable_ID']
 	
 	ser_a = a_table.get(a_id)
 	
 	## DATA MERGE RULES ###
 	year_b = int(row['ltable_year'])
 	try:
 		year_a = int(row['rtable_year'])
 	except:
 		year_a = 0
 	
 	if year_a != 0 and year_b != 0:
 		if abs(year_b - year_a) > 6:
 			year = 0
 		else:
 			year = min(year_a, year_b)
 	else:
 		year = max(year_a, year_b)

 	title = [row['ltable_title'], row['rtable_title']]
 	title = min(title, key=len)
 	artist = [row['ltable_artist'],row['rtable_artist']]
 	artist = min(artist, key=len)

 	## Extraction of enrichment data
 	genre = ser_a[2]
 	duration = ser_b[3]
 	keysignature = ser_b[4]
 	tempo = ser_b[5]
 	timesignature = ser_b[6]

 	## Construct Golden Dataframe of Matches
 	series = [title, artist, genre, duration, tempo, timesignature, keysignature, year]
 	golden_tups.append(series)


golden = pd.DataFrame(golden_tups, columns = ["title", "artist", "genre", "duration", "tempo", "timesignature", "keysignature", "year"])
golden.to_csv("../../csv/golden.csv")



