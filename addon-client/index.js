var self = require("sdk/self");
var pageWorkers = require("sdk/page-worker");

// Create a page worker that loads Wikipedia:
p_worker = pageWorkers.Page({
    contentScriptFile: self.data.url("wsclient.js"),
    contentURL: self.data.url("wsclient.html"),
    onMessage: function(message) {
        console.log("Add-on Script Get: " + message);
        foo();
    }
});


function foo() {
    console.log("RUN FOO.")
}
