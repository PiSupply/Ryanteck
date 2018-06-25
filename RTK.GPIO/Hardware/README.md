# RTK GPIO

<img src="https://drive.google.com/uc?id=1nejyzGFNZUKKjXioRXjylOGQxs4civMZ" width="600" height="600">

The above image of the RTK.GPIO PCB is used in the following descriptions to highlight some of the inputs and outputs and other useful hardware information of the board.

## GPIO header

The GPIO header replicates the current 40-way GPIO header of the Raspberry Pi with the following pinouts.

| Pin#   | Name | Name | Pin#   |
| ----   | ---- | ---- | ----   |
|   1    | 3.3V     | 5V     |   2    |
|   3    | GPIO02     | 5V     |   4    |
|   5    | GPIO03     | GND     |   6    |
|   7    | GPIO04     | GPIO14     |   8    |
|   9    | GND     | GPIO15     |   10   |
|   11   | GPIO17     | GPIO18     |   12   |
|   13   | GPIO27     | GND     |   14   |
|   15   | GPIO22     | GPIO23     |   16   |
|   17   | 3.3V     | GPIO024     |   18   |
|   19   | GPIO10     | GND     |   20   |
|   21   | GPIO09     | GPIO25     |   22   |
|   23   | GPIO11     | GPIO08     |   24   |
|   25   | GND     | GPIO07     |   26   |
|   27   | GPIO00     | GPIO01     |   28   |
|   29   | GPIO05     | GND     |   30   |
|   31   | GPIO06     | GPIO12     |   32   |
|   33   | GPIO13     | GND     |   34   |
|   35   | GPIO19     | GPIO16     |   36   |
|   37   | GPIO26     | GPIO20     |   38   |
|   39   | GND     | GPIO21     |   40   |

# I2C

The I2C header is a breakout header from the 40 way GPIO header, which allows you to directly connect I2C devices to the RTK.GPIO board and keep the header free.

1. 5V
2. SDA
3. SCL
4. GND

# PROG

The PROG header allows you to directly program the STM32F030 MCU using ST Link, ST Nucleo Programmer or ST Link Clone programmers.

1. SWDIO
2. SWCLK
3. Reset
4. GND

# UART
This UART header is another way in which you can connect the RTK.GPIO board to your computer using serial to USB communication. The UARt header is connected to the CH340G serial to USB IC, which converts the signal and send it to the MCU.

1.
2.
3.
4.

# STM32F MCU

The main active microcontroller is a STM32F 030C8T6 from ST microelectronics.

* Core ARM 32-bit Cortex M0 CPU 48MHz
* 64 Kb Flash memory, 8 Kb SRAM
* 2.4-3.6V Operating voltage

# CH340G Serial to USB Convertor

The micro USB and UART connectors are connected to the serial chip interface, which converts USB to UART serial or vice versa when communicating between the MCU and your computer..

* Full speed USB 2.0 interface
* Supports common flow control signals RTS, DTR, DCD, RI, DSR and CTS
* Supports RS232, RS422 and RS485
* Uses the CH341 driver
* Supports both 5V and 3.3V operation
