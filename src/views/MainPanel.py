from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import socket
from views.draw.DrawGraph import DrawGraph
from views.draw.DrawPlot import DrawPlot


class MainPanel:
    def __init__(self):
        self.tweets_to_add = 500
        self.canvas_width = 1246
        self.canvas_height = 687
        self.auto_updating = False

        # self.stream = TweetStream(self)
        # self.mongo_adapter = self.stream.processor.mongo_adapter
        self.graph = DrawGraph()
        # self.plot = DrawPlot(self.mongo_adapter)

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
        # Tkinter puts menus at the top by default
        menu = Menu(master)
        master.config(menu=menu)
        self.add_submenu(menu)

    def add_submenu(self, menu):
        sub_menu = Menu(menu)

        # # Adds a drop down when "File" is clicked
        # menu.add_cascade(label="File", menu=sub_menu)
        # sub_menu.add_command(label="Fetch 10 tweets", command=self.start_stream_a)
        # sub_menu.add_command(label="Fetch 100 tweets", command=self.start_stream_b)
        # sub_menu.add_command(label="Fetch 1000 tweets", command=self.start_stream_c)
        # sub_menu.add_command(label="Fetch 10000 tweets", command=self.start_stream_d)
        # sub_menu.add_separator()
        # sub_menu.add_command(label="Exit", command=self.root.destroy)
        #
        # # Create the edit / settings menu
        # editMenu = Menu(menu)
        # menu.add_cascade(label="Settings", menu=editMenu)
        # editMenu.add_command(label="Change keyword", command=self.change_keyword_dialog)
        # editMenu.add_command(label="Change collection", command=self.change_collection_dialog)
        # editMenu.add_command(label="Remove collection", command=self.remove_collection_dialog)
        #
        # # Create the Info menu
        # helpMenu = Menu(menu)
        # menu.add_cascade(label="Info", menu=helpMenu)
        # helpMenu.add_command(label="Check existing collections", command=self.show_active_collections)
        # helpMenu.add_command(label="Check active settings", command=self.show_settings)
        # helpMenu.add_command(label="About the graph", command=self.show_about_graph)


    def add_toolbar(self, master):
        # ******* Creating a Toolbar *******
        toolbar = Frame(master, bg="gray")

        # Drawing the plot buttons on the toolbar
        # dra_plot_but = Button(toolbar, text="Plot view", command=self.draw_plot)
        # dra_plot_but.pack(side=LEFT, padx=2, pady=2)
        # inc_plot_but = Button(toolbar, text="Zoom in", command=self.increase_plot_size)
        # inc_plot_but.pack(side=LEFT, padx=2, pady=2)
        # dec_plot_but = Button(toolbar, text="Zoom out", command=self.decrease_plot_size)
        # dec_plot_but.pack(side=LEFT, padx=2, pady=2)
        # rig_plot_but = Button(toolbar, text="<", command=self.plot.go_right)
        # rig_plot_but.pack(side=LEFT, padx=2, pady=2)
        # lef_plot_but = Button(toolbar, text=">", command=self.plot.go_left)
        # lef_plot_but.pack(side=LEFT, padx=2, pady=2)
        # upd_plot_but = Button(toolbar, text="Auto update plot", command=self.update_plot)
        # upd_plot_but.pack(side=LEFT, padx=2, pady=2)
        #
        # # Drawing the graph buttons on the toolbar
        # dra_grap_but = Button(toolbar, text="Graph view", command=self.draw_graph)
        # dra_grap_but.pack(side=RIGHT, padx=2, pady=2)
        # inc_grap_but = Button(toolbar, text="Graph size +", command=self.increase_graph_size)
        # inc_grap_but.pack(side=RIGHT, padx=2, pady=2)
        # dec_grap_but = Button(toolbar, text="Graph size -", command=self.decrease_graph_size)
        # dec_grap_but.pack(side=RIGHT, padx=2, pady=2)
        # upd_grap_but = Button(toolbar, text="Auto update graph", command=self.update_graph)
        # upd_grap_but.pack(side=RIGHT, padx=2, pady=2)

        # Add toolbar to window
        toolbar.pack(side=TOP, fill=X)
        
    def add_status_bar(self, master):
        # ******* Creating a Status Bar for the Bottom *******
        # self.statusVar.set('Welcome to Tweet Analyzer by Randy Vroegop')
        # bd is border, relief is type of border
        status = Label(master, textvariable=self.statusVar, bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def add_canvas(self, master):
        # ******* Creating a Canvas *******
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def empty_window(self):
        self.canvas.delete("all")
        # print('cleared')


