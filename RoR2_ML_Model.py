import numpy as np
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score



#Connecting the SQlite Database to Python
con = sqlite3.connect('RoR_Data.db')
#reading the sql database into a DataFrame
df = pd.read_sql_query('Select * From RunData Natural join ItemData;', con)

'''
A Lot of replacements are going to take place to turn categorical data into numerical
There may be a function here later to hide all of this replacing
'''
def data_correction():
    #Replacing winning runs with 1 and losing with 0
    win_description = ['MainEnding', 'ObliterationEnding', 'PrismaticTrialEnding', 'VoidEnding', 'LimboEnding']
    df.replace(win_description, 1, inplace=True)
    df.replace('StandardLoss', 0, inplace=True)

    #replacing characters played to numerical value
    Survivors = ['Bandit2Body', 'CaptainBody', 'CommandoBody', 'CrocoBody', 'EngiBody', 'HuntressBody', 'LoaderBody',
                 'MageBody', 'MercBody', 'RailgunnerBody', 'ToolbotBody', 'TreebotBody', 'VoidSurvivorBody']
    df.replace(Survivors[2], 0, inplace=True)
    df.replace(Survivors[5], 1, inplace=True)
    df.replace(Survivors[0], 2, inplace=True)
    df.replace(Survivors[10], 3, inplace=True)
    df.replace(Survivors[4], 4, inplace=True)
    df.replace(Survivors[7], 5, inplace=True)
    df.replace(Survivors[8], 6, inplace=True)
    df.replace(Survivors[11], 7, inplace=True)
    df.replace(Survivors[6], 8, inplace=True)
    df.replace(Survivors[3], 9, inplace=True)
    df.replace(Survivors[1], 10, inplace=True)
    df.replace(Survivors[9], 11, inplace=True)
    df.replace(Survivors[12], 12, inplace=True)
    df.replace('TracerBody', 0, inplace=True)
    df.replace('DGSamusBody', 0, inplace=True)
    df.replace('MinerBody', 0, inplace=True)
    df.replace('RobPaladinBody', 0, inplace=True)

    #replacing gamemode with numerical
    df.replace('ClassicRun', 0, inplace=True)
    df.replace('EclipseRun', 1, inplace=True)
    df.replace('InfiniteTowerRun', 2, inplace=True)
    df.replace('WeeklyRun', 3, inplace=True)

    #replacing Difficuly with numerical
    df.replace('Easy', 0, inplace=True)
    df.replace('Normal', 1, inplace=True)
    df.replace('Hard', 2, inplace=True)
    df.replace('Eclipse', 3, inplace=True)

    #droping equipment for the mean time
    df.drop(columns='Equipment', inplace=True)

data_correction()
#print(df)

y = df.loc[:, 'GameEnding']

X = df.loc[:, df.columns != 'GameEnding']

#print(X)
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
print('\nAccuracy of SKLearn Function: %d%%\n' % (int(accuracy_score(y_test, y_pred) * 100)))





