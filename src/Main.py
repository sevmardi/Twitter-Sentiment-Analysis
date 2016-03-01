
from src.views import MainPanel


# """ Read the config file"""
# f = open("config/config.json")
# config = json.loads(f.read())
# f.close()


class Main(object):
    def __init__(self):
        self.view = MainPanel.view()



if __name__ == '__main__':
    app = Main()
