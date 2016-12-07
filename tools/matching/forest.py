from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, cross_validation
import pandas as pd
import numpy

print("-- Forest --")

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

cv_eval = cross_validation.cross_val_score(forest, dTestFrame[features], dTestFrame['match'], cv=10)
print("\nEVAL: cvs: ",numpy.mean(score),"\n\n")
