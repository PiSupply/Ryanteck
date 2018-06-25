# testSeg7.py - Test a 7-segment display

import anyio.seg7 as display
import time

# Use this for Raspberry Pi
#import RPi.GPIO as GPIO
#LED_PINS = [10,22,25,8,7,9,11,15]

# Use this for Arduino
import RTk.GPIO as GPIO
LED_PINS = [7,6,14,16,10,8,9,15]

GPIO.setmode(GPIO.BCM)

ON = False # common-anode. Set to True for a common cathode display

display.setup(GPIO, LED_PINS, ON)

try:
  while True:
    for d in range(10):
      display.write(str(d))
      time.sleep(0.5)
finally:
  GPIO.cleanup()

# END
