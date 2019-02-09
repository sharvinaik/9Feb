from __future__ import print_function
import pandas as pd
from sklearn import tree
import tweepy
import time
import os
import json
import sys
from pymongo import MongoClient
from Path import path

dataset = pd.read_csv(path+"TrainingDataMovie.csv")
connection = MongoClient("localhost", 27017)
db = connection.MovieDatabase
movieTable = db.users

def movieRecommendation(traits):

    X = dataset.iloc[:, 1: 6].values #TRAITS
    y = dataset.iloc[:, 6: 16].values  #LABELS

    model = tree.DecisionTreeClassifier(criterion='gini')
    model.fit(X, y)

    #Predict on test data
    y_pred = model.predict([traits])

    #generating movies from genres predicted
    dictionary = {}
    attributesList = dataset.columns.values
    listIndex = 6

    for j in range(0, len(y_pred[0])):
        dictionary.update({attributesList[listIndex] : y_pred[0][j]})
        listIndex = listIndex + 1
    listOfTuples = sorted(dictionary.items(), reverse = True, key = lambda x: x[1])
    i = 1
    movieObject = []
    for e in listOfTuples:
        movieList = []
        if i == 6:
            break
        #print(e[0], " :: ", e[1])
        i += 1
        myquery = {e[0] : "1"}
        
        if e[1] == 2:
            movieNames = movieTable.find(myquery).limit(10)
        elif e[1] == 1:
            movieNames = movieTable.find(myquery).limit(5)
        else:
            movieNames = movieTable.find(myquery).limit(20)
        #movieslist.append(movieNames)
        for movie in movieNames:
            movieList.append(movie)
        movieObject.append(movieList)
    return movieObject