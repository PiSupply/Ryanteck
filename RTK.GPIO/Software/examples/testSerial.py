# testSerial.py  22/04/2014  D.J.Whale
#
# Test that serial or simpleserial works.

import os
import time

try:
  import serial # pyserial
except ImportError:
  print("pyserial not installed, falling back to simpleserial")
  import simpleserial as serial

# linux FTDI
SERIAL_PORT = "/dev/ttyUSB0"
  
# windows
#SERIAL_PORT = "COM4"

# linux Arduino (CDC)
#SERIAL_PORT = "/dev/ttyACM0"

# mac
#SERIAL_PORT = "/dev/cua0"


def main():

  mode = int(raw_input("1:send 2:receive"))

  if mode == 1:
    i=0
    while True:
      print("sending...")
      s.write("hello world " + str(i) + "\r\n")
      print("sent " + str(i))
      time.sleep(0.5)
      i += 1
  else:
    while True:
      print("receiving...")
      m = s.read()
      print("received:" + m)

try:
  s = serial.Serial(SERIAL_PORT)
  s.open()
  main()

finally:
  print("closing...")
  s.close()
  print("closed")
  
# END
