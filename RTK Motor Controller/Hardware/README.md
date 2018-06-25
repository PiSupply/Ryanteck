# RTK Motor Controller Board

<img src="https://drive.google.com/uc?id=1F4HU0QRtmpFsVreogqSMVeMkVLBE3yXS" width="600" height="600">

The above image of the RTK Motor Controller Board PCB is used in the following descriptions to highlight some of the inputs and outputs and other useful hardware information of the board.

## Motor-1 Motor-2

These two screw terminals are used to connect two motors to the motor controller board. You can connect the wires from your motor to the terminals by un-screwing the screw and inserting the wire into the hole and the screw the terminal back down. The red wire should be inserted into the most left screw hole and the black next to it for a clockwise motor direction.

## VCC2

VCC2 screw terminal provides power to the motors and the motor controller chip. You can connect a power supply from 4.5V to 36V ma with current up to 1A. The left terminal it the +V (Red wire) and the right terminal is GND (Black wire).

## GPIO Breakout Headers

There are two rows of 10 GPIO headers, which are breakout from the main 26-way Raspberry Pi GPIO header.

## SN75441ONE

The main active component is the SN75441ONE H-Bridge motor controller by TI. 
