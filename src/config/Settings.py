import json
from tweepy import OAuthHandler
import tweepy


class Settings():
    """
    Fetch the config file to read the API keys
    """
    fr = open('../config/config.json')
    api_data = json.loads(fr.read())
    fr.close()

    def __init__(self):
        self.auth = OAuthHandler(self.api_data["consumer_key"], self.api_data["consumer_secret"])
        self.auth.set_access_token(self.api_data["access_token"], self.api_data["access_token_secret"])

    def get_tweepy_api(self):
        api = tweepy.api(self.auth)
        return api
