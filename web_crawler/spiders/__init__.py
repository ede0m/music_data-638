##############################################################################
# 
#  Music Data Web Scraper using scrapy
#
#  Scrapes every song of every artist on every page of a certain genre
#  Specify page urls for all desired genres in urls list in start_requests
#
#  
#  -- GARRITT MOEDE -- 10/7/16
#


import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from web_crawler.items import WebCrawlerItem
import sys
sys.path.append('../../')
from polite import Polite


class WebSpider(scrapy.Spider):
	name = "music_crawler"
	
	def start_requests(self):
		start_urls = []
		urls = [
	        	# PUT MUSIC GENRES HERE
	        	# 'https://musicbrainz.org/tag/rock/artist?page=1',
	        	# 'https://musicbrainz.org/tag/pop/artist?page=1',
	        	# 'https://musicbrainz.org/tag/electronic/artist?page=1',
	        	
	        	# 'https://musicbrainz.org/tag/jazz/artist?page=1',
	        	# 'https://musicbrainz.org/tag/indie/artist?page=1',
	        	# 'https://musicbrainz.org/tag/folk/artist?page=1',
	        	# 'https://musicbrainz.org/tag/alternative/artist?page=1',
	        	# 'https://musicbrainz.org/tag/hip-hop/artist?page=1',
	        	# 'https://musicbrainz.org/tag/soul/artist?page=1',
	        	

	        	# Country needs to be run alone for some reason?? directory creation error in sequence_genre
	        	# 'https://musicbrainz.org/tag/country/artist?page=1'

	        	#75 PAGES IN FOLLOWING URL. https://musicbrainz.org/tag/punk/artist?page=1


				'https://musicbrainz.org/tag/reggae/artist?page=1',
				'https://musicbrainz.org/tag/dance/artist?page=1',
				'https://musicbrainz.org/tag/funk/artist?page=1',
				'https://musicbrainz.org/tag/ambient/artist?page=1',
				'https://musicbrainz.org/tag/blues/artist?page=1',
				'https://musicbrainz.org/tag/classical/artist?page=1',
		] 
		polite = Polite()
		#for u in urls:
		#	start_urls.append(sequence_genre(u))

		start_urls = polite.sequence_genre(urls)
		for url in start_urls:
	  		yield scrapy.Request(url=url, callback=self.parse_next)


	def parse_next(self, response):
		
		pages = response.xpath('(//ul[@class="pagination"])/li[9]/a/text()').extract() # Will not work for shorter lists
		l_link = response.xpath('(//ul[@class="pagination"])/li[11]/a/@href').extract()
		print('\n',pages,'\n')
		print('\n', l_link ,'\n')
		link = l_link[0]
		total_p = int(pages[0])
		genre = link[28:-14]
		i = 1								# changes from 0 to 1
		while i < total_p: 
			url = 'https://musicbrainz.org/tag/'+genre+'/artist?page='+str(i+1)
			url_l = len(url)
			polite = Polite()
			tmp = []
			tmp.append(url)
			next_page = polite.sequence_genre(tmp)
			i=i+1
			request = scrapy.Request(url=next_page[0], callback=self.parse)
			request.meta['genre'] = genre
			yield request
  	

	def parse(self, response):
		a = Selector(response)
		s = Selector(response)
		urls = a.xpath('(//div[@id="page"]//ul)[3]/li/a/@href').extract()
		artists = s.xpath('(//div[@id="page"]//ul)[3]/li/a/@title').extract()
		polite = Polite()
		for idx, url in enumerate(urls):
			urls[idx]='https://musicbrainz.org' + url

		urls = polite.sequence_artist(urls, artists, response.url)
		for url in urls:
			request = scrapy.Request(url=url, callback=self.parse_artist, dont_filter=True)
			request.meta['genre'] = response.meta['genre']
			yield request


	
	def parse_artist(self, response):
		s = Selector(response)
		artists = Selector(response)
		count = 0
		# Only parse 'Single' table
		headers = response.xpath('//h3/text()').extract()
		tbl_idx = None;
		for i in range(len(headers)):
		 	if headers[i] == 'Single':
		 		print('\n\nFOUND TABLE SINGLE', str(i+1),'\n\n')
		 		tbl_idx = i+1
		 		break
		
		if tbl_idx != None:
			rows = response.xpath('//table['+str(tbl_idx)+']/tbody/tr').extract()
			for j in range(len(rows)):
				year = s.xpath('//table['+str(tbl_idx)+']/tbody/tr['+str(j+1)+']/td[1]/text()').extract()
				song = s.xpath('//table['+str(tbl_idx)+']/tbody/tr['+str(j+1)+']/td[2]/a/bdi/text()').extract()
				print(song,' ', year)
				print('YEAR: ', year[0])
				artist = artists.xpath('//table['+str(tbl_idx)+']/tbody/tr['+str(j+1)+']/td[3]/a/bdi/text()').extract()
				keep = '-'.join(artist)
				item = WebCrawlerItem()
				item['song_year'] = year[0]
				item['song_name'] = song[0]
				item['artist_name'] = keep
				item['genre'] = response.meta['genre']
				count = count+1
				print('\n\n',item,'\n\n')
				yield item
		print('\n NONE FOUND \n')
		return	







