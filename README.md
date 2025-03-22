# WiFi QR Code Generator

## Overview
This simple Python script generates a QR code for a WiFi network, making it easier to connect without manually entering the password. Just scan the QR code with your phone, and you're connected!

## Why This Exists
I created this tool to simplify WiFi connections without compromising security by using easy-to-guess passwords. While similar tools exist online, I wanted a simple, offline solution that works without the need to trust online websites (yes I am paranoid:)).

## Requirements
- Required libraries:
  - `qrcode`
- Optional libraries:
  - `colorama`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Wh0am123/WiFi-QR-Generator.git
   cd WiFi-QR-Generator
   ```
2. Install dependencies:
   ```bash
   pip install qrcode colorama
   ```

## Usage
Run the script and follow the prompts:
```bash
python WiFi_QR.py
```
Enter your WiFi name (SSID) and password when prompted. The script will generate a QR code and save it as an image file named `<SSID>_QR.png` in the same directory.

## Example
```
Enter Wifi Name:
MyHomeWiFiSSID
Enter Wifi's Password:
2JdV'A3swfInh]uAI#RZEx;;}dIAKysW
```
This will generate a file `MyHomeWiFi_QR.png`, which can be scanned using a phone's camera to connect instantly.
