import csv
from csvHandler import CsvHandler
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from csvMyDialect import CsvMyDialect

class ChartHandler:

    def __init__(self, fname):
        self.fname = fname
        csv.register_dialect('my-dialect', CsvMyDialect())
    
    def getValuesFromCsv(self):
        csv = CsvHandler(self.fname)
        return (csv.getCsv())

    def drawGraph(self):
        sns.set(style="darkgrid")
        # self.x_distance = np.array(self.x_distance).astype(np.float)
        # self.y_distance = np.array(self.y_distance).astype(np.float)
        g = sns.jointplot(self.x_distance, self.y_velocity,
                        kind="reg", truncate=False,
                        xlim=(0, 60), ylim=(0, 12))
        plt.show()

    def initDistanceAndVelocity(self, value):
        self.x_distance = []        
        self.y_velocity = []

        del value[0]
        i = 0
        for v in value:
            self.x_distance.append(value[i][0])
            i += 1
    
        i = 0
        for v in value:
            self.y_velocity.append(value[i][1])
            i += 1
        # self.x_distance = np.array(self.x_distance).reshape((len(self.x_distance), 1))
        # self.lr.fit(self.x_distance, self.y_velocity)

        # print(self.x_distance)
        # print(self.y_velocity)

    def handler(self):
        value = self.getValuesFromCsv()
        self.initDistanceAndVelocity(value)
        self.drawGraph()
        