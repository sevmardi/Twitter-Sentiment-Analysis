from src.DB.DataBase import DataBase
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from src.Listener import Listener
from src.config.Settings import Settings


class TweetController:
    """docstring for Controller"""

    def __init__(self):
        self.settings = Settings()
        # self.auth = OAuthHandler(Listener.api_data["consumer_key"], Listener.api_data["consumer_secret"])
        # self.auth.set_access_token(Listener.api_data["access_token"], Listener.api_data["access_token_secret"])
        self.api = tweepy.API(self.settings.auth, parser=tweepy.parsers.JSONParser())

        self.db = DataBase()
        # self.tweet_gui = tweet_gui
        self.default_keyword = ['Obama', 'hillary ', 'Trump']
        self.db.create_table_if_not_exist()

    def start_stream(self):
        self.tweet_listener = Listener()
        self.stream = Stream(auth=self.settings.auth, listener=self.tweet_listener)
        self.stream.filter(track=self.default_keyword, async=True)

    def stop_stream(self):
        self.stream.disconnect()

    def set_keyword(self, default_keyword):
        self.default_keyword = default_keyword
        print(default_keyword)


#
if __name__ == '__main__':
    controller = TweetController()
    controller.start_stream()
