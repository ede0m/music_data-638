from pandas import DataFrame
import os
import subprocess
from sklearn.tree import DecisionTreeClassifier



#Dev set to set up tree.
df = DataFrame.from_csv("training/dev_set.csv")


#Sets the columns of the vectors we use for ML. Does not include ID column.
#id,atable_id,btable_id,sim_title,sim_artist,dif_year,match
#ID is ignored because DataFram.from_csv defaults to having the first column as the ID column. 
#atable_id, btable_id ignored in the following line. Match ignored in the following line because the 2:5 is inclusive:exclusive
features = list(df.columns[2:5])


#Build the tree. min_samples_split takes 20 vectors per sample. Seed for random num gen is 99
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

#Per vector, learn from the features | the match value of that vector.
tree = dt.fit(df[features], df['match'])


#Model was learned above, now apply to unknown data.
dTestFrame = DataFrame.from_csv("training/eval_set.csv")
output = (tree.predict(dTestFrame[features]))



#Evaluating the results. 
eval_results = []
with open("training/eval_set.csv", 'r') as f:
	for line in f:
		eval_results.append(line.split(",")[-1])
for i, val in enumerate(eval_results):
	eval_results[i] = val.replace("\n", "")
eval_results = eval_results[1:]



correct = 0
incorrect = len(eval_results)
for i, val in enumerate(output):
	if(val == eval_results[i]):
		correct = correct + 1
print("Correct: " + str(correct))
print("Accuracy: " + str(correct / incorrect))