'''

Author: Robert Ferdinand (2021)

This PYTHON 3.7 program reads a CSV file 'out.csv' and outputs a database 'bibleSource' which can be queried using SQL.

To run this program, please note the following:

1. The file 'out.csv' needs to be present in the local folder or a path to the file needs to be provided.
2. From the command prompt, one can run the program using the command 'python SIL-Task3.py'.


'''

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('out.csv', engine = "python", sep = ',', quotechar = '"', error_bad_lines = False)

engine = create_engine('sqlite://', echo=False)

df.to_sql('bibleSource', con=engine)

# Running SQL Query to Count Number of Records in the database 'bibleSource'

a = engine.execute("SELECT COUNT(*) FROM bibleSource").fetchall()

print('Total Number of Records in the bibleSource Database = %d' % a[0][0])
