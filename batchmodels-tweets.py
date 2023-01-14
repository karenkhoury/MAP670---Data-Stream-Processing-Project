'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score, KFold
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
'''
In this script, we predict the sentiment of the tweets saved in the 'archive.csv' file 
using batch models from sklearn.
'''

## Load the 'archive.csv' file
df = pd.read_csv('archive.csv', sep=';')
## Load X and y
X = df[['Tweet', 'Language']]
y = df['Sentiment']

## Create a TF-IDF
vectorizer = TfidfVectorizer (max_features=2000, min_df=7, max_df=0.8)
processed_features = vectorizer.fit_transform(np.array(X['Tweet'].astype('U'))).toarray()

## Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_features, y, test_size=0.20)


## Create a Random Forest Classifier
param_grid = {'n_estimators':[ 10, 50, 100, 200]}
cv = KFold(n_splits=10, shuffle=True)
## Create a grid search object
grid = GridSearchCV(RandomForestClassifier(), param_grid=param_grid, cv=cv)
result = grid.fit(X_train, y_train)
## Get the best parameters
n_estimators = result.best_params_['n_estimators']
## Create a Random Forest Classifier with the best parameters
RF = RandomForestClassifier(n_estimators=n_estimators)
RF.fit(X_train, y_train)
predictions = RF.predict(X_test)

print('Random Forest')
print('Confusion matrix')
print(confusion_matrix(y_test,predictions))
print('Classification report')
print(classification_report(y_test,predictions))
print('Accuracy score', accuracy_score(y_test, predictions))
print('---------------------------------------------------------------------------------')

## Create a Logistic Regression Classifier
param_grid = {'solver':['liblinear', 'saga', 'newton-cg']}
cv = KFold(n_splits=10, shuffle=True)
## Create a grid search object
grid = GridSearchCV(LogisticRegression(), param_grid=param_grid, cv=cv)
result = grid.fit(X_train, y_train)
## Get the best parameters
solver  = result.best_params_['solver']
## Create a Logistic Regression Classifier with the best parameters
LR = LogisticRegression(solver=solver)
LR.fit(X_train, y_train)
predictions = LR.predict(X_test)

print('Logistic Regression')
print('Confusion matrix')
print(confusion_matrix(y_test,predictions))
print('Classification report')
print(classification_report(y_test,predictions))
print('Accuracy score', accuracy_score(y_test, predictions))
print('---------------------------------------------------------------------------------')

## Create a Naive Bayes Classifier
gnb = GaussianNB()
gnb.fit(X_train, y_train)
predictions = gnb.predict(X_test)

print('Naive Bayes')
print('Confusion matrix')
print(confusion_matrix(y_test,predictions))
print('Classification report')
print(classification_report(y_test,predictions))
print('Accuracy score', accuracy_score(y_test, predictions))
print('---------------------------------------------------------------------------------')

