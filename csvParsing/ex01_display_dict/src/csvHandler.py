import csv

class CsvHandler:

    def read(self):
        fname = "./ressources/test.csv"
        file = open(fname, "r")
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
        file.close()