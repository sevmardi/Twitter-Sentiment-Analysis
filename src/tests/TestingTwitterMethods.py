import json
import unittest
from models import Tweet

class TestingTwitterMethods(unittest.TestCase):

    def test_name(self):
        pass

    def test_different(self):
        pass

    def test_empty_text_tweet(self):
        pass

    def test_empty_user_tweet(self):
        pass

    def create_tweet(self):
        pass

    def create_tweet_with_user(self):
        pass

    def create_tweet_without_user(self):
        pass

    def fetch_tweet(self):
        tweet = Tweet("Steve Jobs?", 19042011 ,"@Jobs")
        self.assertEquals(tweet.get_tweet(),"Steve Jobs?")
        self.assertEquals(tweet.get_date(),19042011)
        self.assertEquals(tweet.get_user(), "@Jobs")

if __name__ == '__main__':
    unittest.main()