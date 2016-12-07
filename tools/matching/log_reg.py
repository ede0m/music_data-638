from sklearn import linear_model
from sklearn import metrics, cross_validation
import pandas as pd
import numpy

print("-- LOG --")

df = pd.DataFrame.from_csv("../../csv/training/dev_set.csv")

# Select only the last 4 attributes
features = list(df.columns[2:5])
targets = df['match'].tolist()

# Logisitic Regression 
log_reg = linear_model.LogisticRegression(C=1)
log_reg.fit(df[features], targets)

# cv_pred = cross_validation.cross_val_predict(log_reg, df[features], targets, cv=10)
# print("\n\n", metrics.accuracy_score(targets, cv_pred))
# print("\n\n", metrics.classification_report(targets, cv_pred))

score = cross_validation.cross_val_score(log_reg, df[features], targets, cv=10)
print("\n\nTRAIN cvs: ",numpy.mean(score))


#Model was learned above, now apply to unknown data.
dTestFrame = pd.DataFrame.from_csv("../../csv/training/eval_set.csv")
#print(dTestFrame)
output = (log_reg.predict(dTestFrame[features]))


score = cross_validation.cross_val_score(log_reg, dTestFrame[features], dTestFrame['match'], cv=10)
print("\nEVAL cvs: ",numpy.mean(score),'\n\n')







