import os
from src.DB.DataBase import DataBase
from tkinter import simpledialog
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import tkinter
from src.Listener import Listener
from src.controllers.TweetProcessor import TweetProcessor


class TweetController():
    """docstring for Controller"""

    processor = TweetProcessor()

    def __init__(self):
        self.auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
        self.auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())

        self.db = DataBase()
        # self.tweet_gui = tweet_gui
        self.default_keyword = "Trump"
        self.create_table_if_not_exist()
        self.max_tweets = 10000

    # def start_stream(self, tweets_to_add):
    #     self.tweet_listener = Listener()
    #     try:
    #         if tweets_to_add + self.db.fetch_all_tweets() != self.max_tweets:
    #             self.stream = Stream(auth=self.auth, listener=self.tweet_listener)
    #             self.stream.filter(track=[self.default_keyword], async=True)
    #         else:
    #             pass
    #     except BaseException as e:
    #         print(e)
    #
    #         return False

    def start_stream(self):
        self.reset_status()
        self.set_status("active")
        self.tweet_listener = Listener()
        self.stream = Stream(auth=self.auth, listener=self.tweet_listener)
        self.stream.filter(track=[self.default_keyword], async=True)

    def stop_stream(self):
        self.stream.disconnect()

    def set_keyword(self, default_keyword):
        self.default_keyword = default_keyword
        print(default_keyword)

    def create_table_if_not_exist(self):
        self.db.create_table_if_not_exist()

    def set_status(self, status):
        cursor = self.db.conn.cursor()
        cursor.execute("UPDATE tweets SET status=? WHERE id = 1", (status,))
        self.db.conn.commit()

    def get_status(self):
        """
        Retrieve the current status from the database (id, status, tweets_analyzed, avg_mood, pos_tweets, neg_tweets,
        neu_tweets).
        """
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM tweets WHERE id = 1")
        result = cursor.fetchall()
        return result[0]

    def reset_status(self):
        """
        Reset the current status.
        """
        cursor = self.db.conn.cursor()
        cursor.execute(
            "UPDATE tweets SET tweets_retrieved=?, avg_mood=?, pos_tweets=?, neg_tweets=?, neu_tweets=? WHERE id = 1",
            (0, 'neu', 0, 0, 0,))
        self.db.conn.commit()


if __name__ == '__main__':
    controller = TweetController()
    controller.start_stream()
