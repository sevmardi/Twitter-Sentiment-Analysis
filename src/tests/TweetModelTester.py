import json
import unittest


class TweetModelTester(object):
    """docstring for TweetModelTester"""

    def __init__(self, arg):
        super(TweetModelTester, self).__init__()
        self.arg = arg

    def test_create_tweet(self):
        return Tweet({
            "user": {"name": "test operator"},
            "text": "This tweet is just a test"
        })


if __name__ == '__main__':
    unittest.main()
