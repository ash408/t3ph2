
import sys
import pymongo

from pymongo import MongoClient

class DB():
	'''
	Database handler, using pymongo

	Attributes
	==========
	variable : type
		description

	Methods
	=======
	TODO(parameters)
		Description
		returns ...
	'''

	def __init__(self):
		self.client = self.connect();

	def connectClient(self):
		'''
		Attempt to connect to MongoClient, exit if unable

			Returns:
				client (MongoClient) : a MongoDB connection
		'''

		try:
			client = MongoClient(serverSelectionTimeoutMS = 2000)
			return client
		
		except:
			print("Error: cannot connect to MongoDB")
			print("Exiting...")

			sys.exit()
