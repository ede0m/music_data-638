## Feature Generation for learning based entity matching ## 

import py_stringmatching as sm
import pandas as pd
import os, sys

#sample = pd.read_csv('../../csv/sample_label/303/sample.csv')

feature_vectors = open('../../csv/feature_vectors.csv', 'w')


gram3 = sm.QgramTokenizer(qval=3, return_set=True)
jac = sm.Jaccard()
feature_vectors.write('atable_id,btable_id,sim_title,sim_artist,dif_year,match\n')
ID = 0
empty = "-"

with open('../../csv/sample_label/303/sample.csv', 'r', encoding='utf-8', errors='ignore') as data_file:
	itr = iter(data_file)
	next(itr)
	
	for i, row in enumerate(itr):
		
		row_data = row.split(',')

		if row_data[10] != "-":	
			
			b_t = row_data[2][1:]
			a_t = row_data[3][1:]
			l_artist = row_data[5] #row['ltable_artist']
			r_artist = row_data[8] #row['rtable_aritst']
			l_title = row_data[4] #row['ltable_title']
			r_title = row_data[7] #row['rtable_title']
			l_year = row_data[6] #row['ltable_year']
			r_year = row_data[9] #row['rtable_year']

			sim_artist = jac.get_raw_score(gram3.tokenize(l_artist), gram3.tokenize(r_artist))
			sim_title = jac.get_raw_score(gram3.tokenize(l_title), gram3.tokenize(r_title))
			sim_artist = ("%.3f" % sim_artist)
			sim_title = ("%.3f" % sim_title)
			
			#print(row_data)

			if r_year == "-":
				print("- converted right table year -")
				r_year = 0

			
			if float(r_year) != 0 and float(l_year) != 0: 
				year_distance = abs(float(l_year) - float(r_year))
			else:
				year_distance = -1
		
			feature_vectors.write(a_t+","+b_t+","+str(sim_title)+','+str(sim_artist)+','+str(year_distance)+','+str(row_data[10]))
			ID+=1
		
		else:
			print("- disregarded row -")

feature_vectors.close()

fv = pd.read_csv('../../csv/feature_vectors.csv')
dev_set = fv.sample(n=264, random_state=303, replace=False)
eval_set = fv.sample(n=132, random_state=303, replace=False)

dev_set.to_csv('../../csv/training/dev_set.csv')
eval_set.to_csv('../../csv/training/eval_set.csv')


