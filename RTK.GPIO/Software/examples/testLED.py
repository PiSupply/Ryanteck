#!/bin/env python
import RTk.GPIO as GPIO
from time import sleep

LED = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

for x in range(6):
	GPIO.output(LED ,GPIO.HIGH)
	sleep(2)
	GPIO.output(LED ,GPIO.LOW)
	sleep(2)

GPIO.cleanup()
