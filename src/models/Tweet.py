import sys


class Tweet(object):
    tweet = ""
    datetime = ""
    user = ""

    def __init__(self, tweet, user, datetime):
        """
        Creates a tweet object container a tweet
        """
        try:
            self.username = tweet['user']['name']
        except:
            print(sys.exc_info()[0])
        try:
            self.text = tweet['text']
        except KeyError:
            self.text = ""
        except:
            print(sys.exc_info()[0])

        self.mood = 0

        self.tweet = tweet
        self.datetime = datetime
        self.user = user

    def get_tweet(self):
        """
		Return the tweet
		"""
        return self.tweet

    def get_user(self):
        """
		Return the author of the tweet
		"""
        return self.user

    def get_date(self, date):
        """
        Returns the date of the tweet
        """
        self.datetime = date

    def set_tweet(self, tweet):
        """
        Set the tweet
        """
        self.tweet = tweet

    def set_date(self, date):
        """
		Return the a datetime stamp of the tweet
		"""
        self.datetime = date

    def set_user(self, user):
        """
		Set the user of the tweet
		"""
        self.user = user
