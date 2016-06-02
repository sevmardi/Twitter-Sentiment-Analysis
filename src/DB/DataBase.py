import sqlite3


class DataBase(object):
    def __init__(self):
        """
        Establish connection with db
        :return:
        """
        self.conn = sqlite3.connect('DB/iscp.db', check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table_if_not_exist(self):
        """
        Create a database if one not exist
        :return:
        """
        self.cur.execute("DROP TABLE IF EXISTS tweets")
        self.cur.execute(
            "CREATE TABLE tweets (id INTEGER PRIMARY KEY AUTOINCREMENT, tweet TEXT, user TEXT, date DATE, score INT)")
        self.conn.commit()

    def insert_tweet(self, tweet, user, date):
        """
        Insert tweets into database
        :param tweet:
        :param user:
        :param date:
        :return:
        """
        self.cur.execute("INSERT INTO tweets (tweet, user, date) VALUES (?,?, ?)", (tweet, user, date))
        self.conn.commit()
        print("Tweets is added")

    def fetch_number_of_tweets(self):
        """
        Fetch only number of tweets given
        :return: number_of_tweets
        """
        self.cur.execute("SELECT COUNT(tweet) FROM tweets")
        number_of_tweets = self.cur.fetchone()[0]
        return number_of_tweets

    def fetch_all_tweets(self):
        """
        Fetch all the tweets available
        :return:tweets
        """
        sqlCall = self.cur.execute("SELECT tweet FROM tweets")
        tweets = sqlCall.fetchall()
        return tweets

    def set_mood(self, id, analyse):
        """
        Set the mood of a tweet
        :param id:
        :param analyse:
        :return:
        """
        self.cur.execute("UPDATE tweets SET score = ? WHERE id = ?", (analyse, id))
        self.conn.commit()

    def get_mood(self):
        """
        Get the mood using the scores
        :return: analyseLijst
        """
        self.cur.execute("SELECT COUNT(score) FROM tweets WHERE score = -1")
        negetive_words = self.cur.fetchone()[0]

        self.cur.execute("SELECT COUNT(score) FROM tweets WHERE score = 0.5")
        neutral_words = self.cur.fetchone()[0]

        self.cur.execute("SELECT COUNT(score) FROM tweets WHERE score = +1")
        positive_words = self.cur.fetchone()[0]

        analyseLijst = [negetive_words, neutral_words, positive_words]

        return analyseLijst

    def get_time_chart(self):
        """
        get the date, score from the tweets
        :return: data
        """
        self.cur.execute("SELECT date, score FROM tweets ORDER BY date ASC")
        data = (self.cur.fetchall())
        return data

    def fetch_all_scores(self):
        """
        Fetch all the scores
        :return:
        """
        sqlCall = self.cur.execute("SELECT score FROM tweets")
        scores = sqlCall.fetchall()

        return scores