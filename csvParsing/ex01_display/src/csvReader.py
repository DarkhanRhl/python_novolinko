import csv

class CsvReader:

    def read(self):
        #Definit le chemin vers le fichier csv
        fname = "./ressources/test.csv"

        #Ouvre le fichier csv avec le mode lecture et le stocke dans la variable file
        file = open(fname, "r")

        #lit le fichier csv stocké dans file et le parse dans la variable reader
        reader = csv.reader(file)

        #affiche chaque colone du csv 
        for row in reader:
            print(row)
        
        # ferme le fichier
        file.close()