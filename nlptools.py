from sklearn_pandas import DataFrameMapper, gen_features, CategoricalImputer
import sklearn.preprocessing
import pandas as pd
import numpy as np
import nltk
from nltk import word_tokenize
import string
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

import math

# NLP methods
class NLPTools:
    def toLowerCase(self,text):
        return str(text).lower()

    def applyStemming(self,wordList, usePorter=True): # else use Lancaster
        stems = []
        stemmer = PorterStemmer()
        if not usePorter:
            stemmer = LancasterStemmer()

        for w in wordList:
            s = stemmer.stem(w)
            stems.append(s)

        return stems

    def applyLemmatisation(self, wordList):
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmaList=[]
        for w in wordList:
            postag = self.get_wordnet_pos(w)
            lemma = wordnet_lemmatizer.lemmatize(w,pos=postag)
            lemmaList.append(lemma)

        return lemma

    def getPartOfSpeech(self,singleWord):
        postag = nltk.pos_tag(singleWord) # returns tuple (word,tag)
        return postag

    # Note: Adapted to convert POS tags
    # https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
# https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html
    def get_wordnet_pos(self,singleWord):
    # """Map POS tag to first character lemmatize() accepts"""
        word, postag = self.getPartOfSpeech(singleWord)
        print(f"Wordnet POS: {word} -> {postag}")
        wordnet_tag = str(postag[0]) # first character
        return wordnet_tag.lower()

#https://machinelearningmastery.com/clean-text-machine-learning-python/

    def cleanText2List(self, textString):
        text=str(textString)
        lowercase = text.lower()
        # include only words with characters a-z or A-Z
        words = re.split(r'\W+', lowercase)
        punct = string.punctuation
        noPunctuation = []
        for w in words:
            w = w.strip() # remove whitespace
            for p in punct:
                w.replace(p,"") # remove punctuation
            
            if len(w)>0: # no empty strings
                noPunctuation.append(w)
        
        return words
        
    def removeStopwords(self, wordList):
        stoplist = set(stopwords.words('english'))
        mainwords = []
        for w in wordList:
            if w not in stoplist:
                mainwords.append(w)
        return mainwords

    def makeVocabularyFile(self, dataList, filePath):
        # check all items are strings
        # ??? UnicodeEncodeError: 'charmap' codec can't encode character '\u014d' in position 2049: character maps to <undefined>
        strList = []
        for d in dataList:
            strList.append(str(d))
        fulltext = ' '.join(strList)
        cleanWordList = self.cleanText2List(fulltext)
        usefulWords = self.removeStopwords(cleanWordList)
        wordSet = set(usefulWords)
        wordSorted=sorted(wordSet)
        numWords = len(wordSorted)
        textNewLines = '\n'.join(wordSorted)
        # https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
        # does not work: textNewLines.replace('\u014d','') # remove unicode error
        # http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python

        with open(filePath, 'w') as f:
            for char in textNewLines:
                try:
                    f.write(char)
                except BaseException as e:
                    print(str(e))
            
        return numWords

# https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/#:~:text=tf%2Didf%20is%20a%20weighting,considered%20to%20be%20more%20important.

    def termFrequency(self, term, document):
        document=str(document)
        term=str(term)
        term = term.lower()
        document=document.lower()
        words = document.split()
        frequency = words.count(term)
        return frequency

    def documentLength(self, document):
        document=str(document)
        words = document.split()
        return len(words)

    def normalizedTermFrequency(self, term, document):
        tf = float(self.termFrequency(term, document))
        n = float(self.documentLength(document))
        return tf/n

    # number of documents containing term
    def numberDocumentsWithTerm(self,term, documentList):
        frequency = 0
        term=str(term)
        term=term.lower()
        for d in documentList:
            # must be string to split
            d = str(d)
            words = d.split()
            if term in words:
                frequency+=1

        return frequency

    def inverseDocumentFrequency(self, docFrequency, numDocuments):
        # prevent divide by zero or log(0) errors
        if numDocuments==0 or docFrequency==0:
            return 0
        idf = math.log2(numDocuments/docFrequency)
        return idf

    def scoreTFIDF(self, term, document, documentList):
        normTF = self.normalizedTermFrequency(term, document)
        docfreq=self.numberDocumentsWithTerm(term, documentList)
        numdocs=len(documentList)
        idf = self.inverseDocumentFrequency(docfreq, numdocs)
        score = normTF * idf
        return score

# https://cs231n.github.io/python-numpy-tutorial/#:~:text=started%20with%20Numpy.-,Arrays,the%20array%20along%20each%20dimension.

    def makeTFMatrix(self, termList, documentList, saveAsCSV='data/tf.csv'):
        try:
            numTerms = len(termList)
            numDocs=len(documentList)
            # terms=rows, docs=cols
            tfMatrix = np.zeros((numTerms,numDocs))
            for t in range(numTerms):
                for d in range(numDocs):
                    term=termList[t]
                    doc=documentList[d]
                    tfValue = self.normalizedTermFrequency(term,doc)
                    print(f"tf: {tfValue}") # debug
                    tfMatrix[t,d] = tfValue

            np.savetxt(saveAsCSV, tfMatrix)
        except BaseException as e:
            print(str(e))
            return False

        return True
        

    def makeIDFMatrix(self, termList, documentList, saveAsCSV='data/idf.csv'):
        try:
            numTerms = len(termList)
            numDocs=len(documentList)
            # terms=rows, docs=cols
            idfMatrix = np.zeros((numTerms,1)) # one value for each term
            for t in range(numTerms):
                nextTerm=termList[t]
                docfreq = self.numberDocumentsWithTerm(nextTerm, documentList)
                idfScore = self.inverseDocumentFrequency(docfreq, numDocs)
                idfMatrix[t] = idfScore

            np.savetxt(saveAsCSV, idfMatrix)
        except BaseException as e:
            print(str(e))
            return False

        return True

    def makeTFIDFScoreMatrix(self, termList, documentList, saveAsCSV='data/tfidfScores.csv'):
        try:
            numTerms = len(termList)
            numDocs=len(documentList)
            # terms=rows, docs=cols
            scoreMatrix = np.zeros((numTerms,numDocs)) # one value for each term
            for t in range(numTerms):
                nextTerm=termList[t]
                docfreq = self.numberDocumentsWithTerm(nextTerm, documentList)
                idfScore = self.inverseDocumentFrequency(docfreq, numDocs)
                
                for d in range(numDocs):
                    term=termList[t]
                    doc=documentList[d]
                    tfValue = self.normalizedTermFrequency(term,doc)
                    
                    tfidfScore = tfValue*idfScore
                    scoreMatrix[t,d]=tfidfScore

            np.savetxt(saveAsCSV, scoreMatrix)
        except BaseException as e:
            print(str(e))
            return False

        return True

    def readListFile(self, filename):
        termList = []
        with open(filename,'r') as f:
            for t in f.readlines():
                t = t.strip()
                if len(t)>0:
                    termList.append(t)
        return termList