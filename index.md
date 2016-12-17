# STAGE 4 DELIVERABLE: 

[(っ◕‿◕)っ **** _P_D_F_ ](https://github.com/Garritt/music_data-638/blob/master/visual_other/matching.pdf)  

[Golden Data](https://github.com/Garritt/music_data-638/blob/master/csv/sample_label/303/sample.csv)  
[Godlen_Data Sample 2](https://github.com/Garritt/music_data-638/blob/master/csv/sample_label/200/sample2.csv) 

---------------------------
---------------------------  
  
  
#PIPELINE:  
  


## Data Acquisition
-----------------
Used _scrapy_ to extract music data from [https://musicbrainz.org/](https://musicbrainz.org/). For this site we focused on song attributes including **genre**, **title** and **artist**. 


  * [musicbrainz_scrape.csv](https://github.com/Garritt/music_data-638/blob/master/csv/usable_data.csv)  
  * [html data](https://github.com/Garritt/music_data-638/tree/master/data)

Data was acquired from [http://labrosa.ee.columbia.edu/millionsong/](http://labrosa.ee.columbia.edu/millionsong/)  
focusing on attributes **artist**, **song_title**, **tempo**, **duration** and **key**

  * [dump](https://github.com/Garritt/music_data-638/tree/master/csv/MSD)


## Cleaning
------------------------------------------------------------
Empty values and non-ascii characters were removed from **musicbrainz** data.  

   - removed _912_ examples for character encoding and malformed data  
   - removed _12690_ examples for missing data
   - removed _390_ examples because of extra attributes (songs contained ",")  
   - traversed _33144_ examples total    
  
Modify csv string data format from **dump** Data  
   - specifically removed _"'b_ characters 



## Exploration 
------------------------------
run this [tool](https://github.com/Garritt/music_data-638/blob/master/tools/s2stats.py) on individual tables for data attribute type statistics and figures. 
  
peek our [visuals](https://github.com/Garritt/music_data-638/tree/master/visual)  

### Aggregated Statistics
 

{'indie': 321, 'jazz': 571, 'alternative': 1378, 'blues': 126, 'country': 127, 'rock': 2831, 'electronic': 2643, 'classical': 270, 'folk': 1051, 'pop': 1923, 'hip-hop': 1207}

missing_genres:  313  
points iterated: 12761  

AVG ARTIST LEN:  12.632630671577463  
MED ARTIST LEN:      12  
MX ARTIST LEN:   273  
MN ARTIST LEN:   1  
Q1 ARTIST LEN:   9  
Q3 ARTIST LEN:   15  
  
AVG TITLE LEN:   9.019042394796646  
MED TITLE LEN:       8  
MX TITLE LEN:    45  
MN TITLE LEN:    1  
Q1 Title Length:  6  
Q3 Title Length:  11  
  
AVG TEMPO:     123.85006480683292  
MED TEMPO:       123.495  
MX TEMPO:      252.062  
MN TEMPO:      0.0  
Q1 TEMPO:      99.59  
Q3 TEMPO:      141.956  
  
AVG DURATION:  256.03759166601264  
MED DURATION:    236.93016  
MX DURATION:   2569.01179  
MN DURATION:   0.60036  
Q1 DURATION:   193.98485  
Q3 DURATION:   297.40363  


## Blocking
------------------------------------

We reduced the number of candidates from a massive __6,651,032,474__ possible matches to __50,109__ possible matches.

We explored a few different blocking techniques, but ultimately followed our best measure as a Jaccard Score with 3 gram tokenization across song TITLE and a threshold of (.7). This resulted in our [candidate set](https://raw.githubusercontent.com/Garritt/music_data-638/master/csv/candidate_set.csv).

  
## Contributors  
  
  Evan Kivolowitz -- evan.kivolowitz@wisc.edu  
  Garritt Moede -- gmoede@wisc.edu  
  Cormick Hnilicka -- cvhnilicka@wisc.edu  