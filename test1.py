import pyodbc
import pandas as pd
import os
import numpy as np
import seaborn as sns
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import opinion_lexicon
import matplotlib.pyplot as plt


from sqlalchemy import create_engine

from textblob import TextBlob
import re

print("1")

def analize_sentiment(analysis):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


def comment(x):
    if analize_sentiment(blob) > 0:
        return("Positive")
    elif analize_sentiment(blob) == 0:
        return("Ambiguous")
    else:
        return("Negative")



conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=10.199.4.217;'
    r'DATABASE=HavellsDWH;'
    r'UID=spo0171_01_RO;'
    r'PWD=Havells@123'
    )
cursor = conn.cursor()

connDev = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=10.200.4.195;'
    r'DATABASE=HavellsDWH;'
    r'UID=spo0171_03_RW;'
    r'PWD=NewWorld@123'
    )
cursor2 = connDev.cursor()


query = '''SELECT [VBELN] BillingDocument
      ,[ERDAT] BillingDate
      ,[SFAKN] CancelledBillingDocument 
      ,[TEXT]  CancelReason
      ,[CREATED_ON_SQL]
  FROM [SAP_STAGING].[dbo].[stg_ZRFC_DW_REJ_REASON_SAP]
  where [erdat] >= '04-01-2018'
'''


podRemarks = '''Select distinct cast(PODRemark as varchar(200)) as PODRemark from factPOD'''

#cursor.execute(query)

cursor.execute(podRemarks)

cursor2.execute(query)

# abc = str(cursor.fetchall())
# print(abc)

for row in cursor.fetchall():
   one =1


for row in cursor2.fetchall():
   one =1

df = pd.read_sql(podRemarks,conn)

# reason = df.CancelReason

# print(df.describe())
# print(df.head())

print('Total rows in this dataframe:', len(df.index), '\n')

#print(rows)
i=0

#print (type(df[0]))


#print(df['PODRemark'])

totalrows = df['PODRemark'].count()


for i in range(totalrows):
    #print(df.iloc[[i]])
    row = str(df.iloc[[i]])

    blob = TextBlob(row)
    df['Sentiment'] = comment(analize_sentiment(blob))
#    print(i,comment(analize_sentiment(blob)))

#print(df)

df.to_csv("""C:\\Users\\User\\Desktop\\PODRemarks.txt""",sep=";")


df.to_sql('PODRemark',connDev,if_exists='append',chunksize=2)

'''
    blob = TextBlob(df[i])
    print(df[i]) #+ analize_sentiment(blob))
    print (analize_sentiment(blob))

#print(len(rows))

#print(rows[0])

conn.close()
'''
