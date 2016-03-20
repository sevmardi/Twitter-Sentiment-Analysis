import os
# print(os.environ)
# print(os.getcwd())
from views import MainPanel


class Main:
    def __init__(self):
        self.view = MainPanel.MainPanel()


if __name__ == '__main__':
    Main()


