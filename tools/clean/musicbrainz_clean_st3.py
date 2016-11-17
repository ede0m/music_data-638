import os, sys, csv

count = 0

with open("../../csv/musicbrainz_data_plusyear.csv") as csvfile, open("musicbrainz_clean_st3_plusyear.csv", "w") as out:
    csvreader = csv.reader(csvfile)
    csvwriter = csv.writer(out)
    for row in csvreader:
        print(row)
        ## split = row.split(",")
        if len(row) == 5:
            csvwriter.writerow(row)
        else:
        	count+=1

print('Removed ', count, ' tuples\n')

