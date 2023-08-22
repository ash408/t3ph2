
import unittest

from data import DB


class TestDB(unittest.TestCase):

	def test_connect_failure(self):
		'''
		Test to make sure DB handles a failed connection
		properly. Should return False boolean.
		'''
		
		#TODO

	def test_connect_success(self):
		'''
		Test to handle a successful connection. Should
		return MongoClient object.
		'''

		#TODO

if __name__ == '__main__':
	unittest.main()
