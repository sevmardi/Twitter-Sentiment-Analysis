import os

from models import Tweet
from services import Analyser

import jsonstruct
from tweepy.streaming import StreamListener

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""


class TweetProcessor(StreamListener):
    def __init__(self, start_time, time_limit=60, save_location="src/data/tweets.json"):
        super().__init__()
        # self.tweets = []
        # self.time = time.time()
        self.analysed_tweet = None
        self.counter = 0
        self.limit = time_limit
        self.save_location = save_location
        self.analyser = Analyser()

    # TODO
    # def on_status(self, status):
    #     print("Tweet receiving")
    #     self.counter += 1
    #     self.analyser.analyse(tweet)
    #     self.save_tweets()

    def process(self, tweet_json):
        self.analysed_tweet = self.analyser.analyse(Tweet(tweet_json))
        print("Tweet receiving..")
        try:
            self.save_tweets(self.analysed_tweet)
        except BaseException as e:
            # self.analysed_tweet None
            print("Could not connect", e)
            return False
        return True

    def on_error(self, status_code):
        print(str(status_code))

    def on_disconnect(self, notice):
        print("disconnected!")
        # self.save_tweets()
        return

    def save_tweets(self, tweets):
        print("saving tweets in file")
        f = open(os.path.dirname(__file__) + self.save_location, "w")
        f.write(jsonstruct.encode(tweets))
        f.close()
