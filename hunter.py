import socket
import threading
from ipaddress import IPv4Network

# Change this to match your local network range
NETWORK = "192.168.1.0/24"
RTSP_PORT = 554

def check_ip(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((str(ip), RTSP_PORT))
    if result == 0:
        print(f"[!] Found Potential Camera: {ip}:{RTSP_PORT}")
    s.close()

def main():
    print(f"Scanning {NETWORK} for RTSP devices...")
    threads = []
    for ip in IPv4Network(NETWORK):
        t = threading.Thread(target=check_ip, args=(ip,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
