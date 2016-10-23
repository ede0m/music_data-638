#############################################################################
#
#  QUICK CLASS IMPLEMENTATION TO EXTRACT HTML DATA FROM A SPECIFIED URL  
#  AND SAVE IT LOCALLY FOR LOCAL SCAPING. IT WAS ORIGINALLY USED TO AVOID 
#  ROBOT.TXT FLAGS FROM SCRAPY THAT PROHIBITED ACTUAL SCRAPING OVER HTTP 
#
#
#	-- GARRITT MOEDE -- 10/7/16
#


import urllib.request
import shutil
import os

class Polite(object):

	def sequence_genre(self, ulist=[]):
		print(" \n--- starting polite genre extraction  ---\n")
		ret = []
		for url in ulist:
			
			# Correct URL Parsing by ID
			pages = url.split("=")
			if len(pages[1]) > 1:
				string = url[28:-15]
				st_cnt = pages[1]
			else:
				string = url[28:-14]
				st_cnt = url[len(url)-1] 

			# Directory creation
			if not os.path.exists("data/"+string+"/"+string+st_cnt+'/'):
				os.makedirs("data/"+string+"/"+string+st_cnt+'/')
			wd = os.path.dirname(os.path.abspath(__file__))
			fn = wd+"/data/"+string+"/"+string+st_cnt+'/'+string+st_cnt
			if os.path.isfile(fn):
				print('--- file already exists ---') 
			else:
				urllib.request.urlretrieve(url, fn)
			ret.append('file://127.0.0.1'+fn)    #POSSIBLE PATH ERROR
		return ret
	

	def sequence_artist(self, ulist, artists, path):
		print('\n--- starting polite artist extraction ---\n')
		path_l = path.split('/')
		disregard = len(path_l[len(path_l)-2])
		path = path[16:-disregard]
		count = 0;
		ret = []
		for url in ulist:
			artist = artists[count].replace("/", "-")
			artist = artist.replace(" ","_")
			fn = path+artist
			print(fn)
			ret.append('file://127.0.0.1'+fn)
			if os.path.isfile(fn):
				print('--- file already exists ---') 
			else:
				urllib.request.urlretrieve(url, fn)
			count=count+1;	
		return ret



