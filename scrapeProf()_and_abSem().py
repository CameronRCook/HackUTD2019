#This uses urlopen to access a site, then uses BeautifulSoup to get the
#HTML from that site, and then cuts out all of the non-text

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
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    term = str(year%100) + abSem(semester=semester)
    url = "https://coursebook.utdallas.edu/search/searchresults" + "/term_" + term + "/cp_" + prefix + "/" + str(number)
    site = urlopen(url)
    soup = BeautifulSoup(site, "html.parser")
    visible_text = soup.getText()
    
    return visible_text

print(scrapeProf(prefix="cs",year=2020,semester="summer",number=2337))
