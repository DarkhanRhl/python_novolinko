import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from csvMyDialect import CsvMyDialect
from csvHandler import CsvHandler
import psutil
import threading
from computerMonitoring import ComputerMonitoring
import time
import datetime as dt
import matplotlib.animation as animation

class ChartHandler:

    def __init__(self, name, nameLines):
        self.fname = name
        self.nameLines = nameLines
        self.fig = go.Figure()
        csv.register_dialect('my-dialect', CsvMyDialect())


    def animate(self, i, xs, ys):
        df = pd.read_csv(self.fname, dialect="my-dialect")     

        vm = df['virtual-memory']
        cpu = df['cpu']
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(vm[len(cpu) - 1])

        # Limit x and y lists to 50 items
        xs = xs[-50:]
        ys = ys[-50:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Cpu consumption over Time')
        plt.ylabel('Cpu')
        time.sleep(2.6)

    def handler(self):
        self.cih = ComputerMonitoring()
        self.csv = CsvHandler()
        # self.animate(0, 0, 0)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        xs = []
        ys = []
        ani = animation.FuncAnimation(self.fig, self.animate, fargs=(xs, ys), interval=100)
        plt.show()
        