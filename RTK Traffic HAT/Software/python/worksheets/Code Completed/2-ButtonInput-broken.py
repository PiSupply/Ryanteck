#TrafficHAT - Blink LED
#By Your Name Here

import RPi.GPIO as IO #This imports the RPi.GPIO Library as IO

from time import sleep # This imports only the sleep function from time.

#Next we need to setup the Raspberry Pi's GPIO Pins
IO.setmode(IO.BCM) #This sets the Pi to BCM / GPIO Numbering

#Next we want to setup the Green LED as an output
green = 22
button = 25

IO.setup(green,IO.OUT) # This sets the green LED to be an output.
IO.setup(button,IO.IN,pull_up_down=IO.PUD_UP)

IO.setup(green,IO.OUT) # This sets the green LED to be an output.

#By using the try loop we can then add an except at the end
#to figure out what tbe bugs are in our code.
try:
    #In python we indent one for code to be inside a block.
    #All code with 1 indent will be inside the try block
    #To do an indent you can either press space 4 times
    #Or press the Tab button once which will insert 4 spaces.
    #You can do either but you can only do one or the other
    #in the same program.
    #Geany also usually does this automatically for you

    while True:
        #Code in the while loop will repeat forever.
        #As you can see we're using 2 indents for this.

        #To begin we're going to turn the LED On
        #The RPi.GPIO Library accepts a binary input to decide if it is on or off.
        #Binary is either 1 for On / True or 0 for Off / False

        #To control an output we do the following
        IO.output(green,1)

        while(IO.input(25)):
            pass

        IO.output(green,0)

except KeyboardInterrupt:
    #While this isn't actually an error python sees this as an exception.
    #This code is ran when we quit the program using the keyboard.

    #We want to clean up all of the GPIO Pins by running
    IO.cleanup()

except:
    #If there are any other errors we want to know what they are.
    print "Error:", sys.exc_info()[0]
    raise
