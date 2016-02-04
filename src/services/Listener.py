import json
import os
import re
import time

import regex as regex
import tweepy
from src.models import Twitter
from tweepy import OAuthHandler
from tweepy import Stream

""" Read the config file"""
f = open("../config/config.json")
config = json.loads(f.read())
f.close()



# This is a basic listener that just prints received tweets to stdout.
class Listener(tweepy.StreamListener):
    def __init__(self):
        super(Listener, self).__init__()
      #  self.identifier = keyword
        self.time = int(time.time())
        self.tweets_data_path = "../data/tweets.json"

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

    def word_in_text(word, text):
        word = word.lower()
        text = text.lower()
        match = re.search(regex, text)
        if match:
            return match.group()
        return ''

    def tweetStatus(self, status):
        if self.count <= 10:
            self.tweets.append(self.create_tweet(status))
            self.count = +1
            return True
        self.store_tweets()
        return False

    def disconnect(self, notice):
        self.store_tweets()
        return

    def create_tweet(self, status):
        return Twitter(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)

    def store_tweets(self):
        f = open(os.path.dirname(__file__) + self.store_tweets(), "w")
        for tweet in self.tweets:
            f.write(json.dumps(tweet.__dict__))
            f.close()


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = Listener()
    auth = OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token"], config["access_token_secret"])
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])