from sklearn.naive_bayes import GaussianNB
from sklearn import metrics, cross_validation
import pandas as pd

df = pd.DataFrame.from_csv("../../csv/training/dev_set.csv")

# Select only the last 4 attributes
features = list(df.columns[2:5])
targets = df['match'].tolist()

# Naive Bayes classifier
nb = GaussianNB()
nb.fit(df[features], targets)

cv_pred = cross_validation.cross_val_predict(nb, df[features], targets, cv=10)

print("\n\n", metrics.accuracy_score(targets, cv_pred))
print("\n\n", metrics.classification_report(targets, cv_pred))

