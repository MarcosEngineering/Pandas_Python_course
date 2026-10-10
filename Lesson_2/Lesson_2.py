# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:58:09 2026

@author: mcamp
"""

import pandas as pd

df=pd.read_csv("movies.csv")
df.info()

print(df.describe())

# 1. Strip the diollar sign
# 2. Strip the commma
# 3. Convert the remaininhg text into a float (decimal)

df['Gross'] = df['Gross'].str.replace('$','', regex=False).str.replace(',','', regex= False).astype(float)
print(df['Gross'])

print(df['Gross'].mean())


df['Studio_Profits']= df ['Gross']*0.5

print (df['Studio_Profits'])

print (df['Studio_Profits'].mean())

# Filter 1 : Find all movies made by Universal
universal_movies= df[df['Studio']=='Universal']

print(universal_movies)

# Filter 2: Numerical condition (find movies that made over $2 Billion )
billion_club=df[df['Gross'] > 2000] 
print (billion_club)
# Filter 3 : Multiple Conditions (universal movies reased after 2010)

modern_universal= df[(df['Studio']== 'Universal') & (df['Year'] > 2010 ) ]
print (modern_universal)

# Sort the data by year, from newest to oldest
newest_movies= df.sort_values(by="Year", ascending=False)

print(newest_movies)

# Sort by multiple colums: First alphabetical by studi, then by Gross revenue

studio_ranking = df.sort_values(by=["Studio", "Gross"], ascending=[True,False])
print(studio_ranking)



