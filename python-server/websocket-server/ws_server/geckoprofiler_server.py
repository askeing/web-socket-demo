import thread
import logging
import tempfile
from websocket_server import WebsocketServer

tmp_dir = tempfile.mkdtemp(prefix='geckoprofile-')
ws_server = WebsocketServer(8888, host='127.0.0.1')


def kill_server(server_handler):
    server_handler.IS_ONLINE = False
    server_handler.shutdown()


def on_new_client(client, server):
    print('Client {} Joined.'.format(client['id']))


def on_client_left(client, server):
    print('Client {} Left.'.format(client['id']))


def on_message(client, server, message):
    print('Msg from Client {}: {}'.format(client['id'], message))

    # magic string for shutdown server :-)
    if message.startswith('close-server'):
        print('Stopping Server ...')
        thread.start_new_thread(kill_server, (ws_server,))
        print('Server stopped!')


ws_server.set_fn_new_client(on_new_client)
ws_server.set_fn_client_left(on_client_left)
ws_server.set_fn_message_received(on_message)

thread.start_new_thread(ws_server.run_forever, ())
ws_server.IS_ONLINE = True

while ws_server.IS_ONLINE:
    import time
    print('Trying to do something ...')
    time.sleep(30)

    print('Starting get profile ...')

    print('Save to ' + tmp_dir)
    ws_server.send_message_to_all(tmp_dir)
    time.sleep(10)

print('Done.')
