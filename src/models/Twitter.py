import sys

class Twitter(object):
    tweet = ""
    datetime = ""
    user = ""

    def __init__(self, Tweet):
        self.Tweet = Tweet
        self.mood = 0
        
    def getTweet(self):
        return self.tweet

    def getUser(self):
        return self.user

    def setTweet(self, tweet):
        self.tweet = tweet

    def setData(self, date):
        self.datetime = date

    def setUser(self, user):
        self.user= user
