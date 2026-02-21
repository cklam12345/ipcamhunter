#!/bin/bash

echo "--- IPCamHunter: Searching for Z-IOT OEM Cameras ---"

# Check if python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install it."
    exit
fi

# Run the hunter
python3 hunter.py

echo "----------------------------------------------------"
echo "Try connecting via: rtsp://[IP]:554/video1"
