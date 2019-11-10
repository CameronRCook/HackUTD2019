#This uses urlopen to access a site, then uses BeautifulSoup to get the
#HTML from that site, and then cuts out all of the non-text

import requests
from bs4 import BeautifulSoup

def abSem(semester) : #abbreviates the semester value to get the whole term ----returns the one letter abbreviation
    if semester.lower() == "fall":
        return "f"
    elif semester.lower() == "spring":
        return "s"
    elif semester.lower() == "summer":
        return "u"
    else :
        return "And the Lord spake, saying, 'First shalt thou take out the Holy Pin. Then, shalt thou count to three, no more, no less. Three shall be the number thou shalt count, and the number of the counting shall be three. Four shalt thou not count, nor either count thou two, excepting that thou then proceed to three. Five is right out! Once the number three, being the third number, be reached, then lobbest thou thy Holy Hand Grenade of Antioch towards thou foe, who being naughty in my sight, shall snuff it.'"

def scrapeProf(prefix,year,semester,number) : #navigates to the coursebook page with the search criteria and returns creates a list of all the professors
    term = str(year%100) + abSem(semester=semester)
    url = "https://coursebook.utdallas.edu/search/searchresults" + "/" + prefix + str(number) + "/term_" + term
    site = requests.get(url)

    soup = BeautifulSoup(site.content, "html.parser")
    professorList = soup.find_all("a", title=True, attrs ={"class" : "ptools-popover"})

    i = 0
    while i < len(professorList): #changes the professor list full of jank into just the names
        professorList[i] = professorList[i].get_text()
        i = i + 1
    return professorList

print(scrapeProf(prefix="cs",year=2020,semester="spring",number=2336))
