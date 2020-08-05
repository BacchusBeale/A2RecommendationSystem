import prepareData
import nlptools

def test1():
    xlsfile='data/a2data.xlsx'
    rs = prepareData.RSData()
    sampleDataFile = 'data/sample.csv'
    # 10% test sample = 0.1*65000+
    frac=0.1
    res = rs.makeRandomSampleCSV(datafile=xlsfile,percentFraction=frac,saveAsCSV=sampleDataFile)
    print(f"Made sample data = {res}")
    return res

def test2():
    nlp = nlptools.NLPTools()
    rs = prepareData.RSData()
    sampleDataFile = 'data/sample.csv'
    rs.loadCSVData(datafile=sampleDataFile, numrows=None) # all rows

    # all passed...
    # input data: CourseName
    coursenameData = rs.getColumnDataAsList(prepareData.RSData.COURSENAME)
    # nWords = nlp.makeVocabularyFile(dataList=coursenameData, filePath='data/courseVocab.txt')
    # print(f"Course words={nWords}")
    courseVocabList = nlp.readListFile(filename='data/courseVocab.txt')
    nlp.createVocabDocumentIndex(docList=coursenameData, vocabList=courseVocabList, saveAsCSV="data/courseVocabIndex.csv")
    # # output data: Title
    readingListData = rs.getColumnDataAsList(prepareData.RSData.TITLE)
    # nWords = nlp.makeVocabularyFile(dataList=readingListData, filePath='data/readingListVocab.txt')
    # print(f"Title words={nWords}")
    readingVocabList = nlp.readListFile(filename='data/readingListVocab.txt')
    nlp.createVocabDocumentIndex(docList=readingListData, vocabList=readingVocabList, saveAsCSV="data/readingVocabIndex.csv")
    
    # nlp = nlptools.NLPTools()
    # courseTerms = nlp.readListFile(filename='data/courseVocab.txt')
    # status = nlp.makeTFIDFScoreMatrix(termList=courseTerms, documentList=coursenameData,
    # saveNonZero='data/nonzeroCourse.csv', saveAsCSV='data/courseTFIDF.csv')
    # print(f"Course terms: {status}")

    # titleTerms = nlp.readListFile(filename='data/readingListVocab.txt')
    # status = nlp.makeTFIDFScoreMatrix(termList=titleTerms, documentList=readingListData,
    # saveNonZero='data/nonzeroTitle.csv', saveAsCSV='data/readingListTFIDF.csv')
    # print(f"Title terms: {status}")



def runtests():
    #test1()
    test2()
    
runtests()