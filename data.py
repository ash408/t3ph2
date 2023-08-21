
import sys
import pymongo

from pymongo import MongoClient

class DB():
	'''
	Database handler, using pymongo

	Attributes
	==========
	client : MongoClient
		A MongoDB client connection

	Methods
	=======
	connect_client(parameters)
		Attempt to connect to MongoDB

		returns MongoClient object
	'''

	def __init__(self):
		self.client = self.connect_client();

	def connect_client(self):
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
