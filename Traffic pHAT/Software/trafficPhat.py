
# Demo program to use Traffic pHAT with GPIO Zero
#This demo program shows you how to use each LED, and turns each one on in sequence every second.
from gpiozero import TrafficLights
from time import sleep

traffic = TrafficLights(23, 24, 25)

while True:
    traffic.red.on()
    sleep(1)
    traffic.red.off()
    traffic.amber.on()
    sleep(1)
    traffic.amber.off()
    traffic.green.on()
    sleep(1)
    traffic.green.off()
