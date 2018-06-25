#First lets begin by importing two libraries that we require.
#We require the RPi.GPIO Library to access the GPIO Pins
#And we require sleep from time to be able to add a delay.
import RPi.GPIO as IO  #This line imports RPi.GPIO but sets it to IO meaning we can type in IO on every line instead of RPi.GPIO.
from time import sleep #This imports only the sleep function from the time library.

IO.setmode(IO.BCM) #This sets the RPi.GPIO Library to use the BCM/GPIO Numbering scheme which is used on the TrafficHAT PCB.

#Now we want to make a variable for each pin used.
RED = 24
YELLOW = 23
GREEN = 22
BUTTON = 25
BUZZER = 5

#Next we need to configure these pins
#The LEDs & Buzzer are all Outputs, this means we need to configure these all to be an output.
#---------------------------------------
#To do this we are going to add them all to an Array and iterate through the Array to set each one up
outputs = [RED, YELLOW, GREEN, BUZZER]

#Next we need to iterate through each one using an For loop
for(output in outputs):
    #This will then pass the number of the output to the variable output
    IO.setmode(output,IO.OUT)

#Finally we want to configure the button as an input. As there is only one button we only need to do this once.
#The button requires a Pull Up for it to work so requires this to be set using the code
# "pull_up_down=GPIO.PUD_UP"
IO.setmode(button,IO.IN,pull_up_down=GPIO.PUD_UP)

#We are now all setup!
#------------------Remember To Save Your Work--------------------

#Now we are going to perform the Traffic Light Sequence

try:
    while true:
        #Turn Green LED On
        #Wait until the button is pressed 
        #Turn Green LED Off
        #Turn Yellow LED On
        #Wait 1 second
        #Turn Yellow LED Off
        #Turn Red LED On
        #Now we want to blink the yellow LED 10 times
        i = 0
        while(i<10):
            #Turn Buzzer On
            #Wait 0.01 Seconds
            #Turn Buzzer LED Off
            #Wait 0.01 Seconds
            #Add 1 to the count

        i = 0
        while(i<5):
            #Turn Yellow On
            #Wait 0.1 Seconds
            #Turn Yellow Off
            #Wait 0.1 Seconds
            #Add 1 to the count
        #Turn the Red LED off

except (keyboardinterrupt):
    #By doing this we reset the GPIO Pins back to default.
    print("Quitting Program")
    IO.cleanup()





