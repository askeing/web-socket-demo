/**
 * Created by Askeing on 2017/2/21.
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
        html_log("Still has WebSocket object, readyState: " + ws.readyState);
        return;
    }

    var wsserver = document.getElementById("wsserver");
    var wsserver_address = wsserver.value;

    //ws = new WebSocket("ws://localhost:8888/");
    ws = new WebSocket(wsserver_address);

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
    html_log("Connected.");
}

function on_close(evt) {
    console.log("Disconnected.");
    html_log("Disconnected.");
}

function on_error(evt) {
    console.log("ERROR: " + evt.data);
    html_log("ERROR: " + evt.data);
}

function on_message(evt) {
    console.log("GET: " + evt.data);
    html_log("GET: " + evt.data);
}

function on_submit() {
    var input = document.getElementById("input");
    var message = input.value;
    if (message) {
        if (do_send(message)) {
            input.value = "";
            input.focus();
        }
    }
}

function do_send(message) {
    if (typeof ws !== 'undefined' && ws.readyState == WebSocket.OPEN) {
        console.log("SENT: " + message);
        html_log("SENT: " + message);
        ws.send(message);
        return true;
    } else {
        if (typeof ws !== 'undefined') {
            console.log("Cannot send. WebSocket readyState: " + ws.readyState);
            html_log("Cannot send. WebSocket readyState: " + ws.readyState);
        } else {
            console.log("No WebSocket object.");
            html_log("No WebSocket object.");
        }
        return false;
    }
}

function on_click_close_btn() {
    if (typeof ws !== 'undefined') {
        ws.close();
    }
}


function html_log(message) {
    var log = document.getElementById("log");
    var escaped = message.replace(/&/, "&amp;").replace(/</, "&lt;").replace(/>/, "&gt;").replace(/"/, "&quot;");
    log.innerHTML = log.innerHTML + "<br>" + escaped;
}