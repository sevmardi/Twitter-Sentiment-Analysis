import unittest

from tweepy import API, OAuthHandler


class TweepyAuthTests(unittest.TestCase):
	"""docstring for TweepyAuthTests"""
	def __init__(self, arg):
		super(TweepyAuthTests, self).__init__()
		self.arg = arg

	def testoauth(self):
		auth = OAuthHandler(consumer_key, consumer_secret, callback)
		
		#test getting access token	
		auth_url = auth.get_authorization_url()
		print "Please authorize: " + auth_url
		verifier = raw_input('PIN: ').strip()
		self.assert_(len(verifier) > 0)
		access_token = auth.get_access_token(verifier)
		self.assert_(access_token is not None)

		# build api object test using oauth 
		api = API(auth)
		s = api.update_status('test %i' % random.randint(0, 1000))
		api.destroy_status(s, id)
		