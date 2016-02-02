from services import Listener
import json

""" Read the config file"""
f = open("config/config.json")
config = json.loads(f.read())
f.close()


class Main(object):
    def run(self):
        route = Listener()
        route.main()

if __name__ == '__main__':
    app = Main()
    app.run()
