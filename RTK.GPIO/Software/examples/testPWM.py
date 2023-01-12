#!/bin/env python
import RTk.GPIO as GPIO

PWMPIN = 11
FREQUENCY = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPIN, GPIO.OUT)
pwm = GPIO.PWM(PWMPIN, FREQUENCY)

for i in range(181):
	pwm.start(servoCalc(i))

GPIO.cleanup()
