import requests
from bs4 import BeautifulSoup

URL= 'https://www.city-data.com/coronavirus/'
page= requests.get(URL) #perform an HTTP request to the URL
soup = BeautifulSoup(page.content, 'html.parser') #create a Beautiful Soup object that takes the HTML content from the input
results_parent = soup.find(id='card-content') #find an element with the id card-content
results_collapse1 = soup.find(id='collapse1') #find an element with the id collapse1

state_elems= results_collapse1.find_all('tr')
#print the headers
print("{0:<30}{1:<20}{2:<20}{3:<20}{4:<20}".format(
    "State",
    "Confirmed",
    "Recovered",
    "Active",
    "Deaths"
))
for s_ct, state_row in enumerate(state_elems):
    columns_col= state_row.find_all('td')
    if columns_col:
        state_tag, confirmed_tag, recovered_tag, active_tag, deaths_tag = columns_col
        print("{0:<30}{1:<20}{2:<20}{3:<20}{4:<20}".format(
            state_tag.text,
            confirmed_tag.text,
            recovered_tag.text,
            active_tag.text,
            deaths_tag.text
        ))

