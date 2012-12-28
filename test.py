from server import Server
from pprint import pprint

server = Server("192.168.1.201", 32400)
clients = server.clients

for c in clients:
	if "PyPlex" in c.name:
		client = c
if not client:
	print "PyPlex isn't found"

teststr = "/library/metadata/6308/"
media = server.getMedia(teststr)
# print media.transcodeURL
# print media.transcodeURL
# if media:
	# print "playing %s type is %s" % (media.title, media.type)
client.playVideo(media)
