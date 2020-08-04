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
    # 1% test sample = 0.01*65000
    frac=0.01
    res = rs.makeRandomSampleCSV(datafile=xlsfile,percentFraction=frac,saveAsCSV=sampleDataFile)
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
    print(f"Course words={nWords}")

    # output data: CourseName
    readingListData = rs.getColumnDataAsList(prepareData.RSData.TITLE)
    nWords = nlp.makeVocabularyFile(dataList=readingListData, filePath='data/readingListVocab.txt')
    print(f"Title words={nWords}")

    courseTerms = nlp.readListFile(filename='data/courseVocab.txt')
    status = nlp.makeTFIDFScoreMatrix(termList=courseTerms, documentList=coursenameData, saveAsCSV='data/courseTFIDF.csv')
    print(f"Course terms: {status}")

    titleTerms = nlp.readListFile(filename='data/readingListVocab.txt')
    status = nlp.makeTFIDFScoreMatrix(termList=titleTerms, documentList=readingListData, saveAsCSV='data/readingListTFIDF.csv')
    print(f"Title terms: {status}")



def runtests():
    #test1()
    #test2()
    #test3()
    test4()

runtests()