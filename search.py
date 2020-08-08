from prepareData import RSData

class Search:
    def __init__(self, datacsv, courseVocab, titleVocab,
        courseVocabIndex,titleVocabIndex,courseNonzero,titleNonzero):
        self.datafile=datacsv
        self.courseVocab=courseVocab
        self.courseVocabIndex=courseVocabIndex
        self.courseNonzero=courseNonzero
        self.titleVocab=titleVocab
        self.titleVocabIndex=titleVocabIndex
        self.titleNonzero=titleNonzero

        self.data = RSData()
        self.isLoaded=False

    def loadData(self):
        try:
            res = self.data.loadCSVData(datafile=self.datafile, numrows=None)

            self.isLoaded=res
        except BaseException as e:
            print(str(e))
            self.isLoaded=False
        return self.isLoaded

    def resultFormat(self, dataIndex=0, score=0.0):
        title=self.data.getDataItemAsString(rowIndex=dataIndex, columnName=RSData.TITLE)
        isbn=self.data.getDataItemAsString(rowIndex=dataIndex, columnName=RSData.ISBN10S)
        authors=self.data.getDataItemAsString(rowIndex=dataIndex, columnName=RSData.AUTHORS)
        result=f"{title}: {isbn}| {authors}| {score}"
        return result

    def searchContentBased(self,userQuery="",numResults=5):
        results=[]
        index=5
        res = self.resultFormat(dataIndex=index,score=0.75)
        results.append(res)
        return results

    def searchCollaborationBased(self,userQuery="",numResults=5):
        results=[]
        index=3
        res = self.resultFormat(dataIndex=index,score=0.45)
        results.append(res)
        return results