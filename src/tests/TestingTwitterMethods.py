import unittest
import tweepy
from src.models.Tweet import Tweet
from unittest.mock import create_autospec, MagicMock, ANY, patch
from src.config.TwitterAccount import TwitterAccount
from src.config.Settings import Settings


class MockedUser(object):
    protected = False


class TestingTwitterMethods(unittest.TestCase):
    def set_up(self):
        self.api = Settings.get_tweepy_api()
        self.api.retry_count = 2
        self.api.retry_delay = 5

    def test_first(self):
        pass
        # Test
        # api = create_autospec(tweepy.API, _name='FirstAPI')
        # api.get_user = MagicMock(return_value=MockedUser)
        # tweepy.API = MagicMock(return_value=api)
        # self.assertTrue(TwitterAccount.validate('123'))
        # api.get_user.assert_called_once_with('123')

    def test_fetch_tweet(self):
        tweet = Tweet("Steve Jobs?", 19042011, "@Jobs")
        self.assertEquals(tweet.get_tweet(), "Steve Jobs?")
        self.assertEquals(tweet.get_date(), 19042011)
        self.assertEquals(tweet.get_user(), "@Jobs")

    @patch.object(tweepy.API, 'get_user', return_value=MockedUser)
    def test_case_two(self, tweepy_api):
        self.assertTrue(TwitterAccount.validate('123'))
        tweepy_api.assert_called_once_with(ANY)

    @patch('tw.tweepy.API', autospec=True)
    def test_case_third(self, tweepy_api):
        tweepy_api.get_user = MagicMock(return_value=MockedUser)
        self.assertTrue(TwitterAccount.validate('123'))

    def test_same(self):
        self.assertEqual(self.create_tweet, self.create_tweet)
        print("Testing equals")

    def create_tweet(self):
        return self.Tweet.set_tweet('test user')


if __name__ == '__main__':
    unittest.main()
