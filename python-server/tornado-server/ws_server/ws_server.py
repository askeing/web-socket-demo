import thread
from tornado import websocket, web, ioloop
import json


server = None
addon_clients = []
py_clients = []


def stop_server(server_handler):
    server_handler.stop()


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


class AddonSocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in addon_clients:
            print('[WebSocket] one Add-on client connected.')
            addon_clients.append(self)

    def on_close(self):
        if self in addon_clients:
            print('[WebSocket] one Add-on client disconnected.')
            addon_clients.remove(self)

    def on_message(self, message):
        input_data = json.loads(message)
        print('[WebSocket] AddonSocketHandler get: {}'.format(input_data))
        if 'command' in input_data and 'data' in input_data:
            for client in py_clients:
                client.write_message(input_data)


class PythonSocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in py_clients:
            print('[WebSocket] one Python client connected.')
            py_clients.append(self)

    def on_close(self):
        if self in py_clients:
            print('[WebSocket] one Python client disconnected.')
            py_clients.remove(self)

    def on_message(self, message):
        if message.lower().startswith('close-server'):
            print('[WebSocket] Stopping Server ...')
            for client in addon_clients:
                client.close()
            for client in py_clients:
                client.close()
            thread.start_new_thread(stop_server, (server,))
            print('[WebSocket] Server stopped!')
            return

        input_data = json.loads(message)
        print('[WebSocket] PythonSocketHandler get: {}'.format(input_data))
        if 'command' in input_data and 'data' in input_data:
            for client in addon_clients:
                client.write_message(input_data)

app = web.Application([
    (r'/addon', AddonSocketHandler),
    (r'/py', PythonSocketHandler),
])


if __name__ == '__main__':
    app.listen(8888)
    print('[WebSocket] Server is listening on port 8888 ...')
    server = ioloop.IOLoop.instance()
    server.start()
