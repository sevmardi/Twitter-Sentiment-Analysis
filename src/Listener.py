import tweepy
import os
import sys
import time
import json
import sqlite3
import jsonstruct
from src.controllers.TweetProcessor import TweetProcessor
from src.services.MoodAnalyser import MoodAnalyser
from src.models.Tweet import Tweet
from tweepy.streaming import StreamListener

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""

# tweets = []
# file name that you want to open is the second argument
save_file = open('../data/tweets.json', 'a')
MAX_TWEETS = 10000


class Listener(StreamListener):
    # get a dictionary with keys for the twitter api
    fr = open('../config/config.json')
    api_data = json.loads(fr.read())
    fr.close()

    def __init__(self, save_location='/data/tweets.json'):
        super().__init__()
        # self.save_location = save_location
        self.count = 0
        self.tweets = []
        # self.analyser = MoodAnalyser()
        self.save_file = self.tweets
        self.conn = sqlite3.connect('../DB/iscp.db', check_same_thread=False)

        print("Listener created")

    def on_status(self, status):

        print("Tweet starts receiving")
        self.count += 1
        # tweet = self.create_tweet(status)
        # self.analyser.analyse(tweet)
        # self.tweets.append(tweet)
        self.save_tweets()

        return

    def on_data(self, raw_data):
        print("Saving tweets to tweets.json")
        # save_file.append(json.loads(raw_data))
        save_file.write(str(raw_data))
        return True

    # def save_tweets(self):
    #     print("Saving tweets to tweets.json")
    #     f = open(os.path.dirname(__file__) + self.save_location, "w")
    #     f.write(jsonstruct.encode(self.tweets))
    #     f.close()

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

    def create_tweet(self, status):
        return Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)
