from models import Tweet
from services import Analyser

"""

"""


class TweetProcessor():
    mood_analyzer = Analyser()
    tweets = "data/tweets"
    db = tweets
    def __init__(self):
        self.analyzed_tweet = None

    def process(self, tweet_json):
        self.analyzed_tweet = self.Analyser.analyse(Tweet(tweet_json))
        try:
            self.analyzed_tweet = None
            print(self.db.get_count())
        except:
            print("Cloud not connect to database")
            return False
        return True
