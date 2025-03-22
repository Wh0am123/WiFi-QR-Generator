import qrcode
try:
	from colorama import Fore, Style, init

	# Initialize colorama
	init(autoreset=True)

	# ASCII art for 'whoami03'
	banner = r"""
	          _                           _  ___ _____ 
	__      _| |__   ___   __ _ _ __ ___ (_)/ _ \___ /                                                                            
	\ \ /\ / / '_ \ / _ \ / _` | '_ ` _ \| | | | ||_ \                                                                            
	 \ V  V /| | | | (_) | (_| | | | | | | | |_| |__) |                                                                           
	  \_/\_/ |_| |_|\___/ \__,_|_| |_| |_|_|\___/____/                                                                            
	                                                                                                                              
	           
	"""

	# Print the banner with color
	print(Fore.CYAN + banner + Style.RESET_ALL)
except:
	print(" Couldn't print ASCII art, moving on\n")
	
ssid = input("Enter Wifi Name:\n")
password = input("Enter Wifi's Password:\n")
wifi_string = f"WIFI:S:{ssid};T:WPA;P:{password};H:false;;"
#print(wifi_string) #for debugging

qr = qrcode.make(wifi_string)

# Save the QR code
qr_path = f"{ssid}_QR.png"

qr.save(qr_path)

print(f"QR for network {ssid} is saved in {qr_path}")
