#just gets the list of professors for a course

import re
from bs4 import BeautifulSoup
import requests

def profList(coursePrefix, courseNum, semester, year) :
    url = createURL(coursePrefix, courseNum, semester, year)
    if isPageGood(url) :
        return  scrapeProf(url) #this will return a list of prof names with no middle names (-Staff- is deleted)
    else:
        return None