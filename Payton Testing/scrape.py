#This uses urlopen to access a site, then uses BeautifulSoup to get the
#HTML from that site, and then cuts out all of the non-text
import re
from bs4 import BeautifulSoup
import requests

class Professor:
    person = ""
    quality = ""
    takeAgain = ""
    difficulty = ""
    def __init__(self, name):
        self.person = name

def abSem(semester) : #abbreviates the semester value to get the whole term ----returns the one letter abbreviation
    if semester.lower() == "fall":
        return "f"
    elif semester.lower() == "spring":
        return "s"
    elif semester.lower() == "summer":
        return "u"
    else :
        return "And the Lord spake, saying, 'First shalt thou take out the Holy Pin. Then, shalt thou count to three, no more, no less. Three shall be the number thou shalt count, and the number of the counting shall be three. Four shalt thou not count, nor either count thou two, excepting that thou then proceed to three. Five is right out! Once the number three, being the third number, be reached, then lobbest thou thy Holy Hand Grenade of Antioch towards thou foe, who being naughty in my sight, shall snuff it.'"

def createURL(prefix,year,semester,number) : #navigates to the coursebook page with the search criteria and returns creates a list of all the professors
    term = str(year%100) + abSem(semester=semester)
    url = "https://coursebook.utdallas.edu/search/searchresults" + "/" + prefix + str(number) + "/term_" + term

    return url

def scrapeProf(url) : #navigates to the coursebook page with the search criteria and returns creates a list of all the professors
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    professorList = soup.find_all("a", title=True, attrs ={"class" : "ptools-popover"})

    i = 0
    while i < len(professorList): #changes the professor list full of jank into just the names
        professorList[i] = professorList[i].get_text()
        i = i + 1
    return professorList

def getRating(name):

    professor = Professor(name)
    #Initial Search for the Professor
    URL = "https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=The+University+of+Texas+at+Dallas&schoolID=1273&query=" + name
    site = requests.get(URL)
    
    soup = BeautifulSoup(site.content, 'html.parser')
    search = soup.find("a", href=re.compile("ShowRatings"))
    URL = "https://www.ratemyprofessors.com" + search.get('href') # new link
    
    
    #Get Number from the actual professor page.
    site = requests.get(URL)
    soup = BeautifulSoup(site.content, 'html.parser')
    search = soup.find_all('div', attrs={'class':'grade'})
    
    quality = search[0].get_text()
    takeAgain = search[1].get_text()
    difficulty = search[2].get_text()

    professor.quality = re.sub('\s+','',quality)
    professor.takeAgain = re.sub('\s+','',takeAgain)
    professor.difficulty = re.sub('\s+','',difficulty)


    return professor

def topProf(professorList):
    index = 0;
    bestIndex = 0;
    bestQuality = 0.0

    for professor in professorList:
        string = professorList[index].quality
        quality = float(string)
        if quality > bestQuality:
            bestQuality = quality
            bestIndex = index
            index += 1
    
    return professorList[bestIndex]

def bestProf()

#absem
#create url
#scrap prof to array
#for each prof in array get rating and output to new array
#find top prof and return prof
