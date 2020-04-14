import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd  
import pandas_datareader.data as web
style.use('ggplot') #set a plot style

df= pd.read_csv('nflx.csv', parse_dates= True, index_col=0) #read csv file as pandas dataframe
df['100ma']= df['Adj Close'].rolling(window=100, min_periods=0).mean() #add a new column to the dataframe
print(df.head()) #print the first five rows of the dataframe

ax1=plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) #add first subplot 
ax2=plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) #add second subplot 

ax1.plot(df.index, df['Adj Close']) #plot a line with date and Adj Close
ax1.plot(df.index, df['100ma']) #plot a line with date and 100ma
ax2.bar(df.index, df['Volume']) #plot a line with date and Volume
plt.show() #display the figure
