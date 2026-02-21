import os
import re

def get_gateway():
    # Works on macOS/Linux
    stream = os.popen("route -n get default | grep gateway")
    output = stream.read()
    gateway = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output)
    return gateway.group(1) if gateway else "Not Found"

print(f"[*] Connected to Camera Hotspot. Camera IP detected at: {get_gateway()}")
