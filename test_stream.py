import cv2
import sys

def start_stream(rtsp_url):
    print(f"[*] Connecting to: {rtsp_url}")
    print("[!] Press 'q' to quit.")

    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("[!] Error: Could not open video stream. Check your URL/Credentials.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[!] Lost frame. Attempting to reconnect...")
            cap.open(rtsp_url)
            continue

        # Display the resulting frame
        cv2.imshow('Z-IOT Camera Live Feed', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_stream(sys.argv[1])
    else:
        print("Usage: python3 test_stream.py rtsp://admin:password@192.168.1.1:554/live/ch0")
