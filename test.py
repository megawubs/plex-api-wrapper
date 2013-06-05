from server import Server
from pprint import pprint
import os, urllib2, sys


def download(url, file_name):
	downloadPath = os.path.dirname(__file__)
	#the filename
	# file_name = url.split('/')[-1]
	#complete path to the file that will be downloaded shortly
	file_path = os.path.join(downloadPath, file_name)
	#just for development a check to download or not
	#open the url
	u         = urllib2.urlopen(url)
	#open a binary file
	f         = open(file_path, 'wb')
	#get some info
	meta      = u.info()
	#get the file size
	file_size = int(meta.getheaders("Content-Length")[0])
	#the download bar
	file_size_dl = 0
	block_sz     = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		f.write(buffer)

	f.close()

query = sys.argv[1]
# pprint(query)
server = Server("192.168.1.119", 32400)
# # teststr = "/library/metadata/1/"
result = server.library.findShows(query)
for media in result:
	print media.title
	print query
	if media.title == query:
		print 'downloading'
		downloadLink = "http://%s:%d%s" % (server.address, server.port, media.theme)
		title = media.title.replace(' ', '-')
		download(downloadLink, title+'.mp3')
# media = server.getMedia(teststr)
# downloadLink = "http://%s:%d%s" % (server.address, server.port, media.theme)
# # print downloadLink
# 
# 
# # pprint(media.getAllEpisodes())