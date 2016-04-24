import os
import sqlite3

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

from src.Listener import Listener
from src.controllers.TweetProcessor import TweetProcessor

default_keyword = "climate change"
max_tweets = 10000


class TweetController(object):
    """docstring for Controller"""

    processor = TweetProcessor()

    def __init__(self, tweet_gui):
        self.auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
        self.auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        # self.server = server
        # self.conn = sqlite3.connect(os.path.dirname(__file__) + "../DB/iscp.db", check_same_thread=False)
        self.tweet_gui = tweet_gui
        self.conn = sqlite3.connect('DB/iscp.db', check_same_thread=False)

    def start_stream(self, tweets_to_add):
        # max_tweets = tweets_to_add + self.processor.db.get_count()
        self.tweet_listener = Listener()
        self.stream = Stream(auth=self.auth, listener=self.tweet_listener)
        self.stream.filter(track=[default_keyword], async=True)

    def list_of_tweets(self):
        f = open(os.path.dirname(__file__) + "data/tweets.json")
        return f.read()

    def stop_streaming_tweets(self):
        self.stream.disconnect()

        # def set_keyword(self, keywords):
        #     self.keywords = keywords
        #     print(keywords)


if __name__ == '__main__':
    l = TweetController(1)
    l.start_stream(2)
