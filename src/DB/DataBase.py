import sqlite3


class DataBase(object):
    def __init__(self):
        self.conn = sqlite3.connect('../DB/iscp.db', check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table_if_not_exist(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `tweets` (`id` INTEGER PRIMARY KEY AUTOINCREMENT,`status` TEXT,`tweets_retrieved` INTEGER,`avg_mood` TEXT, `pos_tweets` INTEGER, `neg_tweets` INTEGER, `neu_tweets` INTEGER)")
        cursor.execute(
            "INSERT OR IGNORE INTO `tweets`(`id`, `status`, `tweets_retrieved`,`avg_mood`, `pos_tweets`, `neg_tweets`, `neu_tweets`) VALUES(1, 'inactive', 0, 'neu', 0, 0, 0)")
        self.conn.commit()

    def get_timeChart(self):
        cursor = self.conn.cursor()
        data = (self.cur.fetchall())
        return data

    def fetch_number_of_tweets(self):
        self.cur.execute("SELECT COUNT(tweets_retrieved) FROM tweets")
        numberOfTweets = self.cur.fetchone()[0]
        return numberOfTweets

    def fetch_all_tweets(self):
        sqlCall = self.cur.execute("SELECT tweets_retrieved FROM tweets")
        tweets = sqlCall.fetchall()
        return tweets

    def save_count(self, count):
        """
        Save current count to the database.
        """
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tweets SET tweets_retrieved=? WHERE id = 1", (count,))
        self.conn.commit()

    def get_status(self):
        """
        Returns the status of the stream (active or inactive).
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT status FROM tweets WHERE id = 1")
        result = cursor.fetchall()
        return str(result[0][0])
