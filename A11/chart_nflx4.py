
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.dates import date2num
import pandas as pd  
import pandas_datareader.data as web
style.use('ggplot') #set a plot style

df= pd.read_csv('nflx.csv', parse_dates= True, index_col=0) #read csv file as pandas dataframe

df_ohlc= df['Adj Close'].resample('10D').ohlc() #create a new dataframe with resampling of 10 days
df_volume= df['Volume'].resample('10D').sum() ##create a new dataframe with resampling of 10 days
df_ohlc.reset_index(inplace=True) #reset date as index
df_ohlc['Date']=df_ohlc['Date'].map(date2num) #convert datetime object to matplotlib dates
print(df_ohlc.head()) #print the first five rows of the dataframe

ax1= plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) #add first subplot
ax2= plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex= ax1) #add second subplot
ax1.xaxis_date() 

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup= 'g') #plot a candlestick chart 
ax2.fill_between(df_volume.index.map(date2num), df_volume.values, 0) 
plt.show() #display the figure
