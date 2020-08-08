from prepareData import RSData
import pandas as pd 
import nlptools

class SearchEngine:
    def __init__(self, datadir, datacsv, courseVocab, titleVocab,
        courseVocabIndex,titleVocabIndex,courseNonzero,titleNonzero):
        self.datafile=datadir+"/"+datacsv
        self.courseVocab=datadir+"/"+courseVocab
        self.courseVocabIndex=datadir+"/"+courseVocabIndex
        self.courseNonzero=datadir+"/"+courseNonzero
        self.titleVocab=datadir+"/"+titleVocab
        self.titleVocabIndex=datadir+"/"+titleVocabIndex
        self.titleNonzero=datadir+"/"+titleNonzero
        self.nlp = nlptools.NLPTools()
        self.data = RSData()
        self.isLoaded=False

        self.courseVocabIndexList = []
        self.courseNonzeroData = pd.DataFrame()
        self.titleVocabIndexList = []
        self.titleNonzeroData = pd.DataFrame()
        self.nonzeroHeader=["term","termIndex","doc","docIndex","score"]

#http://www.tfidf.com/
#https://honingds.com/blog/pandas-read_csv/#:~:text=Load%20csv%20with%20no%20header,generated%20integer%20values%20as%20header.

    def loadData(self):
        try:
            res = self.data.loadCSVData(datafile=self.datafile, numrows=None)
            self.isLoaded=res
            self.courseVocabIndexList = self.nlp.readListFile(filename=self.courseVocabIndex)
            self.courseNonzeroData = pd.read_csv(self.courseNonzero, header=None, names=self.nonzeroHeader)
            self.titleVocabIndexList = self.nlp.readListFile(filename=self.titleVocabIndex)
            self.titleNonzeroData = pd.read_csv(self.titleNonzero, header=None, names=self.nonzeroHeader)
            
        except BaseException as e:
            print(str(e))
            self.isLoaded=False
        return self.isLoaded

    def resultFormat(self, dataIndex=0, score=0.0):
        title=self.data.getDataItemAsString(rowIndex=dataIndex, columnName=RSData.TITLE)
        sub=self.data.getDataItemAsString(rowIndex=dataIndex, columnName=RSData.SUBTITLE)
        authors=self.data.getDataItemAsString(rowIndex=dataIndex, columnName=RSData.AUTHORS)
        result=f"Title:{title}| subtitle:{sub}| authors:{authors}| score: {score}"
        return result

    def searchContentBased(self,userQuery="",numResults=5):
        results=[]
        
        try:
            words = userQuery.split(sep=" ")
            # find docs with term in it
            matches=[]
            for w in words:
                w=w.lower()
                if w in self.courseVocabIndexList:
                    i = self.courseVocabIndexList.index(w)
                    line = self.courseVocabIndexList[i]
                    matches.append(line)

            docScoreDict={}
            # eg abnormal,486
            for m in matches:
                item = m.split(sep=",")
                n=len(item)
                if n>1:
                    term = item[0]
                    print(f"Keyword: {term}")
                    docIndexes = item[1:]
                    # find title terms from doc Index
                    for d in docIndexes:
                        doctitle = self.data.getDataItemAsString(int(d),columnName=RSData.TITLE)
                        doc = str(doctitle)
                        doc=doc.lower()
                        docwords = doc.split(sep=" ")
                        for dw in docwords:
                            docmatches = self.titleNonzeroData.loc["term"==dw]
                            for x in docmatches:
                                docNumber = x["docIndex"]
                                
                                docScore=x["score"]
                                docScoreDict[str(docNumber)]=docScore
# https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.

            sortDict = sorted(docScoreDict.items(), key=lambda x: x[1], reverse=True)
            nItems = len(sortDict.keys())
            print(f"Num items: {nItems}")
            itemCount=0
            for item in sortDict:
                itemCount+=1
                # max results
                if itemCount>numResults:
                    break
                di = int(item)
                sc = sortDict[item]
                res = self.resultFormat(dataIndex=di,score=sc)
                results.append(res)
            

        except BaseException as e:
            print(str(e))
        
        return results

    def searchCollaborationBased(self,userQuery="",numResults=5):
        results=[]
        index=3
        res = self.resultFormat(dataIndex=index,score=0.45)
        results.append(res)
        return results