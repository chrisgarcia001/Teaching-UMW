import pandas as pd
import numpy as np
import pprint
import matplotlib.pyplot as plt

# Read in the cars dataset.
cars = pd.read_csv('./data/cars.csv.')

# ------ Basic Examples ------------------------------------------

# Nicely prints out the first few rows of data (head() gets first few rows)
pprint.pprint(cars.head())

# Get descriptive statistics for the data.
print(cars.describe())

# Describe the 'mpg' column only.
print(cars['mpg'].describe())

# Print the mean and standard deviations for the 'mpg' column.
print(cars['mpg'].mean())
print(cars['mpg'].std())

# Print the mean for column 1 (0 = leftmost column).
print(cars['mpg'].mean())

# Get column names - note it is a little unintuitive.
print(list(cars))

# ------ Simple Selection/Subsetting Examples ------------------------

# Get new DF with just the MPG, DISP, and HP columns and print its head.
pprint.pprint(cars[['mpg', 'disp', 'hp']].head())

# Get new DF where each row has HP >= 200 and MPG >= 25.
pprint.pprint(cars[(cars['hp'] >= 200) & (cars['mpg'] >= 10)])



# ------ Summarizing/Aggregation/Grouping Examples ------------------
# BTW - good tutorial here: https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

# Get avg. MPG for each distinct number of cylinders.
print(cars.groupby('cyl')['mpg'].mean())

# Get avg. MPG for each distinctcylinder/am combination.
print(cars.groupby(['cyl', 'am'])['mpg'].mean())

# ------ Pairs Plot Examples ------------------
sm = pd.plotting.scatter_matrix(cars)
plt.show()