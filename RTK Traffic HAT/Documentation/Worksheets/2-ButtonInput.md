
<img src = "logonobg.png"/>

#Beginners GPIO - 2
##Detecting button input
In this worksheet we will instead use the button to turn on the LED when we press the button and off when we release the button.

Begin by loading up the code from the last worksheet and saving it as ```2-ButtonInput.md```

To begin we want to first assign the variable button to the GPIO pin that the button uses.
Underneath the line that says ```green = 22``` add ```button = 25```.

Next we want to setup the button to be an input.
Underneath the line that says ```IO.setup(green,IO.OUT)``` you will need to add the following line.

```python
IO.setup(button,IO.IN,pull_up_down=IO.PUD_UP)

```

That section of code should now look like this in total

```python

#Next we want to setup the Green LED as an output
green = 22
button = 25

IO.setup(green,IO.OUT) # This sets the green LED to be an output.
IO.setup(button,IO.IN,pull_up_down=IO.PUD_UP)
```

**This will then successfully setup the button to be an input**

That last section of the setup for the input isn't always required for every add-on, the TrafficHAT requires it for it's button to work.

By doing this the Pi pull's the GPIO line high (1) and then when we press the button it turns the GPIO line to low (0).

Here's a picture of what happens when you press the button.

<img src = "scopebutton.png"/>

To finish our button code we then need to add the line to wait for the button press.

Underneath the line ```IO.output(green,1)``` we then want to wait for the button to be pressed.

Underneath this line add the following code:

```python
while(IO.input(25)):
    pass
IO.output(green,0)
```
Don't forget this has to be indented with the rest of the code.
Your code section here should now look like this

```python
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
```

What this will now do is while the button is not pressed (It will read as high / 1 as described above) it will wait forever and do nothing (by using the pass command);

Once it is pressed it will then turn off the Green LED.

Now try running your code and then press the button.

**The light will not actually turn off, instead it should go dimm.**

By using an oscilioscope we can see what happens.

<img src = "scope1.png"/>

**The picture above is a snapshot of what happens when that program is running and I press the button. If we zoom in we can then see what is happening more clearly.**

<img src = "scope2.png"/>

**Due to there not being a delay after it turning off its then instantly turning it back on with the only delay being the time it takes for the Pi to run the code. **

To fix this we need to just add one line after turning the green light off.

Try adding a delay of 0.1 seconds after turning off the green light by adding undeneath it:
```
sleep(0.1)
```

And now re-run your program. Your light should turn off.

Now in the code the light is still being turned on each time but as there is a longer delay of it being off our eyes see it as being turned off.

Here's that same code on the oscilioscope again. This time zoomed in at the same level of the first picture.

<img src = "scope3.png"/>

As you can see they are just very little blips from where it is turning on.

Congratulations you have successfully used the button!
