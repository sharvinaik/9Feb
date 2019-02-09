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

dataset = pd.read_csv(path+"TrainingDataMusic.csv")
connection = MongoClient("localhost", 27017)
db = connection.MovieDatabase
musicTable = db.Music

def musicRecommendation(traits):

    X = dataset.iloc[:, 1: 6].values #TRAITS
    y = dataset.iloc[:, 6: 16].values  #LABELS
    model = tree.DecisionTreeClassifier(criterion='gini')
    model.fit(X, y)

    #Predict on test data
    y_pred = model.predict([traits])
    # print(y_pred)
    #generating musics from genres predicted
    dictionary = {}
    attributesList = dataset.columns.values
    listIndex = 6

    for j in range(0, len(y_pred[0])):
        dictionary.update({attributesList[listIndex] : y_pred[0][j]})
        listIndex = listIndex + 1
    listOfTuples = sorted(dictionary.items(), reverse = True, key = lambda x: x[1])
    i = 1
    musicObject = []
    for e in listOfTuples:
        musicList = []
        if i == 6:
            break
        # print(e[0], " :: ", e[1])
        i += 1
        myquery = {"genre" : e[0]}
        musicNames = musicTable.find(myquery).limit(15)
        
        for music in musicNames:
            musicList.append(music)
            # print(music['title'])
        musicObject.append(musicList)
    return musicObject