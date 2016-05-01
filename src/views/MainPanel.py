from tkinter import *
import tkinter as tkinter
from tkinter import messagebox
from tkinter import simpledialog
import socket

from src.controllers.TweetController import TweetController

LARGE_FONT = ("Verdana", 12)
class MainPanel:
    def __init__(self):
        self.tweets_to_add = 1000
        self.canvas_width = 850
        self.canvas_height = 450
        self.auto_updating = False
        self.tweetcontroller = TweetController()
        self.tk = Tk()
        self.statusVar = StringVar()
        self.create_window(self.tk)

    def create_window(self, master):
        self.add_menu(master)
        self.add_status_bar(master)
        self.add_canvas(master)
        self.add_navigation()
        self.empty_window()
        master.mainloop()

    def add_menu(self, master):
        # Tkinter puts menus at the top by default
        menu = Menu(master)
        master.config(menu=menu)
        self.add_submenu(menu)

    def add_submenu(self, menu):
        sub_menu = Menu(menu)
        # Adds a drop down when "File" is clicked
        menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_command(label="Fetch 10 tweets", command=self.start_stream_a)
        sub_menu.add_command(label="Fetch 100 tweets", command=self.start_stream_b)
        sub_menu.add_command(label="Fetch 1000 tweets", command=self.start_stream_c)
        sub_menu.add_command(label="Fetch 10000 tweets", command=self.start_stream_d)
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit", command=self.tk.destroy)

        # Create the edit / settings menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Settings", menu=editMenu)


        # Create the Info menu
        helpMenu = Menu(menu)
        menu.add_cascade(label="Info", menu=helpMenu)

        helpMenu.add_command(label="About the graph", command=self.show_about_graph)

    def add_status_bar(self, master):
        # bd is border, relief is type of border
        status = Label(master, textvariable=self.statusVar, bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def add_canvas(self, master):
        # ******* Creating a Canvas *******
        self.canvas = Canvas(self.tk, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def add_navigation(self):
        # test = tkinter.Button(self, text="nice", font=LARGE_FONT)
        # test.pack()

        pass

    def empty_window(self):
        self.canvas.delete("all")
        # print('cleared')

    def start_stream_a(self):
        # change label, then update to show the label before endless loop
        self.tweets_to_add = 10
        self.start_stream()

    def start_stream_b(self):
        # change label, then update to show the label before endless loop
        self.tweets_to_add = 100
        self.start_stream()

    def start_stream_c(self):
        # change label, then update to show the label before endless loop
        self.tweets_to_add = 1000
        self.start_stream()

    def start_stream_d(self):
        # change label, then update to show the label before endless loop
        self.tweets_to_add = 10000
        self.start_stream()

    def start_stream(self):
        if self.test_connection():
            self.set_footer_text('Starting stream to add ' + str(self.tweets_to_add) + " tweets.")
            self.tk.update()
            # start endless loop, application is not responding untill it ends.
            self.tweetcontroller.start_stream(self.tweets_to_add)
        else:
            self.set_footer_text('Failed to connect to the internet. Please check your connection.')

    def set_footer_text(self, footer_text):
        self.statusVar.set(footer_text)

    def show_about_graph(self):
        info = 'This graph represents how positive or negative the tweets are. Green is positive, ' \
               'red is negative. The scales are 12 points from the center, and the words in the tweet have ' \
               'a positive or negative value. For example:' \
               '\n\nhappy = 5 points' \
               '\nunknown words are 0 points' \
               '\nangry = -5 points' \
               '\n\nOther words like nice, sad etc. value between 5 and -5 points.' \
               '\n5 / -5 Points are max and min for every word.' \
               '\n\nhappy happy happy = 15 points.'

        messagebox.showinfo('Current settings', info)

    def test_connection(self):
        remote_server = "www.google.com"
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname(remote_server)
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False
