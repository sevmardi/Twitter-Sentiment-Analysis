import os, random
# print(os.environ)
# print(os.getcwd())

import datetime
import matplotlib.pyplot as plt
import numpy as np
from src.DB.DataBase import DataBase
import tkinter as tk
from tkinter import *

LARGE_FONT = ("Verdana", 12)


class Main(object):
    def __init__(self):
        self.db = DataBase()
        # self.panel()
        self.canvas_width = 400
        self.canvas_height = 0
        self.root = Tk()
        self.create_window(self.root)

    def create_window(self, master):
        self.add_canvas(master)
        self.start_page(master)
        master.mainloop()

    def add_canvas(self, master):
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height, background='white')
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canvas.pack()

    def start_page(self, master):
        label = Label(master, text="ISCP - Sevak Mardirosian", font=("Helvetica", 16))

        label.pack()
        Button1 = tk.Button(master, text="Bar Chart!", command=lambda: self.bar_chart(), bg="gray",
                            fg="white", font="Helvetica")
        Button1.pack()

        Button2 = tk.Button(master, text="Time Chart", command=lambda: self.time_chart(), bg="gray",
                            fg="white", font="Helvetica")
        Button2.pack()

        Button3 = tk.Button(master, text="Pie Chart!", command=lambda: self.pie_chart(), bg="gray",
                            fg="white", font="Helvetica")
        Button3.pack()

        Button4 = tk.Button(master, text="Heat Map!", command=lambda: self.heat_map(), bg="gray",
                            fg="white", font="Helvetica")
        Button4.pack()


    def bar_chart(self):
        plt.xlabel('Sentiment')
        plt.ylabel('Number')

        # X is negatief, neutraal, positief
        # Y is het Number
        data = ['Negatief', 'Neutral', 'Positive']
        x = np.arange(len(data))
        y = self.db.get_mood()
        width = 0.8

        plt.bar(x, y, width, color="darkblue")
        plt.xticks(x + 0.4, data)

        plt.tight_layout()
        plt.show()

    def time_chart(self):
        plt.figure(figsize=(30, 10))
        date_list = []
        score_List = []

        data = self.db.get_time_chart()
        for rij in data:
            date_list.append(datetime.datetime.fromtimestamp(rij[0] / 500.0))
            score_List.append(rij[1])

        plt.plot(date_list, score_List)
        plt.show()

    def pie_chart(self):
        dataLabels = "Negatief", "Neutraal", "Positief"
        dataSize = self.db.get_mood()
        colors = "firebrick", "yellow", "lightskyblue"
        explode = (0, 0, 0)
        plt.pie(dataSize, explode=explode, labels=dataLabels, colors=colors, autopct='%1.1f%%', shadow=True,
                startangle=90)
        plt.axis('equal')
        plt.show()

    def heat_map(self):
        # label = tk.Label(self, text="Heat Map", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)

        title = "ROC's AUC"
        xlabel = "Timeshift"
        ylabel = "Scales"
        N = self.db.fetch_all_scores()
        data = np.random.rand(8, 12)

        f = plt.figure()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        c = plt.pcolor(data, edgecolors='k', linewidths=4, cmap='RdBu', vmin=0.0, vmax=1.0)
        plt.colorbar(c)

        plt.show()




if '__main__' == __name__:
    tet = Main()
