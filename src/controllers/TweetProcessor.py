from models import Tweet
from services import Analyser
from tweepy.streaming import StreamListener
import os
import time
import jsonstruct


class TweetProcessor(StreamListener):
    def __init__(self, start_time, time_limit=60, save_location="/../../tweets.json"):
        super().__init__()
        self.mood_analyzer = Analyser()
        self.tweets = []
        self.time = time.time()
        self.counter = 0
        self.limit = time_limit
        self.save_location = save_location
        self.analyser = Analyser()

    # TODO
    def on_status(self, status):
        print("Tweet receiving")
        self.counter += 1
        self.analyser.analyse(tweet)
        self.save_tweets()

    # TODO
    def process(self, tweet_json, data):
        pass

    def on_error(self, status_code):
        print(str(status_code))

    def on_disconnect(self, notice):
        print("disconnected")
        self.save_tweets()
        return

    def save_tweets(self):
        print("saving tweets in file")
        f = open(os.path.dirname(__file__) + self.save_location, "w")
        f.write(jsonstruct.encode(self.tweets))
        f.close()
