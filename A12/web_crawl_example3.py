from bs4 import BeautifulSoup
import requests
import os
import pandas as pd 
import matplotlib.pyplot as plt


URL= 'https://www.city-data.com/coronavirus/'
page= requests.get(URL) #perform an HTTP request to the URL
soup = BeautifulSoup(page.content, 'html.parser') #create a Beautiful Soup object that takes the HTML content from the input
results_collapse1 = soup.find(id='collapse1') #find an element with the id collapse1

state_elems= results_collapse1.find_all('tr')
state_data= []  #collecting each row for making a dataframe
for s_ct, state_row in enumerate(state_elems):
    columns_col= state_row.find_all('td')
    if columns_col:
        state_tag, confirmed_tag, recovered_tag, active_tag, deaths_tag = columns_col
        state_data.append([
            str(state_tag.text),
            int(confirmed_tag.text.replace(',', '')),
            int(deaths_tag.text.replace(',', ''))
        ])
         
df= pd.DataFrame(state_data, columns= ['State', 'Confirmed', 'Deaths']) #create a pandas dataframe
df.to_csv(os.path.join('data', 'city_covid_data.csv')) #save pandas dataframe to a csv file

df.sort_values(by=['Confirmed'], inplace=True, ascending=True) #sorting values by Confirmed in ascending order
print(df.head(10))
ax= df.head(25).plot.bar(x= 'State', y={'Confirmed', 'Deaths'}, rot=0)
plt.xticks(rotation=45)
plt.savefig(os.path.join('data', 'least25.pdf'))
plt.show() #display the figure
