from pandas import DataFrame
import os
import subprocess
from sklearn.tree import DecisionTreeClassifier, export_graphviz
df = DataFrame.from_csv("training/dev_set.csv")
features = list(df.columns[2:5])
dt = DecisionTreeClassifier(min_samples_split=100, random_state=99)
tree = dt.fit(df[features], df['match'])

dTestFrame = DataFrame.from_csv("training/eval_set.csv")
output = (tree.predict(dTestFrame[features]))

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