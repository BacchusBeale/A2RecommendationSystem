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

    for t in termList:
        print(t)

    nlp = nlptools.NLPTools()
    status = nlp.makeTFMatrix(termList=termList, documentList=coursenameData, saveAsCSV='courseTF.csv')
    print(f"Status: {status}")

def runtests():
    #test1()
    test2()


runtests()