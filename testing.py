import prepareData
import nlptools

def test1():
    xlsfile='data/a2data.xlsx'
    nrows=10
    nlp = nlptools.NLPTools()
    rs = prepareData.RSData()
    rs.loadXLSXData(datafile=xlsfile, numrows=nrows)
    # input data: CourseName
    coursenameData = rs.getColumnDataAsList(prepareData.RSData.COURSENAME)
    nWords = nlp.makeVocabularyFile(dataList=coursenameData, filePath='data/courseVocab.txt')
    print(f"Num words={nWords}")

    # output data: CourseName
    readingListData = rs.getColumnDataAsList(prepareData.RSData.TITLE)
    nWords = nlp.makeVocabularyFile(dataList=readingListData, filePath='data/readingListVocab.txt')
    print(f"Num words={nWords}")

def test2():
    xlsfile='data/a2data.xlsx'
    nrows=10
    nlp = nlptools.NLPTools()
    rs = prepareData.RSData()
    rs.loadXLSXData(datafile=xlsfile, numrows=nrows)
    # input data: CourseName
    coursenameData = rs.getColumnDataAsList(prepareData.RSData.COURSENAME)
    nWords = nlp.makeVocabularyFile(dataList=coursenameData, filePath='data/courseVocab.txt')
    print(f"Num words={nWords}")

    courseListFile = 'data/courseVocab.txt'
    termList = []
    with open(courseListFile,'r') as f:
        for t in f.readlines():
            t = t.strip()
            if len(t)>0:
                termList.append(t)

    # for t in termList:
    #     print(t)

    nlp = nlptools.NLPTools()
    status = nlp.makeTFMatrix(termList=termList, documentList=coursenameData, saveAsCSV='data/courseTF.csv')
    print(f"Status 1: {status}")

    status = nlp.makeIDFMatrix(termList=termList, documentList=coursenameData, saveAsCSV='data/courseIDF.csv')
    print(f"Status 2: {status}")

    status = nlp.makeTFIDFScoreMatrix(termList=termList, documentList=coursenameData, saveAsCSV='data/courseTFIDF.csv')
    print(f"Status 3: {status}")

def test3():
    xlsfile='data/a2data.xlsx'
    
    rs = prepareData.RSData()
    sampleDataFile = 'data/sample.csv'
    res = rs.makeRandomSampleCSV(datafile=xlsfile,percentFraction=0.1,saveAsCSV=sampleDataFile)
    print(f"Made sample data = {res}")
    return res

def test4():
    nlp = nlptools.NLPTools()
    rs = prepareData.RSData()
    sampleDataFile = 'data/sample.csv'
    rs.loadCSVData(datafile=sampleDataFile, numrows=None) # all rows
    # input data: CourseName
    coursenameData = rs.getColumnDataAsList(prepareData.RSData.COURSENAME)
    nWords = nlp.makeVocabularyFile(dataList=coursenameData, filePath='data/courseVocab.txt')
    print(f"Num words={nWords}")

    # output data: CourseName
    readingListData = rs.getColumnDataAsList(prepareData.RSData.TITLE)
    nWords = nlp.makeVocabularyFile(dataList=readingListData, filePath='data/readingListVocab.txt')
    print(f"Num words={nWords}")



def runtests():
    #test1()
    #test2()
    test3()

runtests()