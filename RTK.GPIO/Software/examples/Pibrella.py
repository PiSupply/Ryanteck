#Pibrella Demo
from time import sleep
t = 0.2
import RTk.GPIO as GPIO

RED = 27
YEL = 17
GRN = 4
BUZZ =18
OUT1 =22
OUT2 =23
OUT3 =24
OUT4 =25

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YEL, GPIO.OUT)
GPIO.setup(GRN, GPIO.OUT)
GPIO.setup(OUT1,GPIO.OUT)
GPIO.setup(OUT2,GPIO.OUT)
GPIO.setup(OUT3,GPIO.OUT)
GPIO.setup(OUT4,GPIO.OUT)


try:
	while True:
		GPIO.output(RED, True)
		sleep(t)
		GPIO.output(YEL, True)
		sleep(t)
		GPIO.output(GRN, True)
		sleep(t)
		GPIO.output(OUT1, True)
		sleep(t)
		GPIO.output(OUT2, True)
		sleep(t)
		GPIO.output(OUT3, True)
		sleep(t)
		GPIO.output(OUT4, True)
		sleep(t)
		GPIO.output(RED, False)
		sleep(t)
		GPIO.output(YEL, False)
		sleep(t)
		GPIO.output(GRN, False)
		sleep(t)
		GPIO.output(OUT1, False)
		sleep(t)
		GPIO.output(OUT2, False)
		sleep(t)
		GPIO.output(OUT3, False)
		sleep(t)
		GPIO.output(OUT4, False)
		sleep(t)


finally:
	GPIO.cleanup()
