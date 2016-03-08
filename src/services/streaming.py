from src.services import Listener

import time, tweepy, sys
# http://badhessian.org/2012/10/collecting-real-time-twitter-data-with-the-streaming-api/

## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here
auth     = tweepy.auth.BasicAuthHandler(username, password)
api      = tweepy.API(auth)


def main():
    track = ['obama', 'romney']

    listen = Listener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print ("Streaming started...")

    try:
        stream.filter(track = track)
    except:
        print ("error!")
        stream.disconnect()
