# testButton.py  05/05/2014  D.J.Whale
#
# Test that the button works

import time
TIME = 0.1

# Raspberry Pi
#import RPI.GPIO as GPIO
#BUTTON = 4

# Arduino
import RTk.GPIO as GPIO
BUTTON = 24

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BUTTON, GPIO.IN)

def loop():
  while True:
    time.sleep(TIME)
    b = GPIO.input(BUTTON)
    if not b:
      print("pressed")
    else:
      print("released")

try:
  setup()
  loop()
finally:
  GPIO.cleanup()

# END
