import os
import tweepy
from tweepy import Stream
from src.controllers.TweetProcessor import TweetProcessor
from src.controllers.Listener import Listener
from tweepy import OAuthHandler


class TweetController(object):
    """docstring for Controller"""
    # default values
    search_word = 'climate change'

    def __init__(self, server):
        self.auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
        self.auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        self.server = server


    # def start_stream(self, tweets):
    # pub_tweets = self.api.home_timeline()
    # f = open(os.path.dirname(__file__) + "../../Data/tweets.json", "w")
    # f.write(json.dumps(pub_tweets))

    def start_stream(self, search_word):
        self.tweet_listener = Listener()
        self.stream = Stream(auth=self.auth, listener=self.tweet_listener)
        self.stream.filter(track=search_word, async=True)

    def list_of_tweets(self):
        f = open(os.path.dirname(__file__) + "../data/tweets.json")
        return f.read()

    def stop_streaming_tweets(self):
        self.stream.disconnect()

    def set_search_word(self, search_word):
        self.search_word = search_word


