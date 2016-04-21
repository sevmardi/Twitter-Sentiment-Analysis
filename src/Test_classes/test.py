# import sqlite3
#
# conn = sqlite3.connect(r"../DB/iscp.db")
# print("Database created and opened succesfully")


import json
from pymongo import MongoClient
import datetime


class MongoAdapter:
    def __init__(self):
        self.client = MongoClient()

        self.db = self.client["tweet_stream"]
        self.collection = self.db["happy"]
        self.emptyDbMessage = "Fetching new tweets..."

        self.start()

    def start(self):
        try:
            fr = open("../Test_classes/DbSettings.json", "r")
            settings = fr.read()
            fr.close()

            self.set_db_settings(settings)
        except FileNotFoundError:
            print('DB Settings file not found. Setting default DB and Collection: ' +
                  str(self.db.name + " " + self.collection.name))
        except:
            print('Unknown error setting DB values. Trying to set default DB and Collection: ' +
                  str(self.db.name + " " + self.collection.name))

    def set_db_settings(self, settings):
        self.db = self.client[json.loads(settings)['tweet_db']]
        self.collection = self.db[json.loads(settings)['tweet_db_tweet_collection']]
        self.emptyDbMessage = json.loads(settings)['empty_message']

    def set_collection(self, collection_name):
        self.collection = self.db[collection_name]

    def get_collections(self):
        return self.db.collection_names()

    def insert_one(self, tweet_obj):
        # insert one tweet
        result = self.collection.insert_one({"username":tweet_obj.username,
                                             "text":tweet_obj.text,
                                             "mood":tweet_obj.mood,
                                             "timestamp_ms":datetime.datetime.now()})
        # return result in console
        print("Inserted tweet. ID:\n" + str(result.inserted_id))

    def get_tweets(self):
        cursor = self.collection.find()

        # return iterable cursor
        return cursor

    def get_last(self):
        try:
            last_tweet = self.collection.find_one(sort=[("timestamp_ms", -1)])
            print(last_tweet)
            text = last_tweet['text']
        except:
            text = self.emptyDbMessage

        encoded_str = text.encode("utf8")
        return str(encoded_str)

    def get_count(self):
        try:
            self.count = self.collection.count()
        except:
            self.count = 0
        return self.count

    def get_collection_count(self, collection):
        old_collection = self.collection.name

        self.set_collection(collection)

        try:
            self.count = self.collection.count()
        except:
            self.count = 0

        self.set_collection(old_collection)

        return self.count

if __name__ == '__main__':
    mongo = MongoAdapter()


