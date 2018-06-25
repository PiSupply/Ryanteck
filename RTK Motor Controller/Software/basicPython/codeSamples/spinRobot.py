#RTK-000-001 Tester
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley,

#We want to be able to sleep but don't need all of time & space, just import sleep
from time import sleep
#We alos need to use RPi.GPIO but we want to use it as GPIO
import RPi.GPIO as GPIO

#Setup the Pi to use BCM mode
GPIO.setmode(GPIO.BCM)
#Output the pins 17,18,22,23

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#All Pins setup!
#Now lets make the robot spin for 1 second left
GPIO.output(17,1)
GPIO.output(23,1)
sleep(1)
GPIO.output(17,0)
GPIO.output(23,0)
	
#Now lets make it spin right for 1 second
GPIO.output(18,1)
GPIO.output(22,1)
sleep(1)
GPIO.output(18,0)
GPIO.output(22,0)

#Now lets clean up the GPIO code
GPIO.cleanup()
