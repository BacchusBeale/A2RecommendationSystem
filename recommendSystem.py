import pandas as pd
import nltk

class Course:
    def __init__(self):
        self.courseName=""

class ReadingMaterial:
    def __init__(self,title,resourceType,isbn,issn,doi,
    subtitle,editors,publisher,authors):
        self.title=title
        self.resourceType=resourceType
        self.isbn=isbn
        self.issn=issn
        self.doi=doi
        self.subtitle=subtitle
        self.editors=editors
        self.publisher=publisher
        self.authors=authors

def buildSystem():
    pass

def prepareData():
    pass

def getExtraData():
    pass

def trainStatsModel():
    pass

def trainContentModel():
    pass

def trainCollaborativeModel():
    pass

def testStatsModel():
    pass

def testContentModel():
    pass

def testCollaborativeModel():
    pass

def predictStatsModel(numResults=5):
    pass

def predictContentModel(numResults=5):
    pass

def predictCollaborativeModel(numResults=5):
    pass

def doUserSearch():
    userquery = input("Enter search keywords: ")
    return "You searched for: " + userquery

def userMenu():
    print('''
    Welcome to Recommendation System for University Reading Resources
    1. Initilisation: Build and train system
    2. User Queries: Search by keywords
    0. Quit
    ''')
    choice = input("Enter menu option: ")
    return choice


def run():
    keepRunning = True
    while keepRunning:
        res = userMenu()
        if res=='1':
            output = doUserSearch()
            print(output)
        if res=='2':
            keepRunning=False

run()