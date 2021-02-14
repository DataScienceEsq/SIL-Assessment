import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('out.csv', engine = "python", sep = ',', quotechar = '"', error_bad_lines = False)

print(df.shape)

engine = create_engine('sqlite://', echo=False)

df.to_sql('bibleSource', con=engine)

a = engine.execute("SELECT count(*) FROM bibleSource").fetchall()[0][0]

print('Total Number of Records = ',a)
