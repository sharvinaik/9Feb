import pandas as pd
from Path import path

dataframe = pd.read_csv(path+"TrainingDataBook.csv")

listOfAttributes = ['Comic','Crime','Drama','Educational','Fantasy','Fiction','Mystery','Poetry','Non-Fiction','Romance','Science-Fiction','Thriller','Horror']

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
        dataframe.iloc[col[0], dataframe.columns.get_loc('Poetry')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fiction')] += 1
        
    if (float(col[2]) < 0.73 and float(col[2]) > 0.47):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Mystery')] += 1
    if (float(col[2]) < 0.47):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comic')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Educational')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fantasy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Non-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1

    #CONSCIENTIOUNESS
    if (float(col[3]) > 0.475):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Educational')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
    if (float(col[3]) < 0.475 and float(col[3]) > 0.22):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comic')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fantasy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Poetry')] += 1
    if (float(col[3]) < 0.22):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Non-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Mystery')] += 1

    #EXTRAVERSION
    if (float(col[4]) > 0.45):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Mystery')] += 1
    if (float(col[4]) < 0.45 and float(col[4]) > 0.23):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comic')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fantasy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Non-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
    if (float(col[4]) < 0.23):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Educational')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Poetry')] += 1

    #AGREEABLENESS
    if (float(col[5]) > 0.37):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Educational')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Non-Fiction')] += 1
    if (float(col[5]) < 0.37 and float(col[5]) > 0.14):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comic')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Mystery')] += 1
    if (float(col[5]) < 0.14):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fantasy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Poetry')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        
    #NEUROTISM
    if (float(col[6]) > 0.48):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Crime')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fantasy')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Poetry')] += 1
    if (float(col[6]) < 0.48 and float(col[6]) > 0.31):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Educational')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Non-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Romance')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Mystery')] += 1
    if (float(col[6]) < 0.31):
        dataframe.iloc[col[0], dataframe.columns.get_loc('Comic')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Drama')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Science-Fiction')] += 1
        dataframe.iloc[col[0], dataframe.columns.get_loc('Horror')] += 1
        
    #normalize()

dataframe.to_csv(path+"TrainingDataBook.csv", index = False)
dataframe
