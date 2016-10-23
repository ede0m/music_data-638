##############################################################
#
#	Simple script for stats on CSV music table. 
#   Change data_file_path to point to csv table to analyze 
#
#		Garritt Moede
#
#
import matplotlib.pyplot as plt
import os

data_file_path = "../csv/tables/table_merge.csv"
fp = os.path.relpath(data_file_path, os.curdir)

av_len_artist = 0
av_len_title = 0
mx_len_artist = 0
mx_len_title = 0
mn_len_artist = 1000
mn_len_title = 1000

len_artist_array = []
len_title_array = []

av_tmpo = 0 
av_dur = 0
mx_tmpo = 0
mx_dur = 0
mn_tmpo = 1000
mn_dur = 1000

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

		artist = data[0]
		title = data[1]
		genre = data[2]
		tempo = float(data[3])
		duration = float(data[4])

		artist_len = len(artist)

		len_artist_array.append(artist_len)


		av_len_artist = av_len_artist + artist_len
		title_len = len(title)
		av_len_title = av_len_title + title_len

		len_title_array.append(title_len)

		if artist_len > mx_len_artist:
			mx_len_artist = artist_len
		if title_len > mx_len_title:
			mx_len_title = title_len
		#####
		if artist_len < mn_len_artist:
			mn_len_artist = artist_len
		if title_len < mn_len_title:
			mn_len_title = title_len

		av_tmpo = av_tmpo + tempo
		av_dur = av_dur + duration

		if tempo > mx_tmpo:
			mx_tmpo = tempo
		if tempo < mn_tmpo:
			mn_tmpo = tempo
		if duration > mx_dur:
			mx_dur = duration
		if duration < mn_dur:
			mn_dur = duration
		try:
			count_dict[genre] += 1
		except KeyError:
			genre_miss+= 1


av_len_artist = av_len_artist / (i+1)
av_len_title = av_len_title / (i+1)
av_tmpo = av_tmpo / (i+1)
av_dur = av_dur / (i+1)

len_title_array.sort()
len_artist_array.sort()

quartile1Title = len_title_array[len(len_title_array) //4]
quartile1Artist = len_artist_array[len(len_artist_array) // 4]

quartile3Title = len_title_array[(len(len_title_array) // 4) * 3]
quartile3Artist = len_artist_array[(len(len_artist_array) // 4) * 3]

medianTitle = len_title_array[len(len_title_array) // 2]
medianArtist = len_artist_array[len(len_artist_array) // 2]


print('\n\nAVG ARTIST LEN: ', av_len_artist)
print('MX ARTIST LEN:  ', mx_len_artist)
print('MN ARTIST LEN:  ', mn_len_artist)
print('\n\nAVG TITLE LEN:  ' , av_len_title)
print('MX TITLE LEN:   ', mx_len_title)
print('MN TITLE LEN:   ', mn_len_title)

print('\n', count_dict )
print('\nmissing_genres: ',genre_miss)
print('\nAVG TEMPO:    ', av_tmpo)
print('AVG DURATION: ', av_dur)
print('MX TEMPO:     ', mx_tmpo)
print('MX DURATION:  ', mx_dur, '\n\n')

print("\nQ1 Title Length: ", quartile1Title)
print("Q3 Title Length: ", quartile3Title)

print("\nQ1 Artist Length: ", quartile1Artist)
print("Q3 Artist Length: ", quartile3Artist)


#Uncomment each one you want to show. If you uncomment multiple the code hangs until
#you close the tkinter window.

# BINS_Title = list(range(0,40))
# plt.hist(len_title_array,bins = BINS_Title)
# plt.xlabel("Song Title Length in Characters")
# plt.ylabel("Instances")
# plt.title("Histogram Song Title Length")
# plt.show()


# BINS_Artist = list(range(0,55))
# plt.hist(len_artist_array, bins = BINS_Artist)
# plt.xlabel("Artist Length in Characters")
# plt.ylabel("Instances")
# plt.title("Histogram Artist Length")
# plt.show()

plt.bar(range(len(count_dict)), count_dict.values(), align='center')
plt.xticks(range(len(count_dict)), count_dict.keys())
plt.title("Bar Chart of Genres")
plt.xlabel("Genre")
plt.ylabel("Instance of Genre")
plt.show()
