import tweepy
from src.config.Settings import Settings


class TwitterAccount(object):
    def __init__(self):
        self.settings = Settings()

    def validate(self, user_id):
        try:
            api = self.settings.get_tweepy_api()
            print('object api', api)
            tuser = api.get_user(user_id)
            print('method', api.get_user)
            print('tuser', tuser)
            if tuser.protected:
                return False
        except tweepy.TweepError:
            return False

        return True
