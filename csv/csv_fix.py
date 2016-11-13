import os, sys, csv

print("here")
with open("musicbrainz_final.csv") as csvfile, open("csv_out.csv", "w") as out:
    csvreader = csv.reader(csvfile)
    csvwriter = csv.writer(out)
    for row in csvreader:
        ## split = row.split(",")
        if len(row) == 4:
            csvwriter.writerow(row)

