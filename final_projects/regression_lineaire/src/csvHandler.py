import csv
from csvMyDialect import CsvMyDialect

class CsvHandler:

    def __init__(self, name):
        csv.register_dialect('my-dialect', CsvMyDialect())
        self.fname = name

    def write(self, toWrite):
        file = open(self.fname, "w")

        writer = csv.writer(file, 'my-dialect')
        writer.writerow(toWrite)
        file.close()

    def printCsv(self):
        file = open(self.fname, "r")
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

    def getCsv(self):
        file = open(self.fname, "r")
        reader = csv.reader(file, 'my-dialect')
        results = []
        for row in reader: # each row is a list
            results.append(row)
        file.close()
        return (results)