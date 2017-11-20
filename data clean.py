
# coding: utf-8

# In[ ]:

import pandas as pd
titanic_data=pd.read_csv('titanic-data.csv')
titanic_data=titanic_data[['Survived', 'Pclass','Sex','Age']]
titanic_data= titanic_data[titanic_data["Age"].notnull()]
titanic_data['Count']=1
titanic_data.rename(columns={'Survived':'Survival'}, inplace=True)
titanic_data['Survival'] = titanic_data['Survival'] .apply(lambda x: "survived" if x==1 else "deceased")
titanic_data['AgeGroup'] = titanic_data['Age'].apply(lambda x: "children" if x<10 else ("teenagers" if 10<=x<=18 else("adults" if 19<x<65  else "Seniors")))
titanic_data['Pclass'] = titanic_data['Pclass'].apply(lambda x: "upper" if x==1 else ("middle" if x==2  else "lower"))
titanic_data_children=titanic_data[titanic_data.AgeGroup=="children"]
titanic_data_children.to_csv("titanic_children.csv")
titanic_data_children=titanic_data[titanic_data.AgeGroup=="teenagers"]
titanic_data_children.to_csv("titanic_teenagers.csv")
titanic_data_adults=titanic_data[titanic_data.AgeGroup=="adults"]
titanic_data_adults.to_csv("titanic_adults.csv")
titanic_data_seniors=titanic_data[titanic_data.AgeGroup=="Seniors"]
titanic_data_seniors.to_csv("titanic_seniors.csv")

