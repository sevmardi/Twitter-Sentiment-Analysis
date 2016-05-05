import re
from src.data import mood_values


class MoodAnalyser:
    def __init__(self):
        pass

    def analyse(self, tweet):

        processed_text = self.process_text(tweet.get_tweet())

        # calculate mood
        score = 0

        for word in processed_text:
            if word in mood_values.positive_words:
                score += 0.6
            if word in mood_values.negative_words:
                score -= 0.5
        if score <= -0.5:
            tweet.set_sentiment("neg")
        elif score >= 0.5:
            tweet.set_sentiment("pos")
        else:
            tweet.set_sentiment("neu")

    # def get_mood(self, tweet):
    #     text_clean_up  = self.clear_text(tweet_text)
    #     tweet_dict = str(text_clean_up).split(' ')
    #
    # def clear_text(self, text):
    #     text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    def process_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
        # Remove links
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http://[^\s]+))', 'URL', text)

        # Remove mentions
        text = re.sub('@[^\s]+', 'MENTION', text)
        # Remove white spaces
        text = re.sub('[\s]+', ' ', text)
        # Remove hashtag from words
        text = re.sub(r'#([^\s]+)', r'\1', text)
        # trim
        text = text.strip(' ')
        # trim
        text = text.split(' ')
        return text
