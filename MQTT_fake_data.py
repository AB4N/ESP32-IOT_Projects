import network
import time
#importing just MQTTClient from umqtt lib
from umqtt.simple import MQTTClient
import random


#Connecting to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Markhor" , "Kuchbhi@09")
#Loop so the program does not crash
while not wlan.isconnected():
    print("Connecting...")
    time.sleep(1)
    
print("Connected! IP Address: ",wlan.ifconfig()[0])

#Connect to MQTT broker
#MQTTClient("Unique client ID", "broker")
client = MQTTClient("esp32-amberg-01", "broker.hivemq.com")
client.connect()

#publishing message
#client.publish("topic", "message")//b means bytes
client.publish(b"dorm/energy/room1",b"hello from ESP32")
print("Message published!")

while True:
#simulating fake power reading
    fake_watts =  random.uniform(40,120)
    fake_voltage = 230.0

    #Package data as JSON string
    payload = f'{{"power": {fake_watts:.1f}, "voltage": {fake_voltage}}}'

    #publishing // .encode() converts string to bytes
    client.publish(b"dorm/energy/room1", payload.encode())
    print("Published:", payload)
    time.sleep(2)
