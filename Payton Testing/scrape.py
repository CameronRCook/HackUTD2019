#This uses urlopen to access a site, then uses BeautifulSoup to get the
#HTML from that site, and then cuts out all of the non-text
import re
from bs4 import BeautifulSoup
import requests

def getRating(name):

    #Initial Search for the Professor
    URL = "https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=The+University+of+Texas+at+Dallas&schoolID=1273&query=" + name
    site = requests.get(URL)
    
    soup = BeautifulSoup(site.content, 'html.parser')
    search = soup.find("a", href=re.compile("ShowRatings"))
    URL = "https://www.ratemyprofessors.com" + search.get('href') # new link
    
    
    #Get Number from the actual professor page.
    site = requests.get(URL)
    soup = BeautifulSoup(site.content, 'html.parser')
    search = soup.find('div', attrs={'class':'grade'})
    grade = search.text
    print(grade)


    return

name = "Jason+Smith"
getRating(name)
# Input search into function and call function


##### FUNCTION

## Use search to open page with request.
## Once page is open soupify it.
## search for the link of the professor button
## open the new link with request
## soupify the new link
## look for the number
## return number
