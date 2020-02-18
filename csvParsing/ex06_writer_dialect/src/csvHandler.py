import csv
from csvMyDialect import CsvMyDialect

class CsvHandler:

    #fonction init appellé a la creation de la classe dans le fichier exec
    def __init__(self, name):
        #Definition d'une variable inhérente à cette classe
        #qui pourra être appellé dans n'importe quels fonctions
        csv.register_dialect('my-dialect', CsvMyDialect())
        self.fname = name

    def write(self):
        #Cette fois-ci, nous appellons le self.fname initialiser
        #dans notre méthode __init__
        file = open(self.fname, "w")

        writer = csv.writer(file, 'my-dialect')
        writer.writerow(('test1', 'test2', 'test3'))
        writer.writerow(range(0,3))       # intervalle
        writer.writerow("abc")           # chaîne
        writer.writerow([20, 21, 22])     # liste
        writer.writerow((30, 31, 32))     # tupple
        writer.writerow( [20.80, "xyz", "X|Y|Z","A'B'C"] )
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
        print("\n-------- Modification du csv --------")
        self.write()
        print("\n-------- Seconde lecture --------\n")
        self.read()
        print("\n")
        