import re
import sys

def extract_rtsp(file_path):
    print(f"[*] Analyzing {file_path} for RTSP streams...")
    with open(file_path, 'rb') as f:
        data = f.read().decode('latin-1', errors='ignore')
        # Regex to find rtsp:// URLs
        urls = re.findall(r'rtsp://[a-zA-Z0-9\.\:/_]+', data)
        for url in set(urls):
            print(f"[!] Found Stream URL: {url}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_rtsp(sys.argv[1])
    else:
        print("Usage: python3 pcap_parser.py your_capture.pcap")
