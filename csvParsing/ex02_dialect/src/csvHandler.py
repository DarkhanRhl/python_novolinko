import csv
from csvColonDialect import CsvColonDialect

class CsvHandler:
    def read(self, name):
        fname = name
        file = open(fname, "r")
        
        #Read le dialect contenue dans CsvColonDialect
        reader = csv.reader(file, CsvColonDialect())

        # #Enregistre le dialect definit dans csvColonDialect auprès du module csv
        # csv.register_dialect('colon-dialect', CsvColonDialect())
        # # Read le dialect précédemment enregistrer
        # reader = csv.reader(file, 'colon-dialect')
        
        for row in reader:
            print(row)
        file.close()