import csv

class CsvHandler:

    def __init__(self, name):
        print("DANS LE INIT")
        self.fname = name

    def write(self, name):
        fname =  name    

        #cette fois-ci, nous ouvrons avec le mode écriture
        file = open(fname, "w")

        #et nous recuperons le fichier à éditer
        writer = csv.writer(file)
    
        # Écriture de la ligne d'en-tête avec le titre
        # des colonnes.
        writer.writerow(('Heure', 'Température'))

        # Écriture des quelques données.
        writer.writerow((08.34, '7 degrès celsius'))
        writer.writerow((11.40, '11 degrès celsius'))
        writer.writerow((14.45, '15 degrès celsius'))
        file.close()

    def read(self, name):
        fname = name    
        file = open(fname, "r")

        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

    def handler(self, name):
        print("\n-------- Premiere lecture --------\n")
        self.read(name)
        print("\nd-------- Modification du csv --------")
        self.write(name)
        print("\n-------- Seconde lecture --------\n")
        self.read(name)
        print("\n")
        