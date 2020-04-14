import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd  
import pandas_datareader.data as web
style.use('ggplot') #set a plot style

df= pd.read_csv('nflx.csv', parse_dates= True, index_col=0) #read csv file as pandas dataframe
print(df[['Open', 'High']].head()) #print first five rows of Open and High columns
df['Adj Close'].plot() #use plot atrribite to plot just the "Adj Close" column
plt.show() #display the figure
