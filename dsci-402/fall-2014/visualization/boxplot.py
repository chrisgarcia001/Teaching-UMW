import numpy as np
import pylab as pl

from dateutil.parser import parse
import pandas as pd

df = pd.read_csv("http://bit.ly/119792b")
print(df.columns)
df.date = df.date.apply(parse)
df = df.sort(['date'])
df.index = df.date
df = df.fillna(0)

df.boxplot()
pl.show()

cols = ['Beef', 'Pork', 'Turkey', 'Broilers']
df[cols].plot()
pl.show()
