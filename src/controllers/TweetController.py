import os
import tweepy
from tweepy import Stream
from src.controllers.TweetProcessor import TweetProcessor
from src.controllers.Listener import Listener
from tweepy import OAuthHandler


class TweetController(object):
    """docstring for Controller"""

    default_keyword = "climate change"

    processor = TweetProcessor()

    def __init__(self,  tweet_gui):
        self.auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
        self.auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        #self.server = server
        self.tweet_gui = tweet_gui

    def start_stream(self, tweets_to_add):
        # max_tweet = tweets_to_add + self.processor.db.get_count()
        self.tweet_listener = Listener()
        self.stream = Stream(auth=self.auth, listener=self.tweet_listener)
        self.stream.filter(track=['climate change','earth','NASA'], async=True)
        # self.stream.filter(track=keywords, async=True)

    def list_of_tweets(self):
        f = open(os.path.dirname(__file__) + "../data/tweets.json")
        return f.read()

    def stop_streaming_tweets(self):
        self.stream.disconnect()

    # def set_keyword(self, keywords):
    #     self.keywords = keywords
    #     print(keywords)


if __name__ == '__main__':
    l = TweetController(1)
    l.start_stream('nice')
