#TrafficHAT KS Demo
from time import sleep
t = 0.2
import RTk.GPIO as GPIO

gpios = [0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

GPIO.setmode(GPIO.BCM)

for cGPIO in gpios:
	print("Testing GPIO %s", cGPIO);
	GPIO.setup(cGPIO,GPIO.OUT)
	GPIO.output(cGPIO,1)
	input("Press enter to continue")
	GPIO.output(cGPIO,0)
