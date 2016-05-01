#KEYWORD(S) TO LOOK FOR?
#query = 'snow OR snowing OR snowflakes'
#query = 'powder AND mountain'
query = 'cat'

#HOW MANY TWEETS?
num_tweets = 10

fr = open('../config/config.json')
api_data = json.loads(fr.read())
fr.close()

import tweepy
from tweepy import  *
import urllib2
import json
import re
import unicodedata
from src.Listener import  Listener

auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

