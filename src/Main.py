import os
# print(os.environ)
# print(os.getcwd())
from views import View


class Main:
    def __init__(self):
        self.view = View.MainPanel()


if __name__ == '__main__':
    Main()


# import tkinter
# tkinter._test()