import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a basic series
series_1 = pd.Series([121,312.2,618,727,916.4])
print(series_1)

# Get by single position and multiple positions
print(series_1[2])
print(series_1[[1,2,3]])

# Create an indexed series
series_2 = pd.Series({"a":2, "b":4, "c":6, "d":8})
print(series_2)

# Get specific values from series by simple criteria
print(series_1[series_1 < 800])
print(series_2[series_2 >= 4])

# Make a data frame from scratch
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print(football)

# Print the sum, mean, and SD of the 'wins' column
print(football['wins'].sum())
print(football['wins'].mean())
print(football['wins'].std())

# Describe the data - get a summary
print(football.describe())

# Read in a data set
# Austrailian Trade CSV: https://data.gov.au/dataset/country-and-commodity-trade-data-file
df = pd.read_csv("data/aus-trade.csv", parse_dates=False).dropna()
df.convert_objects(convert_numeric = True)

# See the column names
print(df.columns)

# Look at first 10 rows
print(df[:10]) 
#df = df.set_index("Date")

# SELECTING COLUMNS: Get a new data frame with only columns 
# 'Partner country' and 'Geographic level 1' from the original.
print(df[['Partner country', 'Geographic level 1']][:10])

# df[(df['float_col'] > 0.1) & (df['int_col']>2)]

# TODO - group by
df2 = df[['Partner country', 'A$000']]
grouped = df2.groupby('Partner country')# grouped = df['float_col'].groupby(df['str_col'])
#print(grouped.describe())
print(type(df2['A$000'][2]))