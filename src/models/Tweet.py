import sys

class Tweet(object):
    tweet = ""
    datetime = ""
    user = ""

    def __init__(self, Tweet):
        self.Tweet = Tweet
        self.mood = 0

    def get_tweet(self):
        return self.tweet

    def get_user(self):
        return self.user

    def set_tweet(self, tweet):
        self.tweet = tweet

    def set_data(self, date):
        self.datetime = date

    def set_user(self, user):
        self.user= user
