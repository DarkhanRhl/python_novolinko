import csv
from csvNumDialect import CsvNumDialect

class CsvHandler:

    def read(self):
        fname = "./ressources/test.csv"
        file = open(fname, "r")
        reader = csv.reader(file, CsvNumDialect())
        for row in reader:
            print(row)
        file.close()