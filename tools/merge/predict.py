from sklearn.model_selection import cross_val_score
from pandas import DataFrame
import numpy
import os
from sklearn import tree
from sklearn import metrics, cross_validation

print("\n\n-- Prediction on Candidates --")

########## BUILD/TRAIN MODEL 
# Train tree on entire sample set
df = DataFrame.from_csv("../../csv/sample_label/feature_vectors.csv")
#Sets the columns of the vectors we use for ML. Does not include ID column.
features = list(df.columns[1:4])
#Build the tree. min_samples_split takes 20 vectors per sample. Seed for random num gen is 99
dt = tree.DecisionTreeClassifier(min_samples_split=20, random_state=99)
#Per vector, learn from the features | the match value of that vector.
t = dt.fit(df[features], df['match'])
# Cross validation metrics in 10 folds 
#cv_pred = cross_validation.cross_val_predict(t, df[features], df['match'], cv=10)
score = cross_validation.cross_val_score(t, df[features], df['match'], cv=10)
print("\nTRAIN on full sample CVS: ",numpy.mean(score),'\n\n')
#print("\n\n", metrics.accuracy_score(df['match'], cv_pred))
#print( metrics.classification_report(df['match'], cv_pred))

################### PREDICT ###########################
#Model was learned above, now apply to unknown data.
dTestFrame = DataFrame.from_csv("../../csv/matching/feature_vectors_full.csv")
output = (t.predict(dTestFrame[features]))

################### MERGE #############################
candidates = DataFrame.from_csv("../../csv/matching/candidates_final.csv")
candidates['match'] = output
dist = candidates.groupby(['match']).size()
matches = candidates.loc[candidates['match'] == 1]
drop_duplicates = matches.drop_duplicates('rtable_ID')  ## THIS LINE IS DROPPING POTENTIAL GENRE DIFFERENCES (MAYBE A STRONGER HEURISTIC HERE)
matches_final = drop_duplicates.drop('match', 1)
matches_final.to_csv('../../csv/matching/matches.csv')










