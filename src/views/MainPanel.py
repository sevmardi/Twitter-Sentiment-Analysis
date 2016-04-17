from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import *
import socket
from src.views.draw.DrawGraph import DrawGraph
from src.views.draw.DrawPlot import DrawPlot
from src.controllers.TweetController import TweetController


class MainPanel:
    def __init__(self):
        self.tweets_to_add = 1000
        self.canvas_width = 1246
        self.canvas_height = 687
        self.auto_updating = False

        self.stream = TweetController(self)
       # self.mongo_adapter = self.stream.processor.mongo_adapter
       # self.graph = DrawGraph()
       # self.plot = DrawPlot(self.mongo_adapter)

        self.root = Tk()
        self.statusVar = StringVar()
        self.create_window(self.root)

    def create_window(self, master):
        self.add_menu(master)
        # self.add_toolbar(master)
        # self.add_status_bar(master)
        self.add_canvas(master)
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
        sub_menu.add_command(label="Exit", command=self.root.destroy)

        # Create the edit / settings menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Settings", menu=editMenu)
        editMenu.add_command(label="Change keyword", command=self.change_keyword_dialog)
        editMenu.add_command(label="Change collection", command=self.change_collection_dialog)
        editMenu.add_command(label="Remove collection", command=self.remove_collection_dialog)

        # Create the Info menu
        helpMenu = Menu(menu)
        menu.add_cascade(label="Info", menu=helpMenu)
        helpMenu.add_command(label="Check existing collections", command=self.show_active_collections)
        helpMenu.add_command(label="Check active settings", command=self.show_settings)
        helpMenu.add_command(label="About the graph", command=self.show_about_graph)

    # def add_toolbar(self, master):
    #     # ******* Creating a Toolbar *******
    #     toolbar = Frame(master, bg="gray")
    #
    #     # Drawing the plot buttons on the toolbar
    #     dra_plot_but = Button(toolbar, text="Plot view", command=self.draw_plot)
    #     dra_plot_but.pack(side=LEFT, padx=2, pady=2)
    #     inc_plot_but = Button(toolbar, text="Zoom in", command=self.increase_plot_size)
    #     inc_plot_but.pack(side=LEFT, padx=2, pady=2)
    #     dec_plot_but = Button(toolbar, text="Zoom out", command=self.decrease_plot_size)
    #     dec_plot_but.pack(side=LEFT, padx=2, pady=2)
    #     rig_plot_but = Button(toolbar, text="<", command=self.plot.go_right)
    #     rig_plot_but.pack(side=LEFT, padx=2, pady=2)
    #     lef_plot_but = Button(toolbar, text=">", command=self.plot.go_left)
    #     lef_plot_but.pack(side=LEFT, padx=2, pady=2)
    #     upd_plot_but = Button(toolbar, text="Auto update plot", command=self.update_plot)
    #     upd_plot_but.pack(side=LEFT, padx=2, pady=2)
    #
    #     # Drawing the graph buttons on the toolbar
    #     dra_grap_but = Button(toolbar, text="Graph view", command=self.draw_graph)
    #     dra_grap_but.pack(side=RIGHT, padx=2, pady=2)
    #     inc_grap_but = Button(toolbar, text="Graph size +", command=self.increase_graph_size)
    #     inc_grap_but.pack(side=RIGHT, padx=2, pady=2)
    #     dec_grap_but = Button(toolbar, text="Graph size -", command=self.decrease_graph_size)
    #     dec_grap_but.pack(side=RIGHT, padx=2, pady=2)
    #     upd_grap_but = Button(toolbar, text="Auto update graph", command=self.update_graph)
    #     upd_grap_but.pack(side=RIGHT, padx=2, pady=2)
    #
    #     # Add toolbar to window
    #     toolbar.pack(side=TOP, fill=X)

    # def add_status_bar(self, master):
    #     # ******* Creating a Status Bar for the Bottom *******
    #     # self.statusVar.set('Welcome to Tweet Analyzer by Randy Vroegop')
    #     # bd is border, relief is type of border
    #     status = Label(master, textvariable=self.statusVar, bd=1, relief=SUNKEN, anchor=W)
    #     status.pack(side=BOTTOM, fill=X)

    def add_canvas(self, master):
        # ******* Creating a Canvas *******
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

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
            self.root.update()
            # start endless loop, application is not responding untill it ends.
            self.stream.start_stream(self.tweets_to_add)
        else:
            self.set_footer_text('Failed to connect to the internet. Please check your connection.')

    def set_footer_text(self, footer_text):
        self.statusVar.set(footer_text)

    def change_keyword_dialog(self):
        user_val = simpledialog.askstring('Keyword', 'Set the keyword to filter tweets')
        try:
            self.set_footer_text("Now looking for the word: " + user_val)
            self.stream.search_word = user_val
        except TypeError:
            print('Could not set keyword, probably empty string is given')
        except:
            messagebox.showinfo('Error', 'Could not set the keyword to that value.')

    def change_collection_dialog(self):
        user_val = simpledialog.askstring('Collection', 'Set the collection to store tweets')
        try:
            self.set_footer_text("Storing tweets in collection: " + user_val)
            self.stream.change_collection(str(user_val))
        except TypeError:
            print('Could not set collection, probably empty string is given')
        except:
            messagebox.showinfo('Error', 'Could not set collection to that value.')

    def show_active_collections(self):
        collection_string = ''
        for col_val in self.mongo_adapter.get_collections():
            if col_val != 'system.indexes':
                collection_string += col_val + ' => '
                collection_string += str(self.stream.processor.mongo_adapter.get_collection_count(col_val))
                collection_string += '\n'
        messagebox.showinfo('collections', collection_string)

    def remove_collection_dialog(self):
        user_val = simpledialog.askstring('Remove collection', 'Collection name to remove:')
        self.set_footer_text("Removed collection: " + user_val)
        self.mongo_adapter.db.drop_collection(user_val)

    def show_settings(self):
        info = 'Current collection: ' + \
               str(self.mongo_adapter.collection.name) + \
               '\nCurrent search-word: ' + \
               self.stream.search_word

        messagebox.showinfo('Current settings', info)

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

    def draw_graph(self):
        self.plot.auto_updating = False
        self.graph.auto_updating = False
        self.empty_window()
        self.graph.update_graph(self.canvas, self.root, self.stream.processor.db)
        print(self.stream.processor.mongo_adapter.collection.name)

    def draw_plot(self):
        self.plot.auto_updating = False
        self.graph.auto_updating = False
        self.empty_window()
        self.plot.update_plot(self.canvas, self.root)

    def increase_graph_size(self):
        self.empty_window()
        self.graph.increase_graph_size()
        self.draw_graph()

    def decrease_graph_size(self):
        self.empty_window()
        self.graph.decrease_graph_size()
        self.draw_graph()

    def increase_plot_size(self):
        self.empty_window()
        self.plot.increase_plot_size()
        self.draw_plot()

    def decrease_plot_size(self):
        self.empty_window()
        self.plot.decrease_plot_size()
        self.draw_plot()

    def update_plot(self):
        self.graph.auto_updating = False
        self.plot.auto_update()

    def update_graph(self):
        self.plot.auto_updating = False
        self.graph.auto_update()

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
