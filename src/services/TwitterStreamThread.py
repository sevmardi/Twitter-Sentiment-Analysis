import sys
import threading
from TwitterAPI.TwitterError import TwitterRequestError, TwitterConnectionError
from controller.TwitterLib.TweetProcessor import TweetProcessor
from tweepy import error, streaming


class TwitterStreamThread(threading.Thread):
    processor = TweetProcessor()

    def __init__(self, search_word, api, numbers_to_add):
        threading.Thread.__init__(self)
        self.api = api
        self.search_word = search_word
        self.numbers_to_add = numbers_to_add

        self.loop = True

    def run(self):
        try:
            r = self.api.request('', {'track': self.search_word})
            for tweet_json in r.get_iterator():
                if not self.processor.process(tweet_json):
                    break
                if self.processor.json.count() >= self.numbers_to_add:
                    self.loop_error = True
                    break

        except TwitterRequestError:
            print("Twitter api credentials don't seem to be working.")
        except TwitterConnectionError:
            print("Could not connect to the internet. Please check your connection.")
        except:
            if (self.loop_error):
                print("Could not start stream; Check connection\n" + sys.exc_info()[0])
