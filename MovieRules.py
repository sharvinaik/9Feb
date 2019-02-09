import pandas as pd
from Path import path
dataframe = pd.read_csv(path+"TrainingDataMovie.csv")

listOfAttributes = ['Horror','Comedy','Romance','Thriller','Drama','Action','Adventure','Crime','Science-Fiction','Animation']

def assignZero(col):
    for attribute in listOfAttributes:
        dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)] = 0

def normalize():
    for attribute in listOfAttributes:
            dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)] = dataframe.iloc[col[0], dataframe.columns.get_loc(attribute)]/10

for col in dataframe.itertuples():
    assignZero(col)

    #OPENNESS
    if (float(col[2]) > 0.73):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Thriller')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Action')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
    if (float(col[2]) < 0.73 and float(col[2]) > 0.47):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comedy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
    if (float(col[2]) < 0.47):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Adventure')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Animation')] += 1

    #CONSCIENTIOUNESS
    if (float(col[3]) > 0.475):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Adventure')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
    if (float(col[3]) < 0.475 and float(col[3]) > 0.22):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comedy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Animation')] += 1
    if (float(col[3]) < 0.22):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Thriller')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Action')] += 1

    #EXTRAVERSION
    if (float(col[4]) > 0.45):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comedy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Action')] += 1
    if (float(col[4]) < 0.45 and float(col[4]) > 0.23):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Thriller')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Animation')] += 1
    if (float(col[4]) < 0.23):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Adventure')] += 1

    #AGREEABLENESS
    if (float(col[5]) > 0.37):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comedy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Adventure')] += 1
    if (float(col[5]) < 0.37 and float(col[5]) > 0.14):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Animation')] += 1
    if (float(col[5]) < 0.14):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Thriller')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Action')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
        
    #NEUROTISM
    if (float(col[6]) > 0.48):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Thriller')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Animation')] += 1
    if (float(col[6]) < 0.48 and float(col[6]) > 0.31):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Adventure')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Action')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
    if (float(col[6]) < 0.31):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comedy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1

    #normalize()

dataframe.to_csv(path+"TrainingDataMovie.csv", index = False)
dataframe
