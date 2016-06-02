import os
import sys
import time
import json
import jsonstruct
from src.services.MoodAnalyser import MoodAnalyser
from src.models.Tweet import Tweet
from tweepy.streaming import StreamListener
from src.DB.DataBase import DataBase
from tweepy import Stream

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""


class Listener(StreamListener):
    # get a dictionary with keys for the twitter api
    # fr = open('config/config.json')
    # api_data = json.loads(fr.read())
    # fr.close()

    def __init__(self, save_location='data/tweets.json'):
        super().__init__()
        self.save_location = save_location
        self.count = 0
        self.analyser = MoodAnalyser()
        self.db = DataBase()
        self.max_tweets = 10000
        print("Listener created")

    def on_data(self, data):
        print('tweets receiving..')
        tweets = json.loads(data)
        try:
            if self.db.fetch_number_of_tweets() != self.max_tweets:
                timestamp = tweets['timestamp_ms']
                tweet = tweets['text']
                userData = tweets['user']
                user = userData['screen_name']

                if tweet.startswith("RT @") or tweet.startswith("@"):
                    return True
                if '"' in tweet:
                    tweet.replace('"', '')
                if '"' in user:
                    user.replace('"', '')

                self.db.insert_tweet(tweet, user, timestamp)
            else:
                # self.on_disconnect()
                self.analyser.start_up()
                return False
        except KeyError as e:
            print(e)

    def save_tweets(self):
        print("Saving tweets to tweets.json")
        f = open(os.path.dirname(__file__) + self.save_location, "w")
        f.write(jsonstruct.encode(self.tweets))
        f.close()

    # def create_tweet(self, status):
    #     return print(Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name))

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

    def on_disconnect(self):
        print("Disconnected")
        Stream.disconnect()
        return
