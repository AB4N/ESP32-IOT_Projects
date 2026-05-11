from machine import Pin
import time

led = Pin(2, Pin.OUT)
speed  = 0.1

while True:
    led.value(1)
    time.sleep(speed)
    led.value(0)
    time.sleep(speed)

# to make it blink a specific amount of times
# for i in range(10):
#     led.value(1)
#     time.sleep(speed)
#     led.value(0)
#     time.sleep(speed)
#     
# print("done blinking")