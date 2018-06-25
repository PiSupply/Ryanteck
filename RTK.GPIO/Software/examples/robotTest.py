from RTk import GPIO
from time import sleep

#Setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

i = 0
try:
	while (i<10):
		print("Forward")
		GPIO.output(17,1)
		sleep(1)
		GPIO.output(17,0)
		print("Backward")
		GPIO.output(18,1)
		sleep(1)
		GPIO.output(18,0)
		i=i+1
finally:
  GPIO.cleanup()
