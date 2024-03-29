# -*- coding: utf-8 -*-
"""Breast Cancer Wisconsin (Prognostic) Data Set.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ad3rkGoRu0_KJL1bD8qU5iN4nXSPRse1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data 2.csv")

df.columns

df[["radius_mean","perimeter_mean"]].describe()

df.info()

df.drop(["Unnamed: 32","id"],axis = 1,inplace = True)

np.sum(df.isna())

df.head()

df["diagnosis"].value_counts()

sns.countplot(df["diagnosis"])

sns.barplot(df["diagnosis"],df["area_mean"])

plt.figure(figsize=(5,4))
sns.lineplot(x = df["radius_mean"],y=df["perimeter_mean"],hue = df["diagnosis"])

corrMatrix = df.corr()
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(corrMatrix, annot=True,ax=ax)
plt.show()

sns.swarmplot(df["diagnosis"],df["radius_mean"])

plt.figure(figsize=(6,4))
sns.scatterplot(x=df["radius_mean"],y= df["texture_mean"],hue = df["diagnosis"])

sns.kdeplot(df["radius_mean"],shade = True)

X = df.drop(["diagnosis"],axis = 1)

df["diagnosis"] = df["diagnosis"].map({"M":0, "B":1}) 
y = df.diagnosis

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC,SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

from sklearn.metrics import confusion_matrix, accuracy_score

models=[LogisticRegression(),LinearSVC(),SVC(kernel='rbf'),KNeighborsClassifier(),RandomForestClassifier(),
        DecisionTreeClassifier(),GradientBoostingClassifier(),GaussianNB()]
model_names=['LogisticRegression','LinearSVM','rbfSVM','KNearestNeighbors','RandomForestClassifier','DecisionTree',
             'GradientBoostingClassifier','GaussianNB']
acc_score=[]

for model in range(len(models)):
    clf=models[model]
    clf.fit(X_train,y_train)
    pred=clf.predict(X_test)
    acc_score.append(accuracy_score(pred,y_test))
     
d={'Classification_Algorithm':model_names,'Accuracy':acc_score}
models_summary_table=pd.DataFrame(d)

models_summary_table

sns.barplot(y='Classification_Algorithm',x='Accuracy',data=models_summary_table)
plt.xlabel('Learning Models')
plt.ylabel('Accuracy scores')
plt.title('Accuracy levels of different classification models')