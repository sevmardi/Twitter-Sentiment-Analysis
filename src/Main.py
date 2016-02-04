import json
from src.views import View
""" Read the config file"""
f = open("config/config.json")
config = json.loads(f.read())
f.close()


class Main(object):
    def run(self):
        view = View()


if __name__ == '__main__':
    app = Main()
    app.run()
