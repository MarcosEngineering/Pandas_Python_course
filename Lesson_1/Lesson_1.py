# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:02:09 2026

@author: mcamp


import pandas as pd

# Creating a series from a Python list

ages = pd.Series([ 25,30,45,60])

print(ages)

# Creating a Dataframes from a Dictionary
 
data = { 
        'Name' : ['Alice','Bob','Marco','Beltrand'],
        'Ages' : [ 25,30,45,60],
        'City'  : ['New York','Boston','Rome','Paris'] 
         
     }

df = pd.DataFrame(data)
print(df)

"""

import pandas as pd

movies= pd.read_csv("movies.csv", index_col='Title')
print(movies)

head_movies= movies.head(10)
print(head_movies)

tail_movies= movies.tail(10)
print(tail_movies)

number=len(movies)
print(number)

dim=movies.shape
print(dim)

type_1=movies.dtypes
print(type_1)

position= movies.iloc[300]
print(position)

movie_2= movies.loc["Star Wars: The Force Awakens"]
print(movie_2)