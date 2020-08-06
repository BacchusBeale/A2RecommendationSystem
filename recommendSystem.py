import nlptools
import prepareData

class RSSystem:
    def __init__(self):
        self.rsdata = prepareData.RSData()
        self.nlp = nlptools.NLPTools()
        self.datadir = 'data'
        self.datafile = 'a2data.xlsx'
        self.sampleData = 'sampleData.csv'

        self.course = "course"
        self.courseColumn = self.rsdata.COURSENAME
        self.courseVocab = "courseVocab.txt"
        self.courseVocabIndex = "courseVocabIndex.csv"
        self.courseLookup = "courseNonZero.csv"
        self.courseTFIDF = "courseTFIDF.csv"

        self.reading = 'title'
        self.readingColumn = self.rsdata.TITLE
        self.sampleData = 'sampleData.csv'
        self.readingVocab = "readingVocab.txt"
        self.readingVocabIndex = "readingVocabIndex.csv"
        self.readingLookup = "readingNonZero.csv"
        self.readingTFIDF = "readingTFIDF.csv"
    
    def buildSystem(self):
        try:
            self.rsdata.makeRandomSampleCSV(datafile=f"{self.datadir}/{self.datafile}",
            percentFraction=0.01,
            saveAsCSV=f"{self.datadir}/{self.sampleData}")

        except BaseException as e:
            print("Build error: " + str(e))

    def doUserSearch(self):
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
    system = RSSystem()
    while keepRunning:
        res = userMenu()
        if res=='1':
            system.doUserSearch()
        if res=='2':    
            system.buildSystem()
        else:
            keepRunning=False

if __name__ == "__main__":
    # execute only if run as a script
    main()