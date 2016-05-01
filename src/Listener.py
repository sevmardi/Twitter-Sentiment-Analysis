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
from src.DB.DataBase import DataBase

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""

# tweets = []
# file name that you want to open is the second argument
save_file = open('data/tweets.json', 'a')


class Listener(StreamListener):
    # get a dictionary with keys for the twitter api
    fr = open('config/config.json')
    api_data = json.loads(fr.read())
    fr.close()

    def __init__(self, save_location='/data/tweets.json'):
        super().__init__()
        self.save_location = save_location
        self.count = 0
        self.tweets = []
        self.analyser = MoodAnalyser()
        # self.save_file = self.tweets
        self.db = DataBase()
        self.max_tweets = 10000
        print("Listener created")

    def on_status(self, status):
        """
		Called when a tweet is recieved. It creates a Tweet object and passes it to the Analyser. It saves the tweet
		in memory and writes the recieved tweet count to the database.
		"""
        if self.db.get_status() == "active":
            self.count += 1
            tweet = self.create_tweet(status)
            self.analyser.analyse(tweet)
            self.tweets.append(tweet)
            self.db.save_count()
            return True
        # print("Tweet starts receiving")
        # self.save_tweets()
        return False

    def on_data(self, raw_data):
        try:
            if raw_data + self.db.fetch_number_of_tweets() != self.max_tweets:
                save_file.write(str(raw_data))
            # TODO
            else:
                print("Too Many tweets")

        except BaseException as e:
            print(e)

            return False

    # def save_tweets(self):
    #     print("Saving tweets to tweets.json")
    #     f = open(os.path.dirname(__file__) + self.save_location, "w")
    #     f.write(jsonstruct.encode(self.tweets))
    #     f.close()

    def on_error(self, status_code):
        """
		Called when a error is recieved from the Twitter api.
		"""
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
        """
		Creates a tweet from the given json object from the twitter api.
		"""
        print("Disconnected")
        self.save_tweets()
        return

    def create_tweet(self, status):
        """
		Creates a tweet from the given json object from the twitter api.
		"""
        return Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)
