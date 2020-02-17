import csv

class CsvHandler:

    def __init__(self, name):
        self.fname = name

    def write(self):
        file = open(self.fname, "w")
        writer = csv.writer(file)
        writer.writerow(('Heure', 'Température'))
        writer.writerow((08.34, '7 degrès celsius'))
        writer.writerow((11.40, '11 degrès celsius'))
        writer.writerow((14.45, '15 degrès celsius'))
        file.close()

    def read(self):
        file = open(self.fname, "r")
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

    def handler(self):
        print("\n-------- Premiere lecture --------\n")
        self.read()
        print("\nd-------- Modification du csv --------")
        self.write()
        print("\n-------- Seconde lecture --------\n")
        self.read()
        print("\n")
        