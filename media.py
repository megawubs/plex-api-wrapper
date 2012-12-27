class Media(object):
	"""Test class for media object"""
	def __init__(self, element, server):
		self.element = element
		self.server = server
		self.video = element.find('./Video')
		self.type = self.video.attrib['type']