import numpy as np
import pylab as pl

from dateutil.parser import parse
import pandas as pd

# monthly slaughter records since 1921
df = pd.read_csv("http://bit.ly/119792b")
# parse the data (we could also use pd.to_datetime)
df.date = df.date.apply(parse)
# sort the data frame by date
df = df.sort(['date'])
# create an index
df.index = df.date
# fill months without data with 0s
df = df.fillna(0)

# built in boxplot method
df.boxplot()
pl.show()
# built in histogram method
#df.hist()
#pl.show()

# let's make a time series plot of just the most popular
cols = ["Beef", "Pork", "Turkey", "Broilers"]
df[cols].plot()
#df[cols].hist()
# note that since the data frame is indexed, 
# pandas automatically renders the plot w/ a date for the x-axis
pl.show()

# add a 12 month moving average
df[cols].apply(lambda x: pd.rolling_mean(x, 12)).plot()
pl.show()

df['Beef'].hist()
pl.show()
df['Beef'].plot()
pl.show()