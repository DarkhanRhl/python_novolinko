import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class Graph:

    def handler(self):
        sns.set()
        x = np.linspace(0, 10, 500)
        y = np.random.randn(500)
        # plt.plot(x,y) 
        sns.distplot(y, kde=True)
        plt.show()



        