# seg7.py  02/05/2014  D.J.Whale
#
# This is a driver module, to drive the LEDs of a 7-segment LED display.
#
# A 7-segment LED display actually has 8 LEDs in a single package,
# each LED drives one segment of the display, and there is a spare
# LED that drives the decimal point (DP)
#
# 7-segment displays are very common and used in a lot of products.
# By setting different LEDs on and off you can write many patterns
# to the display. It is possible to write all of the numeric digits,
# most (but not all) of the alphabet, and a few other symbols.
#
# If you can write a program to turn a single LED on and off, then
# it is quite simple to write a program that turns 8 LEDs on and off.
# If you can do that, then it is a small step to driving a 7-segment
# LED display.
#
# This module is provided to save you some time in driving the display,
# and it provides some useful helper functions to make it easier to
# add new patterns supported by the driver. All this really does is
# to make your main program much simpler and shorter. But you will
# see that there is not really any magic in driving such a simple
# display.

#===== PATTERN TABLES ==================================================
#
# A 7-segment display looks like this:
#
#   AAAA
#  F    B
#  F    B
#   GGGG
#  E    C
#  E    C
#   DDDD  DP
#

# This module uses a table-driven (data-driven) method of specifying
# all of the different supported patterns. It would be possible to
# just use a function with lots of 'if' statements and GPIO.output()
# calls for each pattern, but this soon gets very big and hard to
# manage. Most software engineers use this table-driven approach
# when writing a driver for a 7-segment display in their code, as it
# is easier to add new patterns.

# These constants are for convenience, and make the tables a little
# more human readable. Refer to the 7-segment diagram above to see
# which segment names are in which positions. These are indexes into
# a GPIO pin list, which is then used to turn the appropriate GPIO
# pins on and off.

A  = 0
B  = 1
C  = 2
D  = 3
E  = 4
F  = 5
G  = 6
DP = 7


# The pattern table is actually a map of lists. A map is a type of
# table that maps keys to values, in this case it maps a "0" to
# a list of segments that need to be turned on to draw a "0" on the
# 7-segment display.
#
# Python provides easy ways of accessing maps and lists. You can
# find the element in the map that matches "0" by just asking
# for patterns["0"] - the key "0" is looked up in the map, and
# if it exists, the value [A, B, C, D, E, F] is returned.
# If a key does not exist in a map, Python will raise an exception
# called KeyError.
#
# The list of segments is just that, it is a Python list.
# Because earler on in this module we have defined constants for
# the segment letters, this makes this table really easy to read by
# humans, but it is also very efficient for the Python program
# to walk through the table and get out the list of segments
# required to draw a pattern on the 7-segment display.
#
# You can add your own patterns to this table to extend it if you
# like. It is recommended you use characters like "A" and "B" for
# those characters, but you can use any name you like for other
# symbols. You can see that we have used the names "up" and "down"
# to represent symbols for up and down arrows.

patterns = {
  "0":     [A, B, C, D, E, F],
  "1":     [B, C],
  "2":     [A, B, D, E, G],
  "3":     [A, B, C, D, G],
  "4":     [B, C, F, G],
  "5":     [A, C, D, F, G],
  "6":     [A, C, D, E, F, G],
  "7":     [A, B, C],
  "8":     [A, B, C, D, E, F, G],
  "9":     [A, B, C, D, F, G],
  "up":    [A, B, F],
  "down":  [C, D, E],
  "error": [A, D, G],
  " "    : []
}

# These are global variables.
# We don't want to have a direct reference to the GPIO module inside
# this module, as it is possible that the application program is
# using a different module depending on which hardware it is running
# on. So in here, GPIO is actually a variable that later on is
# set to reference the GPIO module provided by the application
# program when it calls the setup() function.
#
# 'pins' is a global variable, it is a list. When the application
# program calls the setup() function it provides 8 pin numbers
# that can be used for each of the 8 segments of the display.
# These pin numbers are stored, in-order, inside the pins[] list.
# This is so that this module can be reused inside different products
# that have different hardware pin usage, without the need to
# customise this module. The application program "owns" the
# pin numbers that it uses for the display.

GPIO = None
pins = None
on = True

def setup(app_gpio, app_pins, on_state):
  """Configure the GPIO driver and 8 used pins for display"""
  global GPIO, pins, on
  GPIO = app_gpio
  pins = app_pins
  on = on_state
  for p in pins:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, False)
  
def clear():
  """clear the display, turn all segments off"""
  writeLEDs([])
  
def write(patternName):
  """look up the pattern name in the table, and display it"""
  try:
    leds = patterns[patternName]
  except KeyError:
    leds = patterns["error"]
  writeLEDs(leds)
  
def setdp(state):
  """turn decimal point on or off"""
  if type(state) == bool and state == True or type(state)==int and state!=0:
    GPIO.output(pins[DP], on)
  else:
    GPIO.output(pins[DP], not on)
  
def writeLEDs(leds):
  """Take a list of LEDs that need turning on, and turn only those on"""
  for seg in [A,B,C,D,E,F,G,DP]:
    if seg in leds:
      GPIO.output(pins[seg], on)
    else:
      GPIO.output(pins[seg], not on)

def writePattern(pattern):
  """Take a list of flags and write that to the LEDs
     Unlisted LEDs are unchanged. A boolean or a number can be used.
  """
  l = len(pattern)
  if l>8:
    l=8
  for seg in range(A, l):
    state = not on
    p = pattern[seg]
    if type(p) == bool:
      if p==True:
        state = on
    elif type(p) == int:
      if p!=0:
        state = on
    else:
      if p!=None:
        state = on
    GPIO.output(pins[seg], state)
      
# A useful helper, to do this with default pinning:
#   import seg7 as d
#   d.configure()
#   d.clear()
#   d.write("8")
#   d.setdp(True)
   
def configure(ON=True):
  try:
    print("Trying Raspberry Pi")
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    setup(GPIO, [10, 11, 14, 15, 17, 18, 22, 23], ON)
    print("Raspberry Pi OK")
      
  except ImportError:
    print("Trying Arduino")
    import anyio.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    setup(GPIO, [7, 6, 14, 16, 10, 8, 9, 15], ON)
    print("Arduino OK")


# test harness

if __name__ == "__main__":
  import time
  configure()
    
  clear()
  for v in patterns:
    print("trying:" + v)
    write(v)
    time.sleep(0.5)
    
# END
