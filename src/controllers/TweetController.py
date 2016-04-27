import os
from src.DB.DataBase import DataBase
from tkinter import simpledialog
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import tkinter
from src.Listener import Listener
from src.controllers.TweetProcessor import TweetProcessor


class TweetController(object):
    """docstring for Controller"""

    processor = TweetProcessor()

    def __init__(self, tweet_gui):
        self.auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
        self.auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        self.db = DataBase()
        self.tweet_gui = tweet_gui
        self.default_keyword = "climate change"

        self.create_table_if_not_exist()


    def start_stream(self, tweets_to_add):

        self.tweet_listener = Listener()
        self.stream = Stream(auth=self.auth, listener=self.tweet_listener)
        self.stream.filter(track=[self.default_keyword], async=True)


    def stop_streaming_tweets(self):
        self.stream.disconnect()

    def set_keyword(self, default_keyword):
        self.default_keyword = default_keyword
        print(default_keyword)

    def create_table_if_not_exist(self):
        self.db.create_table_if_not_exist()
