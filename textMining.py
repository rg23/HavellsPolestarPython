import pyodbc

import pandas as pd

import csv
import textblob as a
import nltk


conn =pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=10.200.4.195;'
    r'DATABASE=HavellsDWH;'
    r'UID=spo0171_03_RW;'
    r'PWD=NewWorld@123'
    )

cursor = conn.cursor()
print(cursor)
print(conn)

query = '''
SELECT top (1) [VBELN] BillingDocument
      ,[ERDAT] BillingDate
      ,[SFAKN] CancelledBillingDocument 
      ,[TEXT]  CancelReason
      ,[CREATED_ON_SQL]
  FROM [SAP_STAGING].[dbo].[stg_ZRFC_DW_REJ_REASON_SAP]
  '''


a= cursor.execute(query)

df = pd.read_sql(query,conn)

print(df)

conn.close()

"""
print(a)
for row in cursor:
    print('row = %r' % (row,))
"""

"""
out = open('Cancelled.csv', 'w')
for row in a:
    for column in row:
        out.write('%s;' % column)
    out.write('\n')
out.close()
"""

