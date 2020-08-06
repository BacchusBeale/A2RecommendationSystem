import nlptools
import prepareData
import search

class RSSystem:
    def __init__(self):
        self.rsdata = prepareData.RSData()
        self.nlp = nlptools.NLPTools()
        self.datadir = 'data'
        self.datafile = 'a2data.xlsx'
        self.sampleData = 'sampleData.csv'
        self.samplePercentage = 0.01
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
        print("Building system, please wait...may take a few minutes")
        try:
            print("Making random sample")
            self.rsdata.makeRandomSampleCSV(datafile=f"{self.datadir}/{self.datafile}",
            percentFraction=self.samplePercentage,
            saveAsCSV=f"{self.datadir}/{self.sampleData}")

            print("Processing course data...")
            res1 = prepareData.prepareWordData(datadir=self.datadir,
                csvfile=self.sampleData,
                dataColumnName=self.courseColumn,
                dataFilePrefix=self.course,
                numrows=None)

            print(f"Process status={res1}")

            print("Processing reading data...")
            res2 = prepareData.prepareWordData(datadir=self.datadir,
                csvfile=self.sampleData,
                dataColumnName=self.readingColumn,
                dataFilePrefix=self.reading,
                numrows=None)

            print(f"Process status={res2}")
            
        except BaseException as e:
            print("Build error: " + str(e))

    def doUserSearch(self, contentBased=True):
        userquery = input("Enter search keywords: ")
        results=[]
        topN = 5
        if contentBased:
            results = search.searchContentBased(numResults=topN)
        else:
            results = search.searchCollaborationBased(numResults=topN)

        print("You searched for: " + userquery)
        print(f"Your top {topN} results are:")
        
        for r in results:
            print(str(r))

def userMenu():
    print('''
    Welcome to Recommendation System for University Reading Resources
    0. Build system
    1. Content-based search
    2. Collaboration-based search
    3. Quit
    ''')
    choice = input("Enter menu option: ")
    return choice


def main():
    keepRunning = True
    system = RSSystem()
    while keepRunning:
        res = userMenu()
        if res=='0':
            system.buildSystem()
        elif res=='1':
            system.doUserSearch(contentBased=True)
        elif res=='2':    
            system.doUserSearch(contentBased=False)
        elif res=='3':
            print("Have a nice day!")
            keepRunning=False

if __name__ == "__main__":
    main()