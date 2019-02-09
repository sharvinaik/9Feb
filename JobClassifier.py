from __future__ import print_function
import pandas as pd
from sklearn import tree
import tweepy
import time
import os
import json
import sys

from Path import path

dataset = pd.read_csv(path+"TrainingDataJob.csv")

def jobRecommendation(traits):
    #split our dataset into its attributes and labels.

    X = dataset.iloc[:, 1: 6].values #TRAITS
    y = dataset.iloc[:, 6:28].values  #LABELS

    model = tree.DecisionTreeClassifier(criterion='gini')
    model.fit(X, y)

    #Predict on test data

    y_pred = model.predict([traits])
    dictionary = {}
    attributesList = dataset.columns.values
    listIndex = 6

    for j in range(0, len(y_pred[0])):
        dictionary.update({attributesList[listIndex] : y_pred[0][j]})
        listIndex = listIndex + 1
    listOfTuples = sorted(dictionary.items(), reverse = True, key = lambda x: x[1])
    return listOfTuples[0:7]