#https://medium.com/@galhever/an-easy-way-for-data-preprocessing-sklearn-pandas-56bc1e6e81d2
#https://en.wikipedia.org/wiki/International_Standard_Book_Number
#https://www.journaldev.com/32797/python-convert-numpy-array-to-list
#https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column
#https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
#https://www.datacamp.com/community/tutorials/stemming-lemmatization-python

from sklearn_pandas import DataFrameMapper, gen_features, CategoricalImputer
import sklearn.preprocessing
import pandas as pd
import numpy as np
import nltk
from nltk import word_tokenize
import string
import re
from nltk.corpus import stopwords

import nlptools

class RSData:
    #COL NAMES
    COURSENAME = 'COURSENAME'
    TITLE = 'TITLE'
    RESOURCE_TYPE = 'RESOURCE_TYPE'
    SUBTITLE = 'SUBTITLE'
    ISBN10S = 'ISBN10S'
    ISBN13S = 'ISBN13S'
    ISSNS = 'ISSNS'
    EISSNS = 'EISSNS'
    DOI = 'DOI'
    EDITION = 'EDITION'
    EDITORS = 'EDITORS'
    PUBLISHER = 'PUBLISHER'
    DATES = 'DATES'
    VOLUME = 'VOLUME'
    PAGE_END = 'PAGE_END'
    AUTHORS = 'AUTHORS'

    def __init__(self):
        self.rsdata = pd.DataFrame()
        self.isLoaded = False

    def loadXLSXData(self, datafile, numrows=None):
        try:
            self.rsdata = pd.read_excel(datafile, nrows=numrows)
            self.isLoaded = True
        except BaseException as e:
            print(str(e))
            self.isLoaded = False
        return self.isLoaded

    def loadCSVData(self, datafile, numrows=None):
        try:
            self.rsdata = pd.read_csv(datafile, nrows=numrows)
            self.isLoaded = True
        except BaseException as e:
            print(str(e))
            self.isLoaded = False
        return self.isLoaded

    def makeRandomSampleCSV(self, datafile, percentFraction, saveAsCSV):
        status = self.loadXLSXData(datafile=datafile, numrows=None)
        if status:
            try:
                sampleData = self.rsdata.sample(frac=percentFraction)
                sampleData.to_csv(saveAsCSV, index=False) # no row ids
            except BaseException as e:
                print(str(e))
                status=False
        return status


    def getColumnDataAsList(self, colname):
        dataVector = self.rsdata[colname].tolist()
        return dataVector
    
    def getColumnNames(self):
        return self.rsdata.keys()

    def dataSummary(self):
        return self.rsdata.info()


import os
# main processing functions
# nrows=None means all data
def preprocessData(datadir='data',
    xlsfile='a2data.xlsx',
    courseDataFile='courseVocab.txt',
    readingDataFile='readingListVocab.txt',
    nrows=10):

    try:
        if not os.path.exists(datadir):
            os.mkdir(datadir)
        
        nlp = nlptools.NLPTools()
        rs = RSData()
        rs.loadXLSXData(datafile=f'{datadir}/{xlsfile}', numrows=nrows)
        # input data: CourseName
        coursenameData = rs.getColumnDataAsList(RSData.COURSENAME)
        nWords = nlp.makeVocabularyFile(dataList=coursenameData, 
        filePath=f'{datadir}/{courseDataFile}')
        print(f"Num words={nWords}")

        # output data: Title
        readingListData = rs.getColumnDataAsList(RSData.TITLE)
        nWords = nlp.makeVocabularyFile(dataList=readingListData, 
        filePath=f'{datadir}/{readingDataFile}')
        print(f"Num words={nWords}")

    except BaseException as e:
        print("Processing error: " + str(e))
        return False

    return True
    
def processRandomSample(datadir='data',
    xlsfile='a2data.xlsx',
    sampleDataFile='sampleData.csv',
    percentFraction=0.01):
    try:
        if not os.path.exists(datadir):
            os.mkdir(datadir)

        datapath=f'{datadir}/{xlsfile}'
        rs = RSData()
        sampleDataPath = f'{datadir}/{sampleDataFile}'
        
        res = rs.makeRandomSampleCSV(datafile=datapath,
        percentFraction=percentFraction,
        saveAsCSV=sampleDataPath)

        print(f"Made sample data = {res}")
    except BaseException as e:
        print("Processing error: " + str(e))
        return False

    return True

def prepareWordData(datadir='data',
    csvfile='sample.csv',
    dataColumnName='COURSENAME',
    dataFilePrefix='course',
    numrows=None):
    try:
        rs = RSData()
        nlp = nlptools.NLPTools()
        datapath = f'{datadir}/{csvfile}'

        if not rs.loadCSVData(datafile=datapath,numrows=numrows):
            raise BaseException("Load error")
        
        vocabFile=f'{datadir}/{dataFilePrefix}Vocab.txt'
        columnData = rs.getColumnDataAsList(colname=dataColumnName)
        nWords = nlp.makeVocabularyFile(dataList=columnData,filePath=vocabFile)
        print(f"{dataColumnName} words= {nWords}")

        dataList = nlp.readListFile(vocabFile)
        indexFile=f'{datadir}/{dataFilePrefix}VocabIndex.csv'
        res = nlp.createVocabDocumentIndex(docList=columnData, 
        vocabList=dataList, saveAsCSV=indexFile)
        print(f"list size={res}")

        tfidfFile=f'{datadir}/{dataFilePrefix}TFIDF.csv'
        nzFile=f'{datadir}/{dataFilePrefix}NonZero.csv'
        status = nlp.makeTFIDFScoreMatrix(termList=vocabFile, 
        documentList=columnData,
        saveNonZero=nzFile, 
        saveAsCSV=tfidfFile)
        print(f"Course terms: {status}")

    except BaseException as e:
        print("Processing error: " + str(e))
        return False

    return True


""" 
https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/#:~:text=tf%2Didf%20is%20a%20weighting,considered%20to%20be%20more%20important.
0   ID             68530 non-null  int64
 1   COURSENAME     68530 non-null  object
 2   ITEM_COUNT     59256 non-null  float64
 3   TITLE          68183 non-null  object
 4   RESOURCE_TYPE  67059 non-null  object
 5   SUBTITLE       68484 non-null  object
 6   ISBN10S        13482 non-null  object
 7   ISBN13S        19355 non-null  object
 8   ISSNS          22015 non-null  object
 9   EISSNS         5488 non-null   object
 10  DOI            4864 non-null   object
 11  EDITION        12677 non-null  object
 12  EDITORS        64694 non-null  object
 13  PUBLISHER      32535 non-null  object
 14  DATES          46645 non-null  object
 15  VOLUME         11947 non-null  object
 16  PAGE_END       14351 non-null  object
 17  AUTHORS        14891 non-null  object
 18  Unnamed: 18    6884 non-null   object
dtypes: float64(1), int64(1), object(17)

 """