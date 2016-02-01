from datatime import datatime
from mock import patch, Mock 
import unittest

from tweepy import API

class TwitterTestCase(TestCase):
	"""docstring for TwitterTestCase"""
	def __init__(self, arg):
		super(TwitterTestCase, self).__init__()
		self.arg = arg
		
	def setUp(self):
			environ('TWITTER_CONSUMER_KEY') = 'fake'
			environ['TWITTER_CONSUMER_KEY'] = 'fake'
     	    environ['TWITTER_ACCESS_TOKEN'] = 'fake'
        	environ['TWITTER_CONSUMER_SECRET'] = 'fake'
       	    environ['TWITTER_ACCESS_SECRET'] = 'fake'

       	    self.mock_event = Mock(
       	    	title= "building an app",
       	    	where= "Name, Location"
       	    	when=datatime.now()
       	    	)