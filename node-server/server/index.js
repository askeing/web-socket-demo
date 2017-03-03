#!/usr/bin/env node

var WebSocketServer = require('websocket').server;
var http = require('http');

// Connected WebSocket clients
var clients = [];

var server = http.createServer(function(request, response) {
    response.writeHead(404);
    response.end();
});

server.listen(8888, function() {
    console.log('Server is listening on port 8888 ...');
});

wsServer = new WebSocketServer({
    httpServer: server,
    autoAcceptConnections: false
});

function originIsAllowed(origin) {
  console.log('Request origin: ' + origin);
  return true;
}

function wsOnMessage(message) {
    if (message.type === 'utf8') {
        console.log('Received Message: ' + message.utf8Data);
        this.sendUTF(message.utf8Data);
    }
    else if (message.type === 'binary') {
        console.log('Received ' + message.binaryData.length + ' bytes Binary Message');
        this.sendBytes(message.binaryData);
    }
}

function wsOnClose(reasonCode, description) {
    console.log((' Client ' + this.remoteAddress + ' disconnected.');
    // remove an item by value:
    clients.splice(clients.indexOf(this), 1);
}

function wsOnRequest(request) {
    if (!originIsAllowed(request.origin)) {
      request.reject();
      console.log('Reject origin ' + request.origin);
      return;
    }

    var connection = request.accept('echo-protocol', request.origin);
    clients.push(connection);
    console.log('Connection accepted.');

    connection.on('message', wsOnMessage);

    connection.on('close', wsOnClose);
}

wsServer.on('request', wsOnRequest);
