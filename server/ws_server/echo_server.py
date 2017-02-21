import thread
from websocket_server import WebsocketServer


def on_new_client(client, server):
    print('Client {} Joined.'.format(client['id']))
    server.send_message_to_all('Dear all, new client {} has joined us.'.format(client['id']))


def on_client_left(client, server):
    print('Client {} Left.'.format(client['id']))
    server.send_message_to_all('Dear all, client {} has left us.'.format(client['id']))


def on_message(client, server, message):
    print('Msg from Client {}: {}'.format(client['id'], message))
    server.send_message(client, 'I got message from client {}: {}'.format(client['id'], message))
    # magic string for shutdown server :-)
    if message.startswith('close-server'):
        print('Server Bye Bye!!')
        thread.start_new_thread(kill_server, (ws_server,))
        print('Done.')


def kill_server(server_handler):
    server_handler.shutdown()


ws_server = WebsocketServer(8888, host='127.0.0.1')
ws_server.set_fn_new_client(on_new_client)
ws_server.set_fn_client_left(on_client_left)
ws_server.set_fn_message_received(on_message)
ws_server.run_forever()
