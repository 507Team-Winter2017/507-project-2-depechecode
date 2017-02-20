#proj2.py
import requests
from bs4 import BeautifulSoup
import re

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
html = requests.get("https://www.nytimes.com/").text
soup = BeautifulSoup(html,"html.parser")
heading = soup.find_all("h2",class_="story-heading")
for h in heading[:10]:
    try:
        print (h.a.string)
    except:
        print (h.string.strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
html = requests.get("https://www.michigandaily.com/").text
soup = BeautifulSoup(html,"html.parser")

most_read = soup.find("div",class_="panel-pane pane-mostread")
for child in most_read.descendants:
    if child.name == "a":
        print (child.string)

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
html = requests.get("http://newmantaylor.com/gallery.html").text
soup = BeautifulSoup(html,"html.parser")

imgs = soup.find_all("img")
for img in imgs:
    if "alt" in img.attrs:
        print (img['alt'])
    else:
        print ("No alternative text provided!!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
BASE_URL = "https://www.si.umich.edu/"
DIRECTORY_PAGE = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"

i = 1
for page in range(6):
    html = requests.get(DIRECTORY_PAGE,params = {'page':page},headers={'User-Agent': 'SI_CLASS'}).text
    soup = BeautifulSoup(html,"html.parser")
    nodes = soup.find_all("a",string = "Contact Details")
    for node in nodes:
        email_html = requests.get(BASE_URL+node["href"],headers={'User-Agent': 'SI_CLASS'}).text
        email_soup = BeautifulSoup(email_html,"html.parser")
        print ("{} {}".format(str(i),email_soup.find(string = re.compile("@umich.edu"))))
        i += 1
