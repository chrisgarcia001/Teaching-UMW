import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/walmart.csv", parse_dates=True)
df = df.set_index("Date")
cols = filter(lambda x: x != "Volume", df.columns)
df = df[cols]
df = df.sort_index()#by=['Date'], ascending=[True])
plt.figure() 
df.plot() 
plt.legend(loc='best')
plt.show()

# Filtering example:
# df[df["Open"] > 76] # Gets rows where "Open" column > 76