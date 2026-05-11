import network
import time

SSID = "Markhor"
PASSWORD = "Kuchbhi@09"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("connecting lol...")
    time.sleep(0.5)
    
print("COnnected! IP:", wlan.ifconfig()[0])