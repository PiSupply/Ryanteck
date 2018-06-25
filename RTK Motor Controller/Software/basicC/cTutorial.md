#Programming the RTK-000-001 / RTK-000-003 using C

In this tutorial we will be showing you how to program your RTK-000-001 Motor Controller to control two motors.
These instructions also apply to the RTK-000-003 Budget Robotics Kit.

**Install some necessary software**
First make sure your Pi is up to date with the latest versions of Raspbian:

```sudo apt-get update```
```sudo apt-get upgrade```

If you do not have Git installed, then under Raspbian (or any of the Debian releases) you can install it with:

```sudo apt-get install git-core```

**Download and Install wiringPi (the C library for controlling GPIOs)**

First of all, obtain WiringPi using Git:

```git clone git://git.drogon.net/wiringPi```

Now build/install it using this script:

```cd wiringPi```
``` ./build ```

This last command will run a script to compile and install it all for you.

##Creating the basis
First we will create the basis which will be used throughout. You will need to use the command line for this. Either use the command prompt you get after logging in, connect via SSH or open up LX Terminal if you are in X windows. At the command prompt, run ```nano robotC.c```

First, we will set up and configure the GPIO pins on the Raspberry Pi.

Start by adding the following lines:

```
#include <stdio.h>

// import the module that controls the GPIO pins
#include <wiringPi.h>

// Set pin numbers here - this will make them global
int m1a = 0;
int m1b = 1;
int m2a = 3;
int m2b = 4;

// main function
int main (void)
{
  // setup the GPIO module
  wiringPiSetup();

  // set up all the pins as outputs
  pinMode(m1a, OUTPUT);
  pinMode(m1b, OUTPUT);
  pinMode(m2a, OUTPUT);
  pinMode(m2b, OUTPUT);

  return 0;
}
```

Now we will create a function to turn both motors in the forward direction. Add the following to your code.

```
//make robot go forwards
void forwards()
{
  digitalWrite(m1a, HIGH);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, HIGH);
  digitalWrite(m2b, LOW);
}
```

Next we need to add in a 'stop' function, add this after the code above
```
//all motors off
void stop()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, LOW);
}
```

On it's own, this code won't do anything. So, to test out everything is working correctly, we add in a small loop to make the motors go forwards for half a second and then stop for half a second.

Do this by replacing the 'int main(void)' function with this one:

```
//main function
int main (void)
{
  //setup the GPIO module
  wiringPiSetup();

  //set the pins up as outputs
  pinMode(m1a, OUTPUT);
  pinMode(m1b, OUTPUT);
  pinMode(m2a, OUTPUT);
  pinMode(m2b, OUTPUT);

  for (;;)
  {
    //Turn motors forward
    printf("forwards");
    forwards();
    delay(500);

    //Stop
    printf("stop");
    stop();
    delay(500);
  }
  return 0;
}
```

Now we can save the code by pressing ```Ctrl + X``` to save, ```y``` to confirm writing and then ```enter``` to confirm to save.

We now want to run our code. Because we are using C, we need to first of all compile the code. We do this by running the following command:
```gcc -Wall -o robotC robotC.c -lwiringPi```
We then run our program by typing
```sudo ./robotC```

The motors should move forwards for half a second, then stop for half a second. This repeats until you stop the program by pressing Ctrl-C. You should press Ctrl-C when the motors are stopped otherwise they will continue to run.

####Troubleshooting direction
It is possible that the first time you run your code the motors will cause the wheels to run in the wrong direction. This can be easily fixed using either a small code change or swapping a wire over on the board.

#####Code Fix
First identify which motor is going in the wrong direction and follow the cable to the board. If it is M1 then swap m1a to be 1 and m1b to be 0, if it is M2 then change m2a to be 4 and m2b to be 3. Re-compile and re-run the code and you should have them both going the right way.

#####Wire Swap
An easier solution (which means all tutorials will be using the same numbers) is just to unscrew the motor going the wrong way and plug the wires in the other way round. Both motors should go the same way now.

###Backwards, Left & Right
To add in the other directions is very simple. Start by re-opening the program by running ```nano robotC.c``` and repeat the 'forwards' code 3 times, changing the forwards to backwards, left and right for each function.

Next we need to modify them to move the motors in other directions. 

Make your extra code look like the following:
```
//Make both motors turn backwards
void reverse()
{
 digitalWrite(m1a, LOW);
 digitalWrite(m1b, HIGH);
 digitalWrite(m2a, LOW);
 digitalWrite(m2b, HIGH);
}

void left()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1b, HIGH);
  digitalWrite(m2a, HIGH);
  digitalWrite(m2b, LOW);
}

//Make motors turn fwd, bak
void right()
{
  digitalWrite(m1a, HIGH);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, HIGH);
}
```

If you find your robot turns the wrong way, either swap the wires over or change the names of the left/right functions to correct the problem.

We have now got the basis of our code completed for the next tutorials.

-Written by Zachary Igielman (@ZacharyIgielman)
