from models import Tweet


class TweetProcessor():
    mood_analyzer = MoodAnalyzer()
    db = tweetsjson

    def __init__(self):
        self.analyzed_tweet = None

    def process(self, tweet_json):
        self.analyzed_tweet = self.mood_analyzer.analyse(Tweet(tweet_json))

        try:
            self.analyzed_tweet = None
            print(self.db.get_count())
        except:
            print("Cloud not connect to database")
            return False

        return True
