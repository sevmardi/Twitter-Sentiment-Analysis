import json
import os
import re
import time
import sys
import regex as regex
import tweepy
from src.models import Tweet
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener


""" Read the config file"""
f = open("../config/config.json")
config = json.loads(f.read())
f.close()



# This is a basic listener that just prints received tweets to stdout.
class Listener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):

        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open(fprefix + '.'
                            + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        self.delout  = open('delete.txt', 'a')

        self.time = int(time.time())
        self.tweets_data_path = "../data/tweets.json"

    def on_data(self, data):

        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print (warning['message'])
            return False

    def on_error(self, status):
        print(status)

    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return

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
        return Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)

    def store_tweets(self):
        f = open(os.path.dirname(__file__) + self.store_tweets(), "w")
        for tweet in self.tweets:
            f.write(json.dumps(tweet.__dict__))
            f.close()
