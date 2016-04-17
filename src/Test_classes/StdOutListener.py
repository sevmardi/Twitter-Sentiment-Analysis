from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

f = open("../config/config.json")
config = json.loads(f.read())
f.close()

access_token = config["access_token"]
access_token_secret = config['access_token_secret']
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']

tweets = []
# file name that you want to open is the second argument
save_file = open('../data/tweets.json', 'a')


class StdOutListener(StreamListener):
    def __init__(self):
        super().__init__()

        self.save_file = tweets
        print("Listener created")

    def on_data(self, raw_data):
        self.save_file.append(json.loads(raw_data))
        print(raw_data)
        save_file.write(str(raw_data))
        print("Tweet received")
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['python', 'ruby'])
