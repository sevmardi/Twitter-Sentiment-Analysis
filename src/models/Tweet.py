class Tweet(object):
    tweet = ""
    datetime = ""
    user = ""
    sentiment = ""

    def __init__(self, tweet, user, datetime):
        """
        Creates a tweet object container a tweet
        """
        self.tweet = tweet
        self.datetime = datetime
        self.user = user
        self.sentiment = ''

    def get_tweet(self):
        """
		Return the tweet
		"""
        return self.tweet

    def set_tweet(self, tweet):
        """
        Set the tweet
        """
        self.tweet = tweet

    def get_user(self):
        """
		Return the author of the tweet
		"""
        return self.user

    def set_user(self, user):
        """
		Set the user of the tweet
		"""
        self.user = user

    def get_date(self):
        """
        Returns the date of the tweet
        """
        return self.datetime

    def set_date(self, date):
        """
		Return the a datetime stamp of the tweet
		"""
        self.datetime = date

    def get_sentiment(self):
        return self.sentiment

    def set_sentiment(self, sentiment):
        self.sentiment = sentiment

    def print_tweet(self):
        print(self.get_tweet())
        print(self.get_date())
        print(self.get_user())
