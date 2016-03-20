from views import Toolbar as toolbar
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import socket


# from views.draw.DrawGraph import DrawGraph
# from views.draw.DrawPlot import DrawPlot


class MainPanel:
    def __init__(self):
        self.tweets_to_add = 500
        self.canvas_width = 1246
        self.canvas_height = 687
        self.auto_updating = False

        # self.stream = TweetStream(self)
        # self.mongo_adapter = self.stream.processor.mongo_adapter
        # self.graph = DrawGraph()
        #  self.plot = DrawPlot(self.mongo_adapter)

        self.root = Tk()
        self.statusVar = StringVar()
        self.create_window(self.root)

    def create_window(self, master):
        self.add_menu(master)
        self.add_toolbar(master)
        self.add_status_bar(master)
        self.add_canvas(master)
        self.empty_window()
        master.mainloop()

    def add_menu(self, master):
        pass

    def add_toolbar(self, master):
        pass

    def add_status_bar(self, master):
        pass

    def add_canvas(self, master):
        pass

    def empty_window(self):
        pass
