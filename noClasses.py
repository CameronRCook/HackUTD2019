#this file defines a function that checks whether or not the page is good
#returns boolean value

import requests
from bs4 import BeautifulSoup

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


print (isPageGood("https://coursebook.utdallas.edu/cp_c"))
print (isPageGood("https://coursebook.utdallas.edu/cp_cs"))