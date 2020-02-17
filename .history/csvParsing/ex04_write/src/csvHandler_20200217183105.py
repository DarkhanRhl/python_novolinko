import csv

class CsvHandler:

    def write(self, name):
        fname =  name    

        #cette fois-ci, nous ouvrons avec le mode écriture
        file = open(fname, "w")

        #et nous recuperons le fichier à éditer
        writer = csv.writer(file)
    
        # Écriture de la ligne d'en-tête avec le titre des colonnes.
        writer.writerow(('Heure', 'Température'))

        # Écriture de quelques données.
        writer.writerow((08.34, '7 degrès celsius'))
        writer.writerow((11.40, '11 degrès celsius'))
        writer.writerow((14.45, '15 degrès celsius'))
        file.close()
        