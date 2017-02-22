/**
 * Created by Askeing on 2017/2/22.
 */

var ws;

function init_ws() {
    if (typeof ws !== 'undefined' && ws.readyState <= 1) {
        /*
         * readyStat
         * 0 CONNECTING
         * 1 OPEN
         * 2 CLOSING
         * 3 CLOSED
         * */
        console.log("Still has WebSocket object, readyState: " + ws.readyState);
        return;
    }

    ws = new WebSocket("ws://localhost:8888/");

    ws.onopen = function (evt) {
        on_open(evt);
    };

    ws.onclose = function (evt) {
        on_close(evt);
    };

    ws.onerror = function (evt) {
        on_error(evt);
    };

    ws.onmessage = function (evt) {
        on_message(evt);
    };
}


function on_open(evt) {
    console.log("Connected.");

    // Send message to server after connected.
    ws.send("Hello World");
}

function on_close(evt) {
    console.log("Disconnected.");
}

function on_error(evt) {
    console.log("ERROR: " + evt.data);
}

function on_message(evt) {
    console.log("GET: " + evt.data);

    // post received message to Add-on script
    self.postMessage(evt.data);
}

init_ws();
