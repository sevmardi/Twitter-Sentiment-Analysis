#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import config.config as config


#Variables that contains the user credentials to access Twitter API
access_token = config.access_token
access_token_secret = config.access_token_secret
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

    def word_in_text(word, text) :
        word = word.lower()
        text = text.lower()
        match = re.search(regex, text)
        if match :
            return match.group()
        return ''

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture Data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['happiness', 'war', 'life'])
        