import csv

class CsvMyDialect(csv.Dialect):
    delimiter = ","
    quotechar = "'"
    escapechar = "\\"
    doublequote = None
    lineterminator = "\r\n"
    quoting = csv.QUOTE_NONE
    skipinitialspace = False