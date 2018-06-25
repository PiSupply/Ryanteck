# testAnalog.py - 06/06/2014 D.J.Whale
# Modified by Ryan Walmsley
# Analog Input

from time import sleep
from subprocess import call

t = 0


# RTk.GPIO
import RTk.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
while True:
    value = GPIO.analogIn(8)
    percentage = (value*100)
    percentage = int(round(percentage))
    print(percentage)
    call(["amixer", "-D", "pulse", "sset", "Master", str(percentage)+"%"])
    sleep(t)


# END
