/*/*
* RTk.GPIO Microcontroller Firmware
* Copyright (C) Ryanteck LTD. (R) 2016. Licensed under GNU GPL V3
* For full license information please read License.MD
*
* Based off of AnyIO For Arduino by David Whale (@whaleygeek)
* https://rtkgpio.xyz
*/


/* Import MBED Libraries */

#include "mbed.h"
#include <stdio.h>
#include <stdlib.h>
#include "math.h"

/* Setup the serial port on the default pins for the RTk.GPIO */
Serial serialPort(SERIAL_TX, SERIAL_RX);

/* AnyIO requests the version if V is sent, Version is now compiled date */
#define VERSION_STR "RTk-2016-01-05-FINAL"

/* Set the serial baudrate. 230400 has tested stable on all platforms. (WIN,MAC,NIX) */
#define BAUD_RATE 230400



/* Define the lowest and highest GPIO pins. For this its 0-27 */
#define MIN_PIN 0
#define MAX_PIN 27

/*
* Errors are sent back via the 'E' Response.
* These are pre-done definitions for each error code.
*/
enum
{
    ERROR_BAD_PIN_RANGE = 1,
    ERROR_UNKNOWN_COMMAND = 2
};

/* Local function prototypes */
/* TO-DO - Find the simpleton way of describing above */

static void command(char cmdch, char paramch);
static void gpio(char pinch, char cmdch);
//static void agpio(char pinch, char cmdch);
static void error(int code);

/* TO-DO - Proper Comment */
static int ioPin;
static int p;


/* Define all of the IO pins as DigitalInOut */
DigitalInOut IO0(GPIO0);
DigitalInOut IO1(GPIO1);
DigitalInOut IO2(GPIO2);
DigitalInOut IO3(GPIO3);
DigitalInOut IO4(GPIO4);
DigitalInOut IO5(GPIO5);
DigitalInOut IO6(GPIO6);    /* Comment out for debug mode */
DigitalInOut IO7(GPIO7);
DigitalInOut IO8(GPIO8);
DigitalInOut IO9(GPIO9);
DigitalInOut IO10(GPIO10);
DigitalInOut IO11(GPIO11);
DigitalInOut IO12(GPIO12);
DigitalInOut IO13(GPIO13);  /* Comment out for debug mode */
DigitalInOut IO14(GPIO14);
DigitalInOut IO15(GPIO15);
DigitalInOut IO16(GPIO16);
DigitalInOut IO17(GPIO17);
DigitalInOut IO18(GPIO18);
DigitalInOut IO19(GPIO19);
DigitalInOut IO20(GPIO20);
DigitalInOut IO21(GPIO21);
DigitalInOut IO22(GPIO22);
DigitalInOut IO23(GPIO23);
DigitalInOut IO24(GPIO24);
DigitalInOut IO25(GPIO25);
DigitalInOut IO26(GPIO26);
DigitalInOut IO27(GPIO27);

//SoftPWM pwm[] = {GPIO0,GPIO1,GPIO2,GPIO3,GPIO4,GPIO5,GPIO6,GPIO7,GPIO8,GPIO9,GPIO10,GPIO11,GPIO12,GPIO13,GPIO14,GPIO15,GPIO16,GPIO17,GPIO18,GPIO19,GPIO20,GPIO21,GPIO22,GPIO23,GPIO24,GPIO25,GPIO26,GPIO27};
/* TO-DO - Proper Comment */
I2C i2c(GPIO2,GPIO3);

/* Uncomment these two lines if you comment out the ones above for debugging mdoe */
//DigitalInOut IO6(NC);
//DigitalInOut IO13(NC);

/* Define list of Pins */
DigitalInOut gpios[] = {IO0,IO1,IO2,IO3,IO4,IO5,IO6,IO7,IO8,IO9,IO10,IO11,IO12,IO13,IO14,IO15,IO16,IO17,IO18,IO19,IO20,IO21,IO22, IO23, IO24,IO25,IO26,IO27};


/* Start the main program routine */

int main() {
    //SystemClock_Config
    //Arduino equiv for setup



    //All setup as digital in.

    /* Setup the serial port at baudrate and send ready message */
    serialPort.baud(BAUD_RATE);
    serialPort.format(8,mbed::SerialBase::None,1);
    serialPort.printf("RTk.GPIO Ready");

    /*
    * Uncomment the below line for clock speed reporting. Useful for debugging
    */
    serialPort.printf("SystemCoreClock = %d Hz\n",SystemCoreClock);


    /* Now the main loop that repeats forever */
    while(1) {

        /* Wait for the serial port to be available */
        if(serialPort.readable() == 1) {
            /* Serial port is available, get the character sent */
            char pinch = (char) serialPort.getc();

            /* TO-DO Maybe optimize this. If its not lowercase or uppercase the \r and \n check shouldn't be needed */
            /* If its not a return or newline command */
                /* If its a uppercase it will be a "Global" Command so send it to that handler. */
                if(pinch >= 'A' && pinch <= 'Z') {
                    char paramch = (char) serialPort.getc();
                    command(pinch, paramch);
                }
                /* If not make sure its a lowercase command which means GPIO request */
                else if (pinch >= 'a' && pinch <= '|')
                {
                    char cmdch = (char) serialPort.getc();
                    gpio(pinch, cmdch);
                }
                /*If it's a newline or return command ignore */
                else if(pinch !='\r' && pinch !='\n' )
                {
                	/* Do Nothing */
                }
                /* If it gets this far its a dud command and we don't want it */
                else
                {
                    error(ERROR_UNKNOWN_COMMAND);
                }

        }

    }
}

/*
* Function to generate an error
* Should always be E + Number with newline
*/
static void error(int code)
{
    serialPort.putc('E');
    serialPort.putc('1');
    serialPort.putc('\r');
    serialPort.putc('\n');
}

/*
* Process a command.
*
* A command is a single character that identifies the command,
* followed by parameters. In most cases parameters are a single
* character, but there is no need for them to be. Each command knows
* how to detect the end of it's parameter string, be that length
* or magic character based.
*/

static void command(char cmdch, char paramch)
{
    switch(cmdch)
    {
    case 'V': // Version
        serialPort.printf(VERSION_STR);
    break;

    case 'G': //GPIO
    {
        while (serialPort.readable() == 0)
        {
            /* Wait for stuff to arrive*/

        }
        char pinch = paramch;
        char cmdch = (char)serialPort.getc();
        gpio(pinch, cmdch);
    }

    case 'I':

        switch(paramch) {
            case 'W': {
                //Write to I2C Bus
                int i2caddr = (int)serialPort.getc();
                int i2cBlocks = (int)serialPort.getc();

                int curBlock = 0;
                char cmdBlk[255];
                while(curBlock <= i2cBlocks) {
                    //Get Block
                    cmdBlk[curBlock] = (int)serialPort.getc();

                    curBlock++;
                }

                //Write I2C Data
                i2c.write(i2caddr,cmdBlk,i2cBlocks+1);  //Error, this line runs first
            }
            break;

            case 'R': {
                //Read to I2C Bus
                int i2caddr = (int)serialPort.getc();
                int i2cBlocks = (int)serialPort.getc();
                int curBlock = 0;
                char cmdBlk[i2cBlocks];
                cmdBlk[0] = (int)serialPort.getc();

                //Write I2C Data
                i2c.read(i2caddr,cmdBlk,i2cBlocks);
                while (curBlock < i2cBlocks) {
                	serialPort.putc(cmdBlk[curBlock]);
                	curBlock++;
                }
                //serialPort.put(pinC);
                //serialPort.putc(pinch);
                //serialPort.printf(p?"1":"0");
                //serialPort.putc('\r');
                //serialPort.putc('\n');

            }
                        break;


        }

    break;

    /*case 'P':
    {
        	char pinch = (char)serialPort.getc();
        	int pin = pinch - 'a';
                switch(paramch) {

                    case 'T': {
                    	pwm[pin].start();
                    }
                    case 'P': {
                         pwm[pin].stop();
                    }


                }
    }
     break;*/





    default:
        //Reject all other commands
        serialPort.putc(cmdch);
        error(ERROR_UNKNOWN_COMMAND);
        break;
    }
}



/* Process a GPIO command.
 *
 * GPIO Commands are two characters.
 * <pinch> <cmdch>
 *
 * pinch is the pin character (a..z) where 'a' represents pin 0.
 * cmdch is the command to perform on that pin:
 *   I: Set this pin to a digital input,        eg: aI
 *   O: Set this pin to a digital output,       eg: aO
 *   0: Write a digital low to this output,     eg: a0
 *   1: Write a digital high to this output,    eg: a1
 *   U: Write a pull input high,    eg: aU
 *   D: Write a pull input down,    eg: aD
 *   ?: Read the state of this digital input,   eg: a?
 *      State is returned as pinch + state(0|1) eg: a0
 */


static void gpio(char pinch, char cmdch)
{   /* GPIO Command Start */

    int pin = pinch - 'a';
    //pin = pin; //Fixes 25 pin issue

    if (pin < MIN_PIN || pin > MAX_PIN)
    {
        error(ERROR_BAD_PIN_RANGE);
    }

    else {
        //Valid pin label
        char pinC;
        pinC = pin;

        /*serialPort.putc(pin);

        serialPort.putc('\r');
        serialPort.putc('\n');*/

        ioPin = pin;

        switch (cmdch)
        {

            /*case 'A':
            {
            //ioPin = pin -2;

                double aIn = agpios[0].read();
                //char cAin[50];
                //snprintf(cAin,50, "%f", aIn);
                serialPort.putc(pinch);
                serialPort.printf("%.7f",aIn);
                serialPort.putc('\r');
                serialPort.putc('\n');

                //serialPort.putc(faIn);

                //serialPort.printf("SystemCoreClock = %c Hz\n",a8In);

            break;
            }*/

            case 'I': //Set as input
                //ioPin = pin - 2;
                gpios[ioPin].input();
                gpios[ioPin].mode(PullNone);
            break;

            case 'O':
                //ioPin = pin - 2;
                gpios[ioPin].output();
            break;

            case '0':
                //ioPin = pin - 2;
                gpios[ioPin] = 0;

            break;

            case '1':
                //ioPin = pin - 2;
                gpios[ioPin] = 1;
            break;


            case '?':
                //ioPin = pin -2;
                p = gpios[ioPin].read();
                serialPort.putc(pinch);
                serialPort.printf(p?"1":"0");
                serialPort.putc('\r');
                serialPort.putc('\n');

            break;

            case 'U':

                gpios[ioPin].mode(PullUp);
            break;

            case 'D':

                gpios[ioPin].mode(PullDown);
            break;

            case 'N':

                gpios[ioPin].mode(PullNone);
            break;






        }
    }
/* GPIO Command End */  }


/*--------------------------------------------------------------------*/
/* Process a Analogue command.
 *
 * Analogue Commands are two characters.
 * <pinch> <cmdch>
 *
 * pinch is the pin character (a..z) where 'a' represents pin 0.
 * cmdch is the command to perform on that pin:
 *   I: Set this pin to a Analogue input,        eg: aI
 *   O: Set this pin to a Analogue output,       eg: aO
 *   0: Write a Analogue low to this output,     eg: a0
 *   1: Write a Analogue high to this output,    eg: a1
 *   ?: Read the state of this Analogue input,   eg: a?
 *      State is returned as pinch + state(0|1) eg: a0
 */
