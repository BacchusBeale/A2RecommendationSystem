#https://medium.com/@galhever/an-easy-way-for-data-preprocessing-sklearn-pandas-56bc1e6e81d2
#https://en.wikipedia.org/wiki/International_Standard_Book_Number
#https://isbnsearch.org/
#https://isbnsearch.org/search?s=TOMSAWYER

from sklearn_pandas import DataFrameMapper, gen_features, CategoricalImputer
import sklearn.preprocessing
import pandas as pd
import numpy as np

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

    def __init__(self, datapath):
        self.csvpath = datapath
        self.rsdata = None

    def preprocessData(self):
        self.rsdata = pd.read_csv(self.csvpath)

    def dataSummary(self):
        return self.rsdata.info()


def run():
    rs = RSData(datapath='a2data.csv')
    rs.preprocessData()
    print(rs.dataSummary())

if __name__ == "__main__":
    run()

""" 
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