import os, sys, csv

count = 0

with open("../csv/musicbrainz_old.csv") as csvfile, open("musicbrainz_clean_st3.csv", "w") as out:
    csvreader = csv.reader(csvfile)
    csvwriter = csv.writer(out)
    for row in csvreader:
        ## split = row.split(",")
        if len(row) == 4:
            csvwriter.writerow(row)
        else:
        	count+=1

print('Removed ', count, ' tuples\n')

