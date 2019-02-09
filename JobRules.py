import pandas as pd
from Path import path
dataframe = pd.read_csv(path+"TrainingDataJob.csv")

listOfAttributes = ['TopExecutive','Fundraiser','SalesManager','EventPlanner','Lawyer','PublicWelfare','Librarian','Writer','Nutritionist','GraphicsDesigner',
                      'Masseuse','Marketting','Archeologist','Actor','Director','Artist','Cosmetologist','HumanResource','CustomerRelationshipManager',
                      'Nurse','HealthCounselor','Professor']

opennessJobs = ['Writer', 'Marketting', 'Archeologist', 'Actor', 'Director', 'Artist', 'GraphicsDesigner']
conscientiounessJobs = ['TopExecutive', 'Fundraiser', 'SalesManager', 'EventPlanner', 'Lawyer', 'PublicWelfare']
extraversionJobs = ['Cosmetologist', 'CustomerRelationshipManager', 'SalesManager', 'EventPlanner', 'Lawyer', 'HumanResource']
agreeablenessJobs = ['Nurse', 'CustomerRelationshipManager', 'Professor', 'HealthCounselor', 'HumanResource']
neurotismJobs = ['Librarian', 'Writer', 'Nutritionist', 'GraphicsDesigner', 'Masseuse', 'TopExecutive']

def assignZero(col):
    for attribute in listOfAttributes:
        dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)] = 0

def notAssigned(col): 
    for attribute in listOfAttributes:
        if dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)] != 0.0:
            return False
    return True

def incrementCount(tempList):    
    for attribute in tempList:
        dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)] += 1

def normalize():
    for attribute in listOfAttributes:
            dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)] = dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)]/10

for col in dataframe.itertuples():

    assignZero(col)
    tempList = []

    #OPENNESS
    if (float(col[2]) > 0.73):
        incrementCount(opennessJobs)    

    #CONSCIENTIOUNESS
    if (float(col[3]) > 0.475):
        incrementCount(conscientiounessJobs)

    #EXTRAVERSION
    if (float(col[4]) > 0.45):
        incrementCount(extraversionJobs)

    #AGREEABLENESS
    if (float(col[5]) > 0.37):
        incrementCount(agreeablenessJobs)

    #NEUROTISM
    if (float(col[6]) > 0.48):
        incrementCount(neurotismJobs)

    if notAssigned(col) == True:
        maxOfAll = float(col[2])
        pos = 2
        for i in range(2, 7):
            if maxOfAll < float(col[i]):
                maxOfAll = float(col[i])
                pos = float(i)

        if pos == 2:
            incrementCount(opennessJobs)    

        elif pos == 3:
            incrementCount(conscientiounessJobs)

        elif pos == 4:
            incrementCount(extraversionJobs)

        elif pos == 5:
            incrementCount(agreeablenessJobs)

        elif pos == 6:
            incrementCount(neurotismJobs)
        
    #normalize()
    
dataframe.to_csv(path+"TrainingDataJob.csv", index = False)

