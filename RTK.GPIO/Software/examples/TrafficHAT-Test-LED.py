#TrafficHAT KS Demo
from time import sleep
t = 0.2
import RTk.GPIO as GPIO

outputs = [22,23,24,5]
BUTT = 25

GPIO.setmode(GPIO.BCM)
sleep(t)
GPIO.setup(outputs, GPIO.OUT)
sleep(t)

GPIO.setup(BUTT,GPIO.IN)
sleep(t)

try:
	while True:
		GPIO.output(22, True)
		sleep(t)
		GPIO.output(23, True)
		sleep(t)
		GPIO.output(24, True)
		sleep(2)
		GPIO.output(22, False)
		sleep(t)
		GPIO.output(23, False)
		sleep(t)
		GPIO.output(24, False)
		sleep(2)


finally:
	GPIO.cleanup()
