import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from csvMyDialect import CsvMyDialect


#voir la librsire plot https://plot.ly/python/line-and-scatter/
class CsvHandler:

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


    def createTwoLinesChart(self):
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
        fig = px.line(df, x='AAPL_x', y='AAPL_y')

        #Affiche la figure
        fig.show()

    def handler(self):
        self.createBasicChart()
        # self.createTwoLinesChart()
        