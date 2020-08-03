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
        wordnet_tag = postag[0] # first character
        return wordnet_tag.lower()

#https://machinelearningmastery.com/clean-text-machine-learning-python/

    def cleanText2List(self, textString):
        lowercase = textString.lower()
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
        fulltext = ' '.join(dataList)
        cleanWordList = self.cleanText2List(fulltext)
        usefulWords = self.removeStopwords(cleanWordList)
        wordSet = set(usefulWords)
        wordSorted=sorted(wordSet)
        numWords = len(wordSorted)
        with open(filePath, 'w') as f:
            for w in wordSorted:
                f.write(w+"\n") # add new lines
        return numWords

# https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/#:~:text=tf%2Didf%20is%20a%20weighting,considered%20to%20be%20more%20important.

    def termFrequency(self, term, document):
        words = document.split()
        frequency = words.count(term)
        return frequency

    def documentLength(self, document):
        words = document.split()
        return len(words)

    def nomralizedTermFrequency(self, term, document):
        tf = float(self.termFrequency(term, document))
        n = float(self.documentLength(document))
        return tf/n

    # number of documents containing term
    def numberDocumentsWithTerm(self,term, documentList):
        frequency = 0
        for d in documentList:
            words = d.split()
            if term in words:
                frequency+=1

        return frequency

    def inverseDocumentFrequency(self, docFrequency, numDocuments):
        idf = math.log2(numDocuments/docFrequency)
        return idf

    def scoreTFIDF(self, term, documentList):
        pass
