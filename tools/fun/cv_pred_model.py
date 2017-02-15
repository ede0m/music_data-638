from pandas import DataFrame
import numpy
import os
from sklearn import tree
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, cross_validation
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

print(" \n\n -- Model CV Predicition on Golden Data -- \n\n\n")

df = DataFrame.from_csv("../../csv/golden.csv")
## Sample ##
sample = df.sample(n=1500, random_state=123, replace=False)
drop_genre = sample.drop('genre', 1)

## Feature Vectors --- BARE rn
#features1 = list(drop_genre.columns[3:5])

features2 = list(drop_genre.columns[6:])
#features = features1 + features2
print(list(drop_genre.columns[:]))
features = list(drop_genre.columns[3:4])
targets = sample['genre']

print(" Testing Raw Features: ", features, "\n\n\n")
#print(len(drop_genre[features]), len(targets))

## Model Testing ##
dt = tree.DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt = dt.fit(drop_genre[features], targets)
forest = RandomForestClassifier(n_jobs=2)
forest = forest.fit(drop_genre[features], targets)
log_reg = linear_model.LogisticRegression(C=1)
log_reg = log_reg.fit(drop_genre[features], targets)
nb = GaussianNB()
nb = nb.fit(drop_genre[features], targets)
svc = svm.SVC()
svc = svc.fit(drop_genre[features], targets)

## Scoring ##
score_dt = cross_validation.cross_val_score(dt, drop_genre[features], targets, cv=10)
print("\n Tree trained/scored on 2/3 sample. CVS:  ----------------------- ", numpy.mean(score_dt),'\n\n')
dt_pred = cross_validation.cross_val_predict(dt, drop_genre[features], targets, cv=10)
print(" Metrics Accuracy Score: ---------------------------------------- ",metrics.accuracy_score(targets, dt_pred), '\n')
print(metrics.classification_report(targets, dt_pred), "\n")

score_forest = cross_validation.cross_val_score(forest, drop_genre[features], targets, cv=10)
print("\n Forest trained/scored on 2/3 sample. CVS: ---------------------- ", numpy.mean(score_forest),'\n\n')
forest_pred = cross_validation.cross_val_predict(forest, drop_genre[features], targets, cv=10)
print(" Metrics Accuracy Score: ---------------------------------------- ",metrics.accuracy_score(targets, forest_pred), '\n')
print(metrics.classification_report(targets, forest_pred), "\n")

score_log_reg = cross_validation.cross_val_score(log_reg, drop_genre[features], targets, cv=10)
print("\n Logistic Regression trained/scored on 2/3 sample. CVS: --------- ", numpy.mean(score_log_reg),'\n\n')
log_pred = cross_validation.cross_val_predict(log_reg, drop_genre[features], targets, cv=10)
print(" Metrics Accuracy Score: ---------------------------------------- ", metrics.accuracy_score(targets, log_pred), '\n')
print(metrics.classification_report(targets, log_pred), "\n")

score_nb = cross_validation.cross_val_score(nb, drop_genre[features], targets, cv=10)
print("\n Naive Bayes trained/scored on 2/3 sample. CVS: ----------------- ", numpy.mean(score_nb),'\n\n')
nb_pred = cross_validation.cross_val_predict(nb, drop_genre[features], targets, cv=10)
print(" Metrics Accuracy Score: ---------------------------------------- ",metrics.accuracy_score(targets, nb_pred), '\n')
print(metrics.classification_report(targets, nb_pred), "\n")

score_svc = cross_validation.cross_val_score(svc, drop_genre[features], targets, cv=10)
print("\n Support Vector Classifier trained/scored on 2/3 sample: CVS: --- ", numpy.mean(score_svc),'\n\n')
svc_pred = cross_validation.cross_val_predict(svc, drop_genre[features], targets, cv=10)
print(" Metrics Accuracy Score: ---------------------------------------- ", metrics.accuracy_score(targets, svc_pred), '\n')
print(metrics.classification_report(targets, svc_pred), "\n")

