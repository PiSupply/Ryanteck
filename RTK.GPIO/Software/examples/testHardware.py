# testHardware.py  08/04/2014  D.J.Whale
#
# Flash LEDs and read switches
# Designed to test the Raspberry Pi and Arduino hardware.
# Uses same pin numbering for LEDs/BUTTONs as all other test programs


import time
FLASH_TIME = 1.0

#for Raspberry Pi
#import RPI.GPIO as GPIO
#BUTTON_GPIO  = [4, 14, 23, 24]
#using 7-seg
#LED_GPIO     = [10, 22, 25, 8, 7, 9, 11, 15]

# for arduino
import RTk.GPIO as GPIO
# using 7-seg and 4 buttons
BUTTON_GPIO  = [4, 5, 2, 3]
LED_GPIO     = [7, 6, 14, 16, 10, 8, 9, 15]

# using 4 buttons and 10 LEDs wired left-to-right
# wiring is such that it is physically left-to-right on the ProMicro
#BUTTON_GPIO   = [10, 16, 14, 15]
#LED_GPIO      = [9, 8, 7, 6, 5, 4, 3, 2, 0, 1]


BUTTON_FIRST      = BUTTON_GPIO[0]
BUTTON_LEFT       = BUTTON_GPIO[1]
BUTTON_RIGHT      = BUTTON_GPIO[2]
BUTTON_LAST       = BUTTON_GPIO[3]


def setup():
  GPIO.setmode(GPIO.BCM)
  for l in LED_GPIO:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l, False)

  for b in BUTTON_GPIO:
    GPIO.setup(b, GPIO.IN)


def loop():
  old_first  = False
  old_left   = False
  old_right  = False
  old_last   = False
  index = 0

  while True:
    # POLL BUTTONS
    # remember they are inverted
    first  = not GPIO.input(BUTTON_FIRST)
    left   = not GPIO.input(BUTTON_LEFT)
    right  = not GPIO.input(BUTTON_RIGHT)
    last   = not GPIO.input(BUTTON_LAST)

    # REPORT ANY CHANGED BUTTONS
    if first != old_first:
      print("FIRST=" + str(first))
      old_first = first
    if left != old_left:
      print("LEFT=" + str(left))
      old_left = left
    if right != old_right:
      print("RIGHT=" + str(right))
      old_right = right
    if last != old_last:
      print("LAST=" + str(last))
      old_last = last


    # PROCESS HELD BUTTONS IN PRIORITY ORDER
    if first:
      index = 0

    elif last:
      index = len(LED_GPIO)-1

    elif left:
      if index > 0:
        index -= 1

    elif right:
      if index < len(LED_GPIO)-1:
        index += 1


    # FLASH PRESENTLY SELECTED LED
    GPIO.output(LED_GPIO[index], True)
    time.sleep(FLASH_TIME/2)
    GPIO.output(LED_GPIO[index], False)
    time.sleep(FLASH_TIME/2)


# MAIN PROGRAM
try:
  setup()
  loop()

finally:
  GPIO.cleanup()

# END
