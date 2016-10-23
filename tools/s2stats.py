##############################################################
#
#	Simple script for stats on CSV music table. 
#   Change data_file_path to point to csv table to analyze 
#
#		Garritt Moede
#
#

import os

data_file_path = "../csv/tables/table_.csv"
fp = os.path.relpath(data_file_path, os.curdir)

av_len_artist = 0
av_len_title = 0
mx_len_artist = 0
mx_len_title = 0

av_tmpo = 0 
av_dur = 0
mx_tmpo = 0
mx_dur = 0

count_dict = {
	"pop":0,
	"rock":0,
	"country":0,
	"electronic":0,
	"indie":0,
	"blues":0,
	"classical":0,
	"hip-hop":0,
	"jazz":0,
	"alternative":0,
	"folk":0
}

genre_miss = 0

with open(fp,'r') as data_file:
	itr = iter(data_file)
	next(itr)
	for i,info in enumerate(itr):
		data = info.split(',')

		artist = data[1]
		title = data[2]
		genre = data[3]
		tempo = float(data[4])
		duration = float(data[5])

		artist_len = len(artist)
		av_len_artist = av_len_artist + artist_len
		title_len = len(title)
		av_len_title = av_len_title + title_len

		if artist_len > mx_len_artist:
			mx_len_artist = artist_len
		elif title_len > mx_len_title:
			mx_len_title = title_len

		av_tmpo = av_tmpo + tempo
		av_dur = av_dur + duration

		if tempo > mx_tmpo:
			mx_tmpo = tempo
		elif duration > mx_dur:
			mx_dur = duration
		try:
			count_dict[genre] += 1
		except KeyError:
			genre_miss+= 1


av_len_artist = av_len_artist / (i+1)
av_len_title = av_len_title / (i+1)
av_tmpo = av_tmpo / (i+1)
av_dur = av_dur / (i+1)


print('\n\nAVG TITLE LEN:  ' , av_len_title)
print('AVG ARTIST LEN: ' , av_len_artist)
print('MX TITLE LEN:   ', mx_len_title)
print('MX ARTIST LEN:  ', mx_len_artist)
print('\n', count_dict )
print('\n  missing_genres: ',genre_miss)
print('\nAVG TEMPO:    ', av_tmpo)
print('AVG DURATION: ', av_dur)
print('MX TEMPO:     ', mx_tmpo)
print('MX DURATION:  ', mx_dur, '\n\n')








