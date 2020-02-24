import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from csvMyDialect import CsvMyDialect
from csvHandler import CsvHandler
import psutil
import threading
from computerMonitoring import ComputerMonitoring
import time

#voir la librsire plot https://plot.ly/python/line-and-scatter/
class GeneratorHandler:

    def __init__(self, name):
        self.fname = name
        csv.register_dialect('my-dialect', CsvMyDialect())


    def createBasicChart(self):
        # Recupere un csv en ligne
        df = pd.read_csv(self.fname, dialect="my-dialect")

        #Crée la figure et donne un nom à la courbe   
        fig = go.Figure(go.Scatter(x = df['heure'], y = df['consommation'], name='consommations journalieres'))
        fig.update_layout(title='Consommations éléctrique au cours d\'une journée',
           plot_bgcolor='rgb(230, 230,230)',
           showlegend=True)

        #Affiche la figure
        fig.show()


    def createTwoLinesChart(self, file, nameLines):
        df = pd.read_csv(file)
        fig = px.line(df, x=nameLines[0], y=nameLines[1])

        #Affiche la figure
        fig.show()

    def updateCsv(self):
        while 1:
            infos = self.cih.handler()
            self.csv.write(self.fname, infos)
            self.csv.read(self.fname)
            time.sleep(2.4)

    def handler(self):
        self.cih = ComputerMonitoring()
        self.csv = CsvHandler()
        self.csv.createFile(self.fname, {"cpu", "virtual-memory"})
        self.updateCsv()
        # self.createBasicChart()
        # self.createTwoLinesChart()
        