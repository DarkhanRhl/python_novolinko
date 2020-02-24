import csv
from csvMyDialect import CsvMyDialect

class CsvHandler:

    def __init__(self):
        csv.register_dialect('my-dialect', CsvMyDialect())

    def write(self, file, toWrite):
        file = open(file, "a")
        writer = csv.writer(file, 'my-dialect')
        writer.writerow(toWrite)
        file.close()

    def read(self, file):
        file = open(file, "r")
        reader = csv.reader(file)
        # for row in reader:
        #     print(row)
        file.close()

    def createFile(self, file, rowTitle):
        file = open(file, "w")
        writer = csv.writer(file, 'my-dialect')
        writer.writerow(rowTitle)