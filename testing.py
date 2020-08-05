import prepareData
import nlptools

def test1():
    xlsfile='data/a2data.xlsx'
    rs = prepareData.RSData()
    sampleDataFile = 'data/sample.csv'
    # 1% test sample = 0.01*65000
    frac=0.01
    res = rs.makeRandomSampleCSV(datafile=xlsfile,percentFraction=frac,saveAsCSV=sampleDataFile)
    print(f"Made sample data = {res}")
    return res

def test2():
    nlp = nlptools.NLPTools()
    rs = prepareData.RSData()
    sampleDataFile = 'data/sample.csv'
    rs.loadCSVData(datafile=sampleDataFile, numrows=None) # all rows
    # input data: CourseName
    coursenameData = rs.getColumnDataAsList(prepareData.RSData.COURSENAME)
    nWords = nlp.makeVocabularyFile(dataList=coursenameData, filePath='data/courseVocab.txt')
    print(f"Course words={nWords}")

    # output data: Title
    readingListData = rs.getColumnDataAsList(prepareData.RSData.TITLE)
    nWords = nlp.makeVocabularyFile(dataList=readingListData, filePath='data/readingListVocab.txt')
    print(f"Title words={nWords}")

    nlp = nlptools.NLPTools()
    courseTerms = nlp.readListFile(filename='data/courseVocab.txt')
    status = nlp.makeTFIDFScoreMatrix(termList=courseTerms, documentList=coursenameData, saveAsCSV='data/courseTFIDF.csv')
    print(f"Course terms: {status}")

    titleTerms = nlp.readListFile(filename='data/readingListVocab.txt')
    status = nlp.makeTFIDFScoreMatrix(termList=titleTerms, documentList=readingListData, saveAsCSV='data/readingListTFIDF.csv')
    print(f"Title terms: {status}")

def runtests():
    # test1()
    test2()
    
  
runtests()