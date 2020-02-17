import csv

class CsvNumDialect(csv.excel):
    quoting = csv.QUOTE_NONNUMERIC