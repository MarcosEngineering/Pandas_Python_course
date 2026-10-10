# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:04:14 2026

@author: mcamp


import pandas as pd
import numpy as np

data = {
    'Product': ['  Laptop ', 'Mouse', 'Keyboard', 'monitor', 'Tablet'],
    'Price': ['$1,200', '$25', np.nan, '$300', '$450'],
    'Stock': ['15', '100', '50', np.nan, '0']
}

df = pd.DataFrame(data)
print(df)

# Check how many missing values exist in each column
print (df.isna().sum())

# Option A : Drop any row with a missing value

df_dropped = df.dropna()
print (df_dropped)

# Option B: Fill missing stock with value 0, and missing price with a placeholder
df['Stock']= df['Stock'].fillna('0')
df['Price']= df['Price'].fillna('$0')

print(df)

# Strip whitespace and Capitalize the first letter for uniformity
df['Product']=df['Product'].str.strip().str.capitalize()

# Remove the dollar signs and commas from the Price column

df["Price"]=df["Price"].str.replace('$','', regex=False)
df["Price"]=df["Price"].str.replace(',','', regex=False)
 
print (df)

# Convert Stock to integers (whole numbers)

df['Stock']=df['Stock'].astype(int)

# Convert Price to floats (decimals)

df['Price']=df['Price'].astype(float)

# Calulate total Inventory vale:
df['Inventory_value']= df['Price']*df['Stock']

print(df[['Product','Inventory_value']])

"""

import pandas as pd
import numpy as np

df = pd.read_csv('google_playstore.csv')
print(df[['App','Rating','Installs','Price']].head(50))

# Create a TRue/False mask of missing values, then sum them up per column

print(df[['App','Rating','Installs','Price']].isna().sum()) 

# Calculate the mean rating

avarage_rating = df['Rating'].mean()

# Fill the NaN values with our calculated avarage

df['Rating']=df['Rating'].fillna(avarage_rating)

print(df[['App','Rating','Installs','Price']].head(50))


# Remove the + and , from INstalls column
df['Installs']=df['Installs'].str.replace('+','',regex=False).str.replace(',','',regex=False)

# Reùove the $ from the Price column
df['Price']=df['Price'].str.replace('$','',regex=False)

print(df[['App','Rating','Installs','Price']].head(10))

# pd.to_nummeric with errors= 'coerce' turns any hidden typos into NaN
 
df['Price']= pd.to_numeric(df['Price'], errors='coerce').fillna(0)
df['Installs']= pd.to_numeric(df['Installs'], errors='coerce').fillna(0)

# Convert to numerical type

df['Price']=df['Price'].astype(float)
df['Installs']=df['Installs'].astype(int)

print(df[['Installs','Price','Rating']].dtypes)






