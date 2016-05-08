import os
# print(os.environ)
# print(os.getcwd())
from src.views.MainPanel import MainPanel
import matplotlib.pyplot as plt
import numpy as np
from src.DB.DataBase import DataBase
import tkinter as tk
import datetime


class Main(object):
    # def __init__(self):
    #     self.view = MainPanel()
    def __init__(self):
        self.db = DataBase()
        self.panel()

    def panel(self):
        window = tk.Tk()

        Button1 = tk.Button(window, text="Open de bar chart!", command=lambda: self.createTimechart(), bg="darkblue",
                            fg="white", font="Helvetica")
        Button1.config(height=5, width=25, bd=4)
        Button1.pack()
        window.mainloop()

    def createBarchart(self):
        plt.xlabel('Sentiment')
        plt.ylabel('Aantal')
        plt.title('ISCP - Daniël Vercouteren: Bar Chart')

        # X is negatief, neutraal, positief
        # Y is het aantal
        data = ['Negatief', 'Neutraal', 'Positief']
        x = np.arange(len(data))
        y = self.db.get_mood()
        width = 0.8

        plt.bar(x, y, width, color="darkblue")
        plt.xticks(x + 0.4, data)

        plt.tight_layout()
        plt.show()

    def createTimechart(self):
        plt.figure(figsize=(30, 10))
        tijdLijst = []
        scoreLijst = []

        data = self.db.getTimeChart()
        for rij in data:
            tijdLijst.append(datetime.datetime.fromtimestamp(rij[0] / 1000.0))
            scoreLijst.append(rij[1])

        plt.plot(tijdLijst, scoreLijst)
        plt.show()

    def createPiechart(self):
        plt.title('ISCP - Daniël Vercouteren: Pie Chart')

        dataLabels = "Negatief", "Neutraal", "Positief"
        dataSize = self.db.get_mood()
        colors = "firebrick", "darkorange", "forestgreen"
        explode = (0, 0, 0)

        plt.pie(dataSize, explode=explode, labels=dataLabels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')

        plt.show()


if __name__ == '__main__':
    Main()
