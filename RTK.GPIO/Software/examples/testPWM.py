# testLED.py - 06/06/2014 D.J.Whale
# Modified by Ryan Walmsley
# Test flashing an LED

from time import sleep
t = 0.01


# RTk.GPIO
import RTk.GPIO as GPIO

P = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(P, GPIO.OUT)


while True:
	GPIO.output(P, True)
	sleep(t)
	GPIO.output(P, False)
	sleep(t)

# END
