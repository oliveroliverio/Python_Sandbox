#!/usr/bin/env python
# https://www.youtube.com/watch?v=2BrpKpWwT2A&t=4s

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import time
import os

style.use('ggplot')

#--------timed explanation functions--------
#---------------------------------------------
def timedMessage(message):
 #   time.sleep(1)
    print("\n")
    print(message)
    # waits for user keyboard enter input
    print("\n\n")
 #   input("press enter to continue")
    # I want to clear the console screen but the bottom doesn't work
    #os.system('clear')


# ----Convert DF to CSV-----------
timedMessage("Convert DF to CSV")
# start = dt.datetime(2015,1,1)
# end = dt.datetime(2019,4,14)
# df = web.DataReader('TSLA', 'yahoo', start,end)
# # convert above df into csv
# df.to_csv('tsla.csv')


#---Read a CSV in-----
timedMessage("here's how to read in CSV from local")
df = pd.read_csv('tsla.csv')
print(df.head())

# However, we want a datetime index
# let the 1st col be the index w/ index_col
timedMessage("However, we want a datetime index")
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
print(df.head())
timedMessage("be sure to lookup how to read json")

#---------Plot------------
timedMessage("DF's have plot attributes, so try the function df.plot(), df.show()")
df.plot()
plt.show()

# only want one column
timedMessage("say we only want adjusted close column, plot this")
df['Adj Close'].plot()
plt.show()


#----------subsetting DFs
print(df[['Open', 'High']].head())
