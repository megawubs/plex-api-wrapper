class Info(object):
	"""Get media info"""
	def __init__(self, media):
		self.str = '<Info Object Type: %s, Title: %s>'

		element = media.element
		mediaElement = element.find('.Media')

		self.media = media
		self.info = {}
		self.info['key'] = element.attrib['key']
		self.info['type'] = media.type
		self.info['title'] = element.attrib['title']
		self.info['summary'] = element.attrib['summary']
		if 'index' in element.attrib:
			self.info['index'] = int(element.attrib['index'])
		self.info['duration'] = int(mediaElement.attrib['duration'])
		self.info['viewed'] = ('viewCount' in element.attrib) and (element.attrib['viewCount'] == '1')
		self.info['offset'] = int(element.attrib['viewOffset']) if 'viewOffset' in element.attrib else 0
		self.info['file'] = element.find('.Media/Part').attrib['file']
		
		self.info['video_codec'] = mediaElement.attrib['videoCodec']
		self.info['audio_codec'] = mediaElement.attrib['audioCodec']
		self.info['width'] = mediaElement.attrib['width']
		self.info['height'] = mediaElement.attrib['height']
		if 'year' in element.attrib:
			self.year = int(element.attrib['year'])
		else:
			self.year = 'unknown'
	 	# self.scrobbleURL = "scrobble?key=" + str(self.mediaKey) + "&identifier=com.plexapp.plugins.library"
   #      self.updateURL =  'progress?key=' + str(self.mediaKey) + '&identifier=com.plexapp.plugins.library&time=%s&state=playing' 
	
	def __str__(self):
		return self.str % (self.info['type'], self.info['title'])

	def __repr__(self):
		return self.str % (self.info['type'], self.info['title'])