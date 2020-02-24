import csv

class CsvNumDialect(csv.excel):
    # delimiter = ";"
    # quotechar = None
    # escapechar = None
    # doublequote = None
    # lineterminator = "\r\n"
    quoting = csv.QUOTE_NONNUMERIC
    # skipinitialspace = False
