import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_csv("wmt.csv", parse_dates = True)
df = df.set_index("Date")
cols = filter(lambda x: x != "Volume", df.columns)
print(cols)
df = df[cols]
df = df.sort_index() # Sort by Date
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()