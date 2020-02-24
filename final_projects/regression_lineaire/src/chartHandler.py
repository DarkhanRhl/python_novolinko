import csv
from csvHandler import CsvHandler
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from csvMyDialect import CsvMyDialect
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class ChartHandler:

    def __init__(self, fname):
        self.fname = fname
        csv.register_dialect('my-dialect', CsvMyDialect())
        self.lr = LinearRegression()
    
    def getValuesFromCsv(self):
        csv = CsvHandler(self.fname)
        return (csv.getCsv())

    def drawGraph(self):
        sns.set()
        plt.title("Données de Hubble")
        plt.xlabel("Distance")
        plt.ylabel("Vitesse de récession")
        plot = plt.scatter(self.initialx_distance, self.initialy_velocity)
        plt.plot(self.x_distance,  self.lr.predict(self.x_distance), color='red', linewidth=3)
        plt.show()

    def initDistanceAndVelocity(self, value):
        self.x_distance = []        
        self.y_velocity = []

        del value[0]
        i = 0
        for v in value:
            self.x_distance.append(float(value[i][0]))
            i += 1

        i = 0
        for v in value:
            self.y_velocity.append(float(value[i][1]))
            i += 1

        self.initialx_distance = self.x_distance
        self.initialy_velocity = self.y_velocity

        self.x_distance = np.array(self.x_distance).reshape((len(self.x_distance), 1))
        self.y_velocity = np.array(self.y_velocity).reshape((len(self.y_velocity), 1))
        self.lr.fit(self.x_distance, self.y_velocity)

    def handler(self):
        value = self.getValuesFromCsv()
        self.initDistanceAndVelocity(value)
        self.drawGraph()
        