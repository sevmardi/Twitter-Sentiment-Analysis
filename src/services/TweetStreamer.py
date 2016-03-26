import json
import os
import time
import sys
from tweepy import *
from models import Tweet
from services import TweetStreamer

"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""


class TweetStreamer(StreamListener):
    def __init__(self, api=None, fprefix='streamer'):
        super().__init__(api)
        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.tweets = []
        self.output = open(fprefix + '.' + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        # self.delout = open('delete.txt', 'a')
        self.time = int(time.time())
        self.tweets_data_path = "../data/tweets.json"
        print("Started streaming..")
        self.processor = TweetProcessor()

    def on_data(self, data):
        if 'in_reply_to_status' in data:
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
            print(warning['message'])
            return False

    def on_error(self, status):
        print(status)

    def on_delete(self, status_id, user_id):
        self.delout.write(str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        """
		Called when a error is recieved from the Twitter api.
		"""
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return

    def on_status(self, status):
        """
        Called when a tweet is recieved. It creates a Tweet object and passes it to the Analyser. It saves the tweet
        in memory and writes the recieved tweet count to the database.
        """
        print("Tweet recieved")
        if self.counter <= 10:
            self.tweets.append(self.create_tweet(status))
            self.counter += 1
            return True
        self.store_tweets()
        return False

    def store_tweets(self):
        """
		Saves in memory tweets to given save save_location.
		"""
        print("Saving tweets to tweets.json")
        f = open(os.path.dirname(__file__) + self.tweets_data_path, "w")
        for tweet in self.tweets:
            f.write(json.dumps(tweet.__dict__))
            f.close()

    def create_tweet(self, status):
        pass

    def disconnect(self, notice):
        """
		Called when twitter sends a disconnect notice
		Disconnect codes are listed here:
		https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
		"""
        print("disconnected")
        self.store_tweets()
        return
