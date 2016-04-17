import re
import json


class MoodAnalyser:

    def __init__(self):
        # initiate the moods dictionary from json
        try:
            fr = open("data/mood_value.json", "r")
            mood_json = fr.read()
            self.mood_values = json.loads(mood_json)['moods']
            self.mood_values_tbd = json.loads(mood_json)['TBD']
            fr.close()
        except BaseException as e:
            print('Mood/value file not found.', e)

    def analyse(self, tweet):
        tweet.mood = self.get_mood(tweet.get_tweet())

        return tweet

    def get_mood(self, tweet_text):
        # clean up the string, make it a dictionary
        clear_tweet_text = self._clear_text(tweet_text)
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

    def _clear_text(self, text):
        text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
        return text

        # def word_in_text(word, text):
        #     word = word.lower()
        #     text = text.lower()
        #     match = re.search(word, text)
        #     if match:
        #         return True
        #     else:
        #         return False

        # def extract_link(text):
        #     regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        #     match = re.search(regex, text)
        #     if match:
        #         return match.group()
        #     return ''
