import json
import requests
#Alexa what professor has the best grades for cs2336
# Exports an object of type ClassGrade that

class ClassGrade:
    students = 0
    aStudents = 0
    percentA = 0
    professor = ""
    def __init__(self,name):
        self.professor = name


def gradeCheck(prefix,number):
    site = requests.get("https://raw.githubusercontent.com/bharatari/utd-grades/master/data/Spring%202019/spring2019.json")
    string = site.content
    data = json.loads(string)

    classList = []

    for section in data:
        if section['subj'] == prefix and section['num'] == number:
            students = 0
            aStudents = 0
            name = section['prof']

            classGrade = ClassGrade(name)
            
            if 'A+' in section['grades']:
                aStudents += int(section['grades']['A+'])
                students += int(section['grades']['A+'])
            if 'A' in section['grades']:
                aStudents += int(section['grades']['A'])
                students += int(section['grades']['A'])
            if 'A-' in section['grades']:
                aStudents += int(section['grades']['A-'])
                students += int(section['grades']['A-'])
            if 'B+' in section['grades']:
                students += int(section['grades']['B+'])
            if 'B' in section['grades']:
                students += int(section['grades']['B'])
            if 'B-' in section['grades']:
                students += int(section['grades']['B-'])
            if 'C+' in section['grades']:
                students += int(section['grades']['C+'])
            if 'C' in section['grades']:
                students += int(section['grades']['C'])
            if 'C-' in section['grades']:
                students += int(section['grades']['C-'])
            if 'D+' in section['grades']:
                students += int(section['grades']['D+'])
            if 'D' in section['grades']:
                students += int(section['grades']['D'])
            if 'D-' in section['grades']:
                students += int(section['grades']['D-'])
            if 'F' in section['grades']:
                students += int(section['grades']['F'])
            if 'W' in section['grades']:
                students += int(section['grades']['W'])

            classGrade.students = students
            classGrade.aStudents = aStudents
            if classGrade.students == 0:
                classGrade.percentA = 0
            else:
                classGrade.percentA = (classGrade.aStudents/classGrade.students)*100

            classList.append(classGrade)
    
    
    index = 0
    bestIndex = 0
    bestPercent = 0

    for item in classList:
        percent = classList[index].percentA
        if percent > bestPercent:
            bestPercent = percent
            bestIndex = index
        index += 1
    
    print(classList[bestIndex].professor)
    print(classList[bestIndex].percentA)
            

gradeCheck("EERF", "7V89")
# WE VIBING TONIGHT 