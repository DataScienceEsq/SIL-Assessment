from pybtex.database.input import bibtex

INFILE = 'source.bib'
OUTFILE = 'out.csv'

fh = open(OUTFILE, "w")
fh.write("ID"+","+"TITLE"+","+"LGCODE"+","+"YEAR"+"\n")


parser = bibtex.Parser()

bibdata = parser.parse_file(INFILE)


for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        TITLE = str(b['title'])
        TITLE = TITLE.replace(',','')
        LGCODE = str(b['lgcode'])
        LGCODE = LGCODE.replace(',','')
        YEAR = str(b['year'])
        YEAR = YEAR.replace(',','')
        fh.write(str(bib_id)+","+TITLE+","+LGCODE+","+YEAR+"\n")
    except(KeyError):
        continue
    except(UnicodeEncodeError):
        continue
 
fh.close()
     