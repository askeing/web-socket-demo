from websocket import create_connection


ws = create_connection('ws://localhost:8888/', subprotocols=['echo-protocol',])

print "Sending 'Hello, Server. I am client.'...."
ws.send("Hello, Server. I am client.")
print "Sent"
print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()
