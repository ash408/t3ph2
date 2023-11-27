
import json
import uuid


class Entity:

	def __init__(self, uid=None, attributes=None, labels=None, resources=None):
		
		if (uid is None):
			uid = str(uuid.uuid4())
		
		self.uid = uid
		self.attributes = attributes
		self.labels = labels
		self.resources = resources


	def generate_json(self):
		json_data = {}

		json_data['uid'] = self.uid
		json_data['attributes'] = self.attributes
		json_data['labels'] = self.labels
		json_data['resources'] = self.resources

		return json.dumps(json_data)
