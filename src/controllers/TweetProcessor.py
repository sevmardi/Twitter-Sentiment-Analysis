import os
from src.models.Tweet import Tweet
from src.services.MoodAnalyser import MoodAnalyser



"""
Class used to retrieve Tweets from the twitter api. It uses the Twitter stream api.
"""


class TweetProcessor:
    mood_analyser = MoodAnalyser()



    def process(self, tweet):
        # analyser returns model.tweet object
        self.analysed_tweet = self.mood_analyser.analyse(Tweet(tweet))
        return True
