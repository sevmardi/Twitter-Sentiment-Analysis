import os
#print(os.environ)
#print(os.getcwd())
from src.views.MainPanel import MainPanel


class Main(object):
    def __init__(self):
        self.view = MainPanel()


if __name__ == '__main__':
    Main()
