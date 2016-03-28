# tweepy setup
import time
from tweepy import OAuthHandler
import tweepy
import json
from src.controllers import TweetProcessor

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""


class TweetStreamer:
    # default values
    search_word = 'emoji'
    streaming = False

    # processor to process tweets (store, moodvalue etc.)
    processor = TweetProcessor()

    # get a dictionary with keys for the twitter api
    fr = open('src/config/config.json')
    api_data = json.loads(fr.read())
    fr.close()

    # combine keys to create the OAUTH2 connection with Twitter, using the TwitterAPI
    auth = OAuthHandler(api_data["consumer_key"], api_data["consumer_secret"])
    auth.set_access_token(api_data["access_token"], api_data["access_token_secret"])
    api = tweepy.API(auth)

    def __init__(self, tweet_gui):
        self.gui = tweet_gui

    # TODO
    def start_stream(self, tweets_to_add):
        max_tweets = tweets_to_add + self.processor.db.get_count()

    def set_search_word(self, search_word):
        self.search_word = search_word

    # TODO
    def change_collection(self, collection_name):
        self.processor.mongo_adapter.set_collection(collection_name)

