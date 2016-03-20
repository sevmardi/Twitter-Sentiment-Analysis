import json
# print(os.environ)
# print(os.getcwd())
from views import MainPanel

f = open("config/config.json")
config = json.loads(f.read())
f.close()


class Main:
    def __init__(self):
        self.view = MainPanel.MainPanel()


if __name__ == '__main__':
    Main()
