
import uuid


class entity:

	def __init__(self, uid=None, attributes=None, labels=None, resources=None):
		
		if (uid is None):
			uid = str(uuid.uuid4())
		
		self.uid = uid
		self.attributes = attributes
		self.labels = labels
		self.resources = resources


