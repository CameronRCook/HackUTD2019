import re
from bs4 import BeautifulSoup
import requests

def createURL(coursePrefix, courseNum, semester, year) : #navigates to the coursebook page with the search criteria and returns creates a list of all the professors
    term = str(year%100) + abSem(semester=semester)
    url = "https://coursebook.utdallas.edu/search/searchresults" + "/" + coursePrefix + str(courseNum) + "/term_" + term

    return url

def abSem(semester) : #abbreviates the semester value to get the whole term ----returns the one letter abbreviation
    if semester.lower() == "fall":
        return "f"
    elif semester.lower() == "spring":
        return "s"
    elif semester.lower() == "summer":
        return "u"
    else :
        return "And the Lord spake, saying, 'First shalt thou take out the Holy Pin. Then, shalt thou count to three, no more, no less. Three shall be the number thou shalt count, and the number of the counting shall be three. Four shalt thou not count, nor either count thou two, excepting that thou then proceed to three. Five is right out! Once the number three, being the third number, be reached, then lobbest thou thy Holy Hand Grenade of Antioch towards thou foe, who being naughty in my sight, shall snuff it.'"

def isPageGood(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    zeroMatches = soup.find("div", attrs ={"class" : "zeromatches"}) #if page is bad the find() will return "<div class="zeromatches"><p>No course sections matched your search criteria.</p><p>Please try again using fewer or different search terms.</p></div>"

    badString = '<div class="zeromatches"><p>No course sections matched your search criteria.</p><p>Please try again using fewer or different search terms.</p></div>'

    #tests to see if there is string denoting no results is in the page
    if badString in str(zeroMatches) :
        return False
    else:
        return True

def scrapeOnline(coursePrefix, courseNum, semester, year) : #navigates to the coursebook page with the search criteria and returns creates a list of all the professors
    url = createURL(coursePrefix, courseNum, semester, year)
    if isPageGood(url):
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "html.parser")
        courseIDstr = (soup.find_all("a", attrs ={"class" : "stopbubble"}))
        i = 0
        for courseID in courseIDstr:
            text = courseIDstr[i].get_text()
            if text.split(".")[-1] == "0W1":
                return True #there is at least one online section
            i = i + 1
        return False #there are no online sections
    return None #the page was bad
    
     

print(scrapeOnline("geos", 1303, "spring", 2020)) #true
print(scrapeOnline("isns", 2367, "spring", 2020)) #true
print(scrapeOnline("cs", 2336, "spring", 2020)) #false