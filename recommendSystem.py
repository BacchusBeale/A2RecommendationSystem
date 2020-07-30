# http://www.nltk.org/ 
import dataModels
import prepareData

def buildSystem():
    pass

def doUserSearch():
    userquery = input("Enter search keywords: ")
    return "You searched for: " + userquery

def userMenu():
    print('''
    Welcome to Recommendation System for University Reading Resources
    1. User Queries: Search by keywords
    2. Build system
    any other input. Quit
    ''')
    choice = input("Enter menu option: ")
    return choice


def main():
    keepRunning = True
    while keepRunning:
        res = userMenu()
        if res=='1':
            output = doUserSearch()
            print(output)
        if res=='2':
            buildSystem()
        else:
            keepRunning=False

if __name__ == "__main__":
    # execute only if run as a script
    main()