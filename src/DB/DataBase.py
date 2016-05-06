import sqlite3



class DataBase(object):
    def __init__(self):
        self.conn = sqlite3.connect('DB/iscp.db', check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table_if_not_exist(self):
        self.cur.execute("DROP TABLE IF EXISTS tweets")
        self.cur.execute(
            "CREATE TABLE tweets (id INTEGER PRIMARY KEY AUTOINCREMENT, tweet TEXT, user TEXT, date DATE, score INT)")
        self.conn.commit()

    def insert_tweet(self, tweet, user, date):
        self.cur.execute("INSERT INTO tweets (tweet, user, date) VALUES (?,?, ?)", (tweet, user, date))
        self.conn.commit()
        print("Tweets is added")

    def get_timeChart(self):
        cursor = self.conn.cursor()
        data = (cursor.fetchall())
        return data

    def fetch_number_of_tweets(self):
        self.cur.execute("SELECT COUNT(tweet) FROM tweets")
        number_of_tweets = self.cur.fetchone()[0]
        return number_of_tweets

    def fetch_all_tweets(self):
        sqlCall = self.cur.execute("SELECT tweet FROM tweets")
        tweets = sqlCall.fetchall()
        return tweets

    def set_mood(self, id, analyse):
        self.cur.execute("UPDATE tweets SET score = ? WHERE id = ?", (analyse, id))
        self.conn.commit()

    def get_mood(self):
        self.cur.execute("SELECT COUNT(score) FROM tweets WHERE score = -1")
        negatieve_woorden = self.cur.fetchone()[-1]

        self.cur.execute("SELECT COUNT(score) FROM tweets WHERE score = 0.5")
        neutrale_woorden = self.cur.fetchone()[5]

        self.cur.execute("SELECT COUNT(score) FROM tweets WHERE score = +1")
        positieve_woorden = self.cur.fetchone()[+1]

        analyseLijst = [negatieve_woorden, neutrale_woorden, positieve_woorden]

        return analyseLijst
