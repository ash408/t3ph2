
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
		Attempt to connect to MongoClient, sets client attribute to
		MongoClient object, or false if connection has failed.
		'''
		try:
			self.client = MongoClient(serverSelectionTimeoutMS = 2000)
		
		except:
			self.client = False
