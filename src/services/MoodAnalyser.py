import re
import json


class MoodAnalyser:
    def __init__(self):
        # initiate the moods dictionary from json
        try:
            fr = open("../data/mood_value.json", "r")
            mood_json = fr.read()
            self.mood_values = json.loads(mood_json)['moods']
            self.mood_values_tbd = json.loads(mood_json)['TBD']
            fr.close()
        except BaseException as e:
            print('Mood/value file not found.', e)

    # TODO
    def analyse(self, tweet):
        tweet.mood = self.get_mood(tweet.text)

        return tweet

    def get_mood(self, tweet_text):
        # clean up the string, make it a dictionary
        clear_tweet_text = self._process_text(tweet_text)
        tweet_dict = str(clear_tweet_text).split(' ')

        # we are going to calculate mood
        mood = 0

        # mood dict build: [word]:[amount]
        # What we do with it:
        # calculate the word mood value (negative / positive)
        for word in tweet_dict:
            word = word
            word_mood = self._calculate_mood(word.lower())
            mood += word_mood
        return mood

    def _calculate_mood(self, tweet_word):
        if tweet_word in self.mood_values.keys():
            return self.mood_values[tweet_word]
        elif tweet_word in self.mood_values_tbd.keys():
            return self.mood_values_tbd[tweet_word]
        else:
            return 0

    # TODO
    def _process_text(self, text):
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
        text = text.split('\'"')
        return text
