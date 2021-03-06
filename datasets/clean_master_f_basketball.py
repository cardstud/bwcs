import numpy as np
import pandas as pd 
import csv 
# import matplotlib.pyplot as plt


df = pd.read_csv(r'C:/Users/Todd/Desktop/python_learn/python_data_analytics/buildweek/datasets/Master_f_basketball.csv')

print(df.head())

print(df.columns)

df1 = (df[['weight', 'height', 'gender','sport']].copy())
print(df1.head())

print(df1.shape)


df1['gender'].fillna('Female', inplace =True)
df1['sport'].fillna('Basketball', inplace =True)
print(df1.head())

print(df1.columns)

df1['weight'] = (df1['weight'].values*2.20462262)
print(df1.head())

df1['height'] = (df1['height'].values/2.54)
print(df1.head())

# df1['id'] = range(1, 1+len(df1))
df1.insert(0, 'id', range(1,1+len(df1)))
print(df1.head(66))

df1.set_index('id', inplace=True)
print(df1.head())


print(df1.isna().sum())

df1 = df1.dropna()
print(df1.shape)
print(df1.isna().sum())

df1 = df1.round(1)

print(df1.head(20))

print(df1.describe())

df1.to_csv('basketball_f.csv')