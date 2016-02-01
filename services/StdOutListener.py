import regex as regex
import tweepy
from models import Twitter
from config import config
import re
import os
import json

# Variables that contains the user credentials to access Twitter API
access_token = config.access_token
access_token_secret = config.access_token_secret
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(tweepy.StreamListener):
    def __init__(self):
        super(StdOutListener, self).__init__()
        self.count = 0
        self.tweets = []
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


# if __name__ == '__main__':
#     # This handles Twitter authetification and the connection to Twitter Streaming API
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     stream = Stream(auth, l)

    # This line filter Twitter Streams to capture Data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['happiness', 'war', 'life'])
