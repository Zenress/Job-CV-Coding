#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("Machine Learning Datasets/KNN_Project_Data.csv")
print(df.head())

myscaler = StandardScaler()
myscaler.fit(X=df.drop("TARGET CLASS", axis=1))
X = myscaler.transform(X=df.drop("TARGET CLASS", axis=1))

tdf = pd.DataFrame(X, columns=df.columns[:-1])
print(tdf.head())

y = df["TARGET CLASS"]
X_train, X_Test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=101)

myKNN = KNeighborsClassifier(n_neighbors=1)
myKNN.fit(X_train, y_train)