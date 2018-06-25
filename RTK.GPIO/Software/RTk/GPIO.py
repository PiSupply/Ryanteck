# anyio/arduino/GPIO.py  21/04/2014  D.J.Whale
#
# An ardunio (serial) based GPIO link

# CONFIGURATION ========================================================

DEBUG = False
# There was the option to use the serial library pre-installed. This has changed so that we know the python lib in use is the one distributed with the rtk library.
#If you wish to use the built in one instead change the import rtkserial to import serial which is below (Approx line 38)

MIN_PIN = 0
MAX_PIN = 27

IN      = 0
OUT     = 1
BCM     = 0
BOARD   = 1
HIGH    = 1
LOW     = 0

PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22
VERSION = "RTk.GPIO 0.1A"
RPI_REVISION = 3
RPI_INFO = {'P1_REVISION': 3, 'RAM': 'Unknown', 'REVISION': '90092', 'TYPE': 'Unknown','PROCESSOR': 'Unknown','MANUFACTURER':'Unknown'}


# OS INTERFACE =========================================================

from RTk import protocol
from RTk import adaptors


#from os import sys, path
#thisdir = path.dirname(path.abspath(__file__))
#sys.path.append(thisdir)

#import rtkserial as serial

#Temporarily changing back to normal serial

from RTk import rtkserial

instance = protocol.GPIOClient(adaptors.SerialAdaptor(rtkserial.s), DEBUG)

def setwarnings(option):
  instance.setwarnings(option)

def setmode(mode):
  instance.setmode(mode)

def setup(channel, mode,pull_up_down=None,initial=0):
  if type(channel) is list:
    for c in channel:
      instance.setup(c, mode,pull_up_down,initial)
  else:
    instance.setup(channel, mode,pull_up_down,initial)

def input(channel):
  return instance.input(channel)

def output(channel, value):
  instance.output(channel, value)

def cleanup():
  instance.cleanup()


# END
