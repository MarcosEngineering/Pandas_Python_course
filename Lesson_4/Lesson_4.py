# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:21:12 2026

@author: mcamp


import pandas as pd

# Creating a sample sales dataset
data = {
    'Store': ['New York', 'New York', 'London', 'London', 'Tokyo'],
    'Department': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
    'Revenue': [5000, 2000, 4500, 3000, 7000]
}

df= pd.DataFrame(data)

print (df)

# Grou by store to find total revenue per location

store_totals = df.groupby('Store')['Revenue'].sum()

print(store_totals)

# 1 Concateating (Stacking data)

january_sales = pd.DataFrame({'Date': ['Jan 1'], 'Sale': [100]})
february_sales = pd.DataFrame({'Date': ['Feb 1'], 'Sale': [150]})

all_sales = pd.concat([january_sales,february_sales], ignore_index=True)

print(all_sales)

# 2 MERGING 

customers = pd.DataFrame({'CustomerID': [1,2], 'Name': ['Alice','Bob']})
orders = pd.DataFrame({'OrderID': [101,102],'CustomerID': [1,2], 'Amount': [250,400]})

# Merge orders with customers names matching on the CustomerID column

merge_data =pd.merge(orders,customers, on='CustomerID')

print(merge_data)

# Create a pivot table

pivot =pd.pivot_table(
    df,
    values='Revenue', 
    index='Store',  # these become the rows
    columns='Department', # these become the column
    aggfunc='sum', # the math to apply
    fill_value=0  # Fill empty combination with 0 instead of NaN
    
    )

print(pivot)

"""

import pandas as pd

# Load the data
df= pd.read_csv('movies.csv')

df['Gross']=df['Gross'].str.replace('$','', regex=False)
df['Gross']=df['Gross'].str.replace(',','', regex=False)
df['Gross']=df['Gross'].astype(float)

# 1 Group the datatset by Studio

studios = df.groupby('Studio')

# 2 Add up (sum) the Gross revenue for each studio

studio_revenue = studios['Gross'].sum()

top_studios = studio_revenue.sort_values(ascending=False)


print(top_studios.head())

# create a second DatatFrame rapresenting data from another file
hq_data= pd.DataFrame({
     'Studio':['Buena Vista', 'Fox','Universal'],
     'Location': ['Burbank, CA', 'Century City, CA', 'Universal City, CA']

    })

merged_df= pd.merge(df,hq_data, on='Studio', how='inner')

print(merged_df[['Title','Studio','Location']].head)

# Filter for modern movies (2015 and newer)

modern_movies=df[df['Year']>=2015]

# Create the Pivot table
pivot = pd.pivot_table(
    modern_movies,
    values= 'Gross', 
    index ='Year', # Years  become the rows
    columns='Studio',# studios become the columns
    aggfunc='sum', # math: add the revenue together 
    fill_value=0 # fil with 0 instead NaN
    
    )

print (pivot[['Buena Vista','Universal', 'Warner Brothers']].head())









