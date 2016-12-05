from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, cross_validation
import pandas as pd
import numpy

df = pd.DataFrame.from_csv("../../csv/training/dev_set.csv")

# Select only the last 4 attributes
features = list(df.columns[2:5])
targets = df['match'].tolist()

# RandomForestClassifier
forest = RandomForestClassifier(n_jobs=2)
forest.fit(df[features], targets)

#cv_pred = cross_validation.cross_val_predict(forest, df[features], targets, cv=10)
score = cross_validation.cross_val_score(forest, df[features], targets, cv=10)
print("\n\nTRAIN cvs: ",numpy.mean(score))
# print("\n\n", metrics.accuracy_score(targets, cv_pred))
# print("\n\n", metrics.classification_report(targets, cv_pred))


#Model was learned above, now apply to unknown data.
dTestFrame = pd.DataFrame.from_csv("../../csv/training/eval_set.csv")
#print(dTestFrame)
output = (forest.predict(dTestFrame[features]))

# # Check golden labels 
# g_labels = []
# with open("../../csv/training/eval_set.csv", 'r') as f:
# 	for line in f:
# 		g_labels.append(line.split(",")[-1])
# for i, val in enumerate(g_labels):
# 	g_labels[i] = val.replace("\n", "")
# 	print(g_labels)
# g_labels = g_labels[1:]

# correct = 0
# # Evaluate predictions
# total = len(g_labels)
# for i, val in enumerate(output):
# 	pred = int(val)
# 	true = int(g_labels[i])
# 	#print(pred, " ", true)
# 	if pred is true:
# 		correct = correct + 1
# 	else:
# 		print(pred, " ", true)
# 		print()

# print("Correct: " + str(correct))
# print("N_accuracy: " + str(correct / total))

# cv_pred_eval = cross_validation.cross_val_predict(forest, dTestFrame[features], dTestFrame['match'], cv=10)
# print("\n\n", metrics.accuracy_score(dTestFrame['match'], cv_pred_eval))
# print("\n\n", metrics.classification_report(dTestFrame['match'], cv_pred_eval))

cv_eval = cross_validation.cross_val_score(forest, dTestFrame[features], dTestFrame['match'], cv=10)
print("\nEVAL: cvs: ",numpy.mean(score),"\n\n")
