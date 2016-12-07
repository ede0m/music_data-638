from sklearn.naive_bayes import GaussianNB
from sklearn import metrics, cross_validation
import pandas as pd
import numpy

print("-- Naive Bayes --")

df = pd.DataFrame.from_csv("../../csv/training/dev_set.csv")

# Select only the last 4 attributes
features = list(df.columns[2:5])
targets = df['match'].tolist()

# Naive Bayes classifier
nb = GaussianNB()
nb.fit(df[features], targets)

score = cross_validation.cross_val_score(nb, df[features], targets, cv=10)
print("\n\nTRAIN cvs: ",numpy.mean(score))
# cv_pred = cross_validation.cross_val_predict(nb, df[features], targets, cv=10)
# print("\nTRAINED ON DEV SET\n", metrics.accuracy_score(targets, cv_pred))
# print("\n\n", metrics.classification_report(targets, cv_pred))

###############################################################################
#Model was learned above, now apply to unknown data.
dTestFrame = pd.DataFrame.from_csv("../../csv/training/eval_set.csv")
#print(dTestFrame)
output = (nb.predict(dTestFrame[features]))

score = cross_validation.cross_val_score(nb, dTestFrame[features], dTestFrame['match'], cv=10)
print("\nEVAL cvs: ", numpy.mean(score),'\n\n')



