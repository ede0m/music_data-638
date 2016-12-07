## Feature Generation for learning based entity matching ## 
import py_stringmatching as sm
import pandas as pd
import os, sys

feature_vectors = open('../../csv/matching/feature_vectors_full.csv', 'w')


gram3 = sm.QgramTokenizer(qval=3, return_set=True)
jac = sm.Jaccard()
feature_vectors.write('atable_id,btable_id,sim_title,sim_artist,dif_year\n')
ID = 0

with open('../../csv/matching/candidates_final.csv', 'r', encoding='utf-8', errors='ignore') as data_file:
#with open('../../csv/sample_label/200/sample2.csv', 'r', encoding='utf-8', errors='ignore') as data_file:
	itr = iter(data_file)
	next(itr)
	for i, row in enumerate(itr):
		
		row_data = row.split(',')	
		b_t = row_data[1][1:]
		a_t = row_data[2][1:]
		l_artist = row_data[4]
		r_artist = row_data[7]
		l_title = row_data[3]
		r_title = row_data[6]
		l_year = row_data[5]
		r_year = row_data[8] 
		sim_artist = jac.get_raw_score(gram3.tokenize(l_artist), gram3.tokenize(r_artist))
		sim_title = jac.get_raw_score(gram3.tokenize(l_title), gram3.tokenize(r_title))
		sim_artist = ("%.4f" % sim_artist)
		sim_title = ("%.4f" % sim_title)

		if r_year == '—\n':
			print("- converted right table year -")
			r_year = 0
		
		if float(r_year) != 0 and float(l_year) != 0: 
			year_distance = abs(float(l_year) - float(r_year))
		else:
			year_distance = -1
	
		feature_vectors.write(a_t+","+b_t+","+str(sim_title)+','+str(sim_artist)+','+str(year_distance)+"\n")
		ID+=1
		

feature_vectors.close()

