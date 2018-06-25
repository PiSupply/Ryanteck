#Programming the RTK-000-001 / RTK-000-003 using python

In this tutorial we will be showing you how to program your RTK-000-001 Motor Contoller to move around two motors for robots including the RTK-000-003 Budget Robotics Kit

##Creating the basis
First we will create the basis which will be used throughout. Start by either connecting via SSH or using a screen / VNC (Opening up LX Terminal) and running ```nano robotPython.py```

We will be first setting up and configuring the GPIO pins on the Raspberry Pi and then creating 4 functions which we will then be able to use to easily control both motors at the same time.

Start by adding in the following lines. You require to copy the code but not the comments indicated with the # symbol.

```
#RTK-000-001 Basis
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley, Michael Horne
from time import sleep #We will need to sleep the code at points
import RPi.GPIO as GPIO #Import the GPIO library as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

#Assign variables to pins
m1a = 17
m1b = 18
m2a = 22
m2b = 23

GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)

```
This has now setup the GPIO pins ready for use.

Now we will make a function to turn both motors forward, add the following now to your code.

```
#Make both motors go forwards
def forwards():
        GPIO.output(m1a,1) # Motor 1 Forwards turn on
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,1) # Motor 2 Forwards turn on
        GPIO.output(m2b,0) # Motor 2 Backwards turn off
```
Next we need to add in a stop function, add this after the code above
```
##All off
def stop():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,0) # Motor 2 Backwards turn off
```
Finally we want to add in a small loop to make the motors go forwards for one second and then stop for another.
Do this by adding the following
```
#Forever
while True:
    #Turn motors forward
    print "forwards"
    forwards()
    #sleep for 1 second
    sleep(1)
    #Stop
    print "stop"
    stop()
    #sleep 1 second
    sleep(1)
```

Now we can save the code by running the following commands, ```Ctrl + X``` to save, ```y``` to confirm writing and then ```enter``` to confirm to save.

We now want to run our python code, do this by running ```sudo python robotPython.py```, the motors should move forwards and print forwards and stop each time they start going forwards or stop.
####Troubleshooting direction
It is likely that the first time you run your code the motors will move in oposite directions, this can be easily fixed using either a small code change or swapping a wire over on the board.
#####Code Fix
First identify which motor is going in the wrong direction and follow the cable to the board. If it is M1 then swap m1a to be 18 and m1b to be 17, if it is M2 then change m2a to be 23 and m2b to be 22. Re run the code and you should have them both going the right way.

#####Wire Swap
An easier solution which means all tutorials will be using the same numbers is just to unscrew the motor going the wrong way and plug the wires in the other way round. Both motors should go the same way now.

###Backwards, Left & Right
To add in the other directions in very simple, start by re-opening the python program by running ```nano robotPython.py``` and repeat the forwards code 3 more times changing the forwards to backwards, left and right for each function.
Next we need to modify them to move the motors in other directions. 
We need the following outputs for each motor. This assumes Motor 1 will be on the left and Motor 2 on the right

*Backwards, m1b & m2b on. m1a & m2a off.
*Left, m1b & m2a on. m1a & m2b off.
*Right, m1a & m2b on. m1b & m2a off.
Your code should now have the following above the while loop.
```
#Make motors turn bak, bak  
def backwards():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,1) # Motor 1 Backwards turn on
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,1) # Motor 2 Backwards turn on
        
#Make motors turn fwd, bak      
def left():
        GPIO.output(m1a,1) # Motor 1 Forwards turn on
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,1) # Motor 2 Backwards turn on
        #Make both motors go forwards
        
#Make motors turn fwd, bak          
def right():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,1) # Motor 1 Backwards turn on
        GPIO.output(m2a,1) # Motor 2 Forwards turn on
        GPIO.output(m2b,0) # Motor 2 Backwards turn off
```

Woo! We have now got the basis of our code completed for the next tutorials.
