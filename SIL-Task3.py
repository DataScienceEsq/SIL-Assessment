'''

This PYTHON program reads in a CSV file 'out.csv' and outputs a database which can be queried using SQL.
To run this program, please note the following:

1. The file 'out.csv' needs to be present in your folder or a path needs to provided to the file.
2. From the command prompt one can run the program using the command 'python SIL-Task3.py'.


'''

import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('out.csv', engine = "python", sep = ',', quotechar = '"', error_bad_lines = False)

print(df.shape)

engine = create_engine('sqlite://', echo=False)

df.to_sql('bibleSource', con=engine)

# Counting Number of Records in the database bibleSource

a = engine.execute("SELECT count(*) FROM bibleSource").fetchall()[0][0]

print('Total Number of Records = %d' % a)
