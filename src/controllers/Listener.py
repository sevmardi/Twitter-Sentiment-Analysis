import tweepy
import os
import sys
import time
import json
import jsonstruct
from src.controllers.TweetProcessor import TweetProcessor
from src.services.MoodAnalyser import MoodAnalyser
from src.models.Tweet import Tweet
from tweepy.streaming import StreamListener

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""


class Listener(StreamListener):
    # get a dictionary with keys for the twitter api
    fr = open('config/config.json')
    api_data = json.loads(fr.read())
    fr.close()

    def __init__(self, save_location="../data/tweets.json"):
        super().__init__()
        self.save_location = save_location
        self.count = 0
        self.tweets = []
        # self.analyser = MoodAnalyser()
        print("Listener created")

    def on_status(self, status):
        """
        Called when a tweet is recieved. It creates a Tweet object and passes it to the Analyser. It saves the tweet
		in memory and writes the recieved tweet count to the database.
        :param status:
        """
        print("Tweet received")
        # self.output.write(status + "\n")
        tweet = self.create_tweet(status)
        # self.analyser.analyse(tweet)
        self.count += 1
        self.save_tweets()
        return

    def save_tweets(self):
        print("Saving tweets to tweets.json")
        f = open(os.path.dirname(__file__) + self.save_location, "w")
        f.write(jsonstruct.encode(self.tweets))
        f.close()

    def on_error(self, status_code):
        sys.stderr.write('Error:' + str(status_code) + '\n')
        return False

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds ...\n")
        time.sleep(60)
        return

    def on_disconnect(self, notice):
        print("Disconnected")
        self.save_tweets()
        return

    def set_search_word(self, search_word):
        self.search_word = search_word

    def create_tweet(self, status):
        return Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)
