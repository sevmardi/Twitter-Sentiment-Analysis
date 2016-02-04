from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import rcParams
from mpltools import style
from matplotlib import dates
from datetime import datetime
import seaborn as sns
import time
import os
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import random


# Seaborn plots
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
# for R lovers :)
style.use('ggplot')
rcParams['axes.labelsize'] = 9
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 7
# rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['text.usetex'] = False
rcParams['figure.figsize'] = 20, 10

MAX_TWEETS = 10000
data = Cursor(api.search, q='mozsprint').items(MAX_TWEETS)


mozsprint_data = []
# You will use this line in production instead of this
# current_working_dir = os.path.dirname(os.path.realpath(__file__))
current_working_dir = "./"
log_tweets = current_working_dir  + str(time.time()) + '_moztweets.txt'
with open(log_tweets, 'w') as outfile:
    for tweet in data:
        mozsprint_data.append(json.loads(json.dumps(tweet._json)))
        outfile.write(json.dumps(tweet._json))
        outfile.write("\n")


 print mozsprint_data[0]

{u'contributors': None, u'truncated': False, u'text': u'RT @justin_littman: Just downloaded the @ORCID_Org public data file (http://t.co/pEtCav7cKf) to find some examples for https://t.co/84Fflcz\u2026', u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 607297684182036480, u'favorite_count': 0, u'source': u'<a href="http://www.flipboard.com" rel="nofollow">Flipboard</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [{u'indices': [3, 18], u'screen_name': u'justin_littman', u'id': 481186914, u'name': u'Justin Littman', u'id_str': u'481186914'}, {u'indices': [40, 50], u'screen_name': u'ORCID_Org', u'id': 148815591, u'name': u'ORCID Organization', u'id_str': u'148815591'}], u'hashtags': [{u'indices': [139, 140], u'text': u'mozsprint'}], u'urls': [{u'url': u'http://t.co/pEtCav7cKf', u'indices': [69, 91], u'expanded_url': u'http://bit.ly/1Mar5Xj', u'display_url': u'bit.ly/1Mar5Xj'}, {u'url': u'https://t.co/84FflczWaX', u'indices': [119, 140], u'expanded_url': u'https://github.com/gwu-libraries/orcid2vivo', u'display_url': u'github.com/gwu-libraries/\u2026'}]}, u'in_reply_to_screen_name': None, u'id_str': u'607297684182036480', u'retweet_count': 9, u'in_reply_to_user_id': None, u'favorited': False, u'retweeted_status': {u'contributors': None, u'truncated': False, u'text': u'Just downloaded the @ORCID_Org public data file (http://t.co/pEtCav7cKf) to find some examples for https://t.co/84FflczWaX for #mozsprint.', u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 606786791237107712, u'favorite_count': 13, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [{u'indices': [20, 30], u'screen_name': u'ORCID_Org', u'id': 148815591, u'name': u'ORCID Organization', u'id_str': u'148815591'}], u'hashtags': [{u'indices': [127, 137], u'text': u'mozsprint'}], u'urls': [{u'url': u'http://t.co/pEtCav7cKf', u'indices': [49, 71], u'expanded_url': u'http://bit.ly/1Mar5Xj', u'display_url': u'bit.ly/1Mar5Xj'}, {u'url': u'https://t.co/84FflczWaX', u'indices': [99, 122], u'expanded_url': u'https://github.com/gwu-libraries/orcid2vivo', u'display_url': u'github.com/gwu-libraries/\u2026'}]}, u'in_reply_to_screen_name': None, u'id_str': u'606786791237107712', u'retweet_count': 9, u'in_reply_to_user_id': None, u'favorited': False, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'id': 481186914, u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/496478011533713408/GjecBUNj_normal.jpeg', u'profile_sidebar_fill_color': u'DDEEF6', u'is_translator': False, u'geo_enabled': True, u'entities': {u'description': {u'urls': []}}, u'followers_count': 35, u'protected': False, u'location': u'', u'default_profile_image': False, u'id_str': u'481186914', u'lang': u'en', u'utc_offset': -14400, u'statuses_count': 38, u'description': u'', u'friends_count': 40, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/496478011533713408/GjecBUNj_normal.jpeg', u'notifications': False, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'profile_background_color': u'C0DEED', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'name': u'Justin Littman', u'is_translation_enabled': False, u'profile_background_tile': False, u'favourites_count': 21, u'screen_name': u'justin_littman', u'url': None, u'created_at': u'Thu Feb 02 12:19:18 +0000 2012', u'contributors_enabled': False, u'time_zone': u'Eastern Time (US & Canada)', u'profile_sidebar_border_color': u'C0DEED', u'default_profile': True, u'following': False, u'listed_count': 1}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Fri Jun 05 11:36:59 +0000 2015', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'id': 64645233, u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/1717565784/image_normal.jpg', u'profile_sidebar_fill_color': u'DDFFCC', u'is_translator': False, u'geo_enabled': True, u'entities': {u'description': {u'urls': []}}, u'followers_count': 63, u'protected': False, u'location': u'Helsinki', u'default_profile_image': False, u'id_str': u'64645233', u'lang': u'en', u'utc_offset': 10800, u'statuses_count': 212, u'description': u'', u'friends_count': 198, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/1717565784/image_normal.jpg', u'notifications': False, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme16/bg.gif', u'profile_background_color': u'9AE4E8', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme16/bg.gif', u'name': u'Annikki Roos', u'is_translation_enabled': False, u'profile_background_tile': False, u'favourites_count': 39, u'screen_name': u'AnnikkiRoos', u'url': None, u'created_at': u'Tue Aug 11 06:27:12 +0000 2009', u'contributors_enabled': False, u'time_zone': u'Helsinki', u'profile_sidebar_border_color': u'BDDCAD', u'default_profile': False, u'following': False, u'listed_count': 7}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Sat Jun 06 21:27:05 +0000 2015', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}


 # Create the dataframe we will use
tweets = pd.DataFrame()
# We want to know when a tweet was sent
tweets['created_at'] = map(lambda tweet: time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')), mozsprint_data)
# Who is the tweet owner
tweets['user'] = map(lambda tweet: tweet['user']['screen_name'], mozsprint_data)
# How many follower this user has
tweets['user_followers_count'] = map(lambda tweet: tweet['user']['followers_count'], mozsprint_data)
# What is the tweet's content
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), mozsprint_data)
# If available what is the language the tweet is written in
tweets['lang'] = map(lambda tweet: tweet['lang'], mozsprint_data)
# If available, where was the tweet sent from ?
tweets['Location'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, mozsprint_data)
# How many times this tweet was retweeted and favorited
tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], mozsprint_data)
tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], mozsprint_data)


