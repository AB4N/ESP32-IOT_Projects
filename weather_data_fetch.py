import network
import time
import urequests
import json

#Connecting to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("#####" , "######")
#Loop so the program does not crash
while not wlan.isconnected():
    print("Connecting...")
    time.sleep(1)
    
print("Connected! IP Address: ",wlan.ifconfig()[0])

#GET request 
response = urequests.get("http://api.open-meteo.com/v1/forecast?latitude=49.44&longitude=11.86&current_weather=true")

# print(response.text)

#Parses JSON respone into a python dictionary
data= json.loads(response.text)
response.close()

#Saving data from dictionaries in 'data' to variables
temperature = data["current_weather"]["temperature"]
windspeed = data["current_weather"]["windspeed"]
weathercode = data["current_weather"]["weathercode"]
latitude = data["latitude"]

#Output
print("Temperature:", temperature, "C")
print("Wind speed:", windspeed, "km/h")
print("code:",weathercode)

print("lat", latitude)
