import requests
from bs4 import BeautifulSoup

URL= 'https://www.monster.com/jobs/search/?q=Programmer&where=Tennessee'
page= requests.get(URL) #perform an HTTP request to the URL
soup = BeautifulSoup(page.content, 'html.parser') #create a Beautiful Soup object that takes the HTML content from the input
results = soup.find(id='ResultsContainer') #find an element with the id ResultsContainer

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print('----------------')
    #print with whitespaces removed
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
