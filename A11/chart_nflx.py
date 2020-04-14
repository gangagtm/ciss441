import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd  
import pandas_datareader.data as web

style.use('ggplot') #set a plot style
start = dt.datetime(2000,1,1)
end= dt.datetime(2016,12, 31)
df= web.DataReader("NFLX", "yahoo", start, end) #create a pandas dataframe
print(df.tail(6)) #print last 6 rows


df.to_csv('nflx.csv') #export pandas dataframe to a csv file
