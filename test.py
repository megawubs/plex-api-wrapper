from server import Server
from episode import Episode
from media import Media
from movie import Movie
from pprint import pprint

server = Server("192.168.1.201", 32400)
clients = server.clients

for c in clients:
	if "PyPlex" in c.name:
		client = c
if not client:
	print "PyPlex isn't found"

teststr = "/library/metadata/6240/"

result = Media(server.query(teststr), server)

if result.type == "episode":
	media = Episode(result.video, server)
elif result.type == "movie":
	media = Movie(result.video, server)
else:
	print "unknown type: %s" % result.type
	exit(0)

print "playing %s" % media.title
client.playVideo(media)
