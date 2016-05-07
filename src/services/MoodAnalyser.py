import re
from src.data import mood_values
from src.DB.DataBase import DataBase


class MoodAnalyser:
    def __init__(self):
        self.db = DataBase()

    def start_up(self):
        count = 0
        tweets = self.db.fetch_all_tweets()
        for tweet in tweets:
            count += 1
            self.analyse(tweet, count)

    def analyse(self, tweet, count):
        tweet = "".join(tweet)
        # processed_text = self.process_text(tweet)

        # calculate mood
        score = 0
        for word in tweet.split():
            if word in mood_values.positive_words:
                score += 0.6
            if word in mood_values.negative_words:
                score -= 0.5

        self.scoring(score, count)

    def scoring(self,tweetScore, tweetNummer):
        print("Dit is tweet #" + str(tweetNummer))
        if tweetScore <= -1:
            # tweet is negative
            self.db.set_mood(tweetNummer, '-1')
        elif tweetScore >= 0.5:
            # tweet is positive
            self.db.set_mood(tweetNummer, "+1")
        else:
            # tweet is neutral
            self.db.set_mood(tweetNummer, "0.5")


    # @staticmethod
    # def process_text(text):
    #     # text = text.lower()
    #     # Remove links
    #     text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http://[^\s]+))', 'URL', text)
    #     # Remove mentions
    #     text = re.sub('@[^\s]+', 'MENTION', text)
    #     # Remove white spaces
    #     text = re.sub('[\s]+', ' ', text)
    #     # Remove hashtag from words
    #     text = re.sub(r'#([^\s]+)', r'\1', text)
    #
    #     # trim
    #     text = text.strip('\'"')
    #     # Split text to array
    #     text = text.split()
    #     return text
