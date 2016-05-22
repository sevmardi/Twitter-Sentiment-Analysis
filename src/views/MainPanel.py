from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tkinter
from tkinter import messagebox
from tkinter import simpledialog
import socket
from tkinter import ttk
from src.controllers.TweetController import TweetController


class MainPanel:
    def __init__(self):
        self.canvas_width = 850
        self.canvas_height = 450
        self.auto_updating = False

        self.tk = Tk()
        self.statusVar = StringVar()
        self.create_window(self.tk)


    def create_window(self, master):
        self.add_menu(master)
        self.add_status_bar(master)
        self.add_canvas(master)
        master.mainloop()

    def add_menu(self, master):
        # Tkinter puts menus at the top by default
        menu = Menu(master)
        master.config(menu=menu)

    def add_status_bar(self, master):
        # bd is border, relief is type of border
        status = Label(master, textvariable=self.statusVar, bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def add_canvas(self, master):
        # ******* Creating a Canvas *******
        self.canvas = Canvas(self.tk, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def add_
    def set_footer_text(self, footer_text):
        self.statusVar.set(footer_text)

    def heat_map(self):
        pass

    def plot_view(self):
        pass

    def scatter_plot(self):
        pass

    def time_line(self):
        pass


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



