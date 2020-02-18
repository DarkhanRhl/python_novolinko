import csv

class CsvMyDialect(csv.Dialect):
    # Séparateur de champ
    delimiter = "|"
    # Séparateur de ''chaîne''
    quotechar = "'"
    # Gestion du séparateur dans les ''chaînes''
    escapechar = "\\"
    doublequote = None
    # Fin de ligne
    lineterminator = "\r\n"
    # Ajout automatique du séparateur de chaîne (pour ''writer'')
    quoting = csv.QUOTE_NONNUMERIC
    # Ne pas ignorer les espaces entre le délimiteur de chaîne
    # et le texte
    skipinitialspace = False