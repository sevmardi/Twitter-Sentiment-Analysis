import re
from src.data import mood_values
from src.DB.DataBase import DataBase


class MoodAnalyser:
    def __init__(self):
        self.db = DataBase()

    def start_up(self):
        """
        A function to startup the mood analyser, fetching all the tweets and passing
        each tweet to the analyser
        :return:
        """
        count = 0
        tweets = self.db.fetch_all_tweets()
        for tweet in tweets:
            count += 1
            self.analyse(tweet, count)
            # print(tweet)

    def analyse(self, tweet, count):
        """
        Analyser each word using the moodvalue file words
        :param tweet:
        :param count:
        :return:
        """
        tweet = "".join(tweet)
        processed_text = self.process_text(tweet)
        # calculate mood
        score = 0
        for word in processed_text:
            if word in mood_values.positive_words:
                score += 0.6
            if word in mood_values.negative_words:
                score -= 0.5

        self.scoring(score, count)

    def scoring(self,tweet_score, tweet_number):
        """
        Setting the score of each tweet
        :param tweet_score:
        :param tweet_number:
        :return:
        """
        if tweet_score <= -1:
            # tweet is negative
            self.db.set_mood(tweet_number, '-1')
        elif tweet_score >= 0.5:
            # tweet is positive
            self.db.set_mood(tweet_number, "+1")
        else:
            # tweet is neutral
            self.db.set_mood(tweet_number, "0.5")

    def process_text(self, text):
        """
        A function to process the text of the tweet stripping all the links and white spaces.
        :param text:
        :return:
        """
        text = text.lower()
        # Remove links
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http://[^\s]+))', 'URL', text)
        # Remove mentions
        text = re.sub('@[^\s]+', 'MENTION', text)
        # Remove white spaces
        text = re.sub('[\s]+', ' ', text)
        # Remove hashtag from words
        text = re.sub(r'#([^\s]+)', r'\1', text)
        # trim
        text = text.strip('\'"')
        # Split text to array
        text = text.split()
        return text
