import os
import json
from websocket import create_connection


ws = create_connection('ws://localhost:8888/py')

file_path = os.path.abspath('.')
data = {
    'command': 'getfile',
    'data': file_path
}
print "Sending {} ...."
ws.send(json.dumps(data))
print "Sent"

print "Receiving..."
result = ws.recv()
print "Received '%s'" % result

data = {
    'command': 'getlink',
    'data': ''
}
print "Sending {} ...."
ws.send(json.dumps(data))
print "Sent"

print "Receiving..."
result = ws.recv()
print "Received '%s'" % result

ws.send("close-server")
ws.close()
