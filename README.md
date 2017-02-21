# Web Socket Demo

Python WebSocket Server, HTML WebSocket Client, Add-on WebSocket Client

## Server

Install Python server.

```bash
$ virtualenv .env-python
$ source .env-python/bin/activate
$ python server/setup.py develop
```

Running server.

```bash
$ python server/ws_server/echo_server.py
Listening on port 8888 for clients..
```

Pressing `Ctrl + C` for stopping server.

## HTML Client

Running HTTP server for HTML page.

```bash
$ python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Then launch browser and access `http://localhost:8000/html-client/`.

Pressing `Ctrl + C` for stopping HTTP server.
