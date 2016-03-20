import json
import os
import tweepy
from src import Main
from src.services import TweetStreamer


class TweetController(object):
    """docstring for Controller"""

    def __init__(self, server):
        self.auth = tweepy.OAuthHandler(Main.config["consumer_key"], Main.config["consumer_secret"])
        self.auth.set_access_token(Main.config["access_token"], Main.config["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())

        def fetch_tweets(self):
            pub_tweets = self.api.home_timeline()
            f = open(os.path.dirname(__file__) + "../../Data/tweets.json", "w")
            f.write(json.dumps(pub_tweets))

        def start_streaming_tweets(self, keywords):
            self.tweet_listener = TweetStreamer()
            self.stream = tweepy.Stream(auth=self.auth, listener=self.tweet_listener)
            self.stream.filter(track=keywords, async=True)

        def list_of_tweets(self):
            f = open(os.path.dirname(__file__) + "../../Data/tweets.json")
            return f.read()

        def stop_streaming_tweets(self):
            self.stream.disconnect()
