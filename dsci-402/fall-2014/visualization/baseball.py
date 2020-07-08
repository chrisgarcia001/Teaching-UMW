import numpy as np
import pandas as pd
import pylab as pl

baseball = pd.read_csv("http://bit.ly/144sh7t")

# group by year and get a summary of each numeric column
baseball.groupby(["year"]).describe()
# for each year, get the mean of each column
baseball.groupby(["year"]).aggregate(np.mean)
# you can create group objects
baseball_grouped = baseball.groupby(["year"])
# getting the count of rows for each league
baseball.groupby("lg").size()
# lg
# AA      171
# AL    10007
# FL       37
# NL    11378
# PL       32
# UA        9

# records per year
baseball.groupby(["year"]).size()
# year
# 1871     7
# 1872    13
# 1873    13
# 1874    15
# 1875    17
# ...

def analyze(df):
    return pd.Series({"nrow": len(df), "ncol": len(df.columns)})
# rows and columns per league
baseball.groupby("lg").apply(analyze)
#     ncol   nrow
# lg             
# AA    22    171
# AL    22  10007
# FL    22     37
# NL    22  11378
# PL    22     32
# UA    22      9

# aggregate over year and get mean RBIs per year
mean_rbis = baseball.groupby("year")['rbi'].aggregate(np.mean)
mean_rbis.head()
# year
# 1871    22.285714
# 1872    20.538462
# 1873    30.923077
# 1874    29.000000
# 1875    31.588235

mean_rbis.plot()
pl.show()

def years_played_to_date(player):
    years_to_date = player.year - np.min(player.year) + 1
    player['years_to_date'] = years_to_date
    return player

# for each player, calculate the number of years played
players = baseball.groupby("id").apply(years_played_to_date)
players.ix[players.id=="ansonca01"]
#            id  year  stint team  ...  years_to_date
# 0   ansonca01  1871      1  RC1  ...              1
# 7   ansonca01  1872      1  PH1  ...              2
# 20  ansonca01  1873      1  PH1  ...              3
# 33  ansonca01  1874      1  PH1  ...              4
# 48  ansonca01  1875      1  PH1  ...              5

# get the mean and median years played and plot it
players.groupby("year").aggregate([np.mean, np.median]).years_to_date.plot()
pl.show()