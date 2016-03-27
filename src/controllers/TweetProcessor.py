from models import Tweet
from services import Analyser
from tweepy.streaming import StreamListener
import os
import time
import io
"""

"""

class TweetProcessor(StreamListener):

    def __init__(self, start_time, time_limit=60):
        mood_analyzer = Analyser()
        self.tweet_data = []
        self.time = start_time
        self.limit = time_limit

    def process(self, tweet_json):
        self.analyzed_tweet = self.Analyser.analyse(Tweet(tweet_json))

        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
        # write to file
        try:

            print(self.db.get_count())
        except:
            print("Cloud not connect to database")
            return False
        return True
