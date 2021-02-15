'''

Author: Robert Ferdinand (2021)

This PYTHON program reads a CSV file 'out.csv' as input and outputs a database 'bibleSource' which can be queried using SQL.

To run this program, please note the following:

1. The file 'out.csv' needs to be present in local folder or a path to the file needs to provided in the 'pd.read_csv' statement below.
2. From the command prompt one can run the program using the command 'python SIL-Task3.py'.


'''

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('out.csv', engine = "python", sep = ',', quotechar = '"', error_bad_lines = False)

print(df.shape)

engine = create_engine('sqlite://', echo=False)

df.to_sql('bibleSource', con=engine)

# Running SQL Query to Count Number of Records in the database 'bibleSource'

a = engine.execute("SELECT count(*) FROM bibleSource").fetchall()[0][0]

print('Total Number of Records in the bibleSource Database = %d' % a)
