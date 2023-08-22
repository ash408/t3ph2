
import sys
import pymongo

from pymongo import MongoClient


class DB():
	'''
	Database handler, using pymongo.

	Attributes
	==========
	client : MongoClient
		A MongoDB client connection

	Methods
	=======
	connect_client(parameters)
		Attempt to connect to MongoDB

		returns MongoClient object or false

	Schema
	======
	Each database corresponds to owner's UUID, holding multiple games.
	Each game is assigned to one table, with necessary objects held
	inside.
	'''

	def __init__(self):
		self.connect_client();

	def connect_client(self):
		'''
		Attempt to connect to MongoClient, sets client attribute.

			Returns:
				client (MongoClient) : a MongoDB connection, or False
									if unable to connect
		'''

		try:
			self.client = MongoClient(serverSelectionTimeoutMS = 2000)
			return client
		
		except:
			self.client = False
			return False
