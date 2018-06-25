import sys

try:
    from RTk.smbus import SMBus
except ImportError:
    if sys.version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif sys.version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

I2C_ADDRESS = 0x54
CMD_ENABLE_OUTPUT = 0x00
CMD_SET_PWM_VALUES = 0x01
CMD_ENABLE_LEDS = 0x13
CMD_UPDATE = 0x16
CMD_RESET = 0x17


def i2c_bus_id():
    revision = ([l[12:-1] for l in open('/proc/cpuinfo', 'r').readlines() if l[:8] == "Revision"]+['0000'])[0]
    return 1 if int(revision, 16) >= 4 else 0


def enable():
    """ 
    Enables output.
    """
    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_ENABLE_OUTPUT, [0x01])


def disable():
    """ 
    Disables output.
    """
    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_ENABLE_OUTPUT, [0x00])


def reset():
    """ 
    Resets all internal registers.
    """
    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_RESET, [0xFF])


def enable_leds(enable_mask):
    """ 
    Enables or disables each LED channel. The first 18 bit values are
    used to determine the state of each channel (1=on, 0=off) if fewer
    than 18 bits are provided the remaining channels are turned off.

    Args:
        enable_mask (int): up to 18 bits of data
    Raises:
        TypeError: if enable_mask is not an integer.
    """
    if type(enable_mask) is not int:
        raise TypeError("enable_mask must be an integer")

    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_ENABLE_LEDS, [enable_mask & 0x3F, (enable_mask >> 6) & 0x3F, (enable_mask >> 12) & 0X3F])
    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_UPDATE, [0xFF])


def channel_gamma(channel, gamma_table):
    """ 
    Overrides the gamma table for a single channel.

    Args:
        channel (int): channel number
        gamma_table (list): list of 256 gamma correction values
    Raises:
        TypeError: if channel is not an integer.
        ValueError: if channel is not in the range 0..17.
        TypeError: if gamma_table is not a list.
    """	
    global channel_gamma_table

    if type(channel) is not int:
        raise TypeError("channel must be an integer")

    if channel not in range(18):
        raise ValueError("channel be an integer in the range 0..17")

    if type(gamma_table) is not list or len(gamma_table) != 256:
        raise TypeError("gamma_table must be a list of 256 integers")

    channel_gamma_table[channel] = gamma_table	


def output(values):
    """ 
    Outputs a new set of values to the driver

    Args:
        values (list): channel number
    Raises:
        TypeError: if values is not a list.
    """ 
    if type(values) is not list or len(values) != 18:
        raise TypeError("values must be a list of 18 integers")

    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_SET_PWM_VALUES, [channel_gamma_table[i][values[i]] for i in range(18)])
    i2c.write_i2c_block_data(I2C_ADDRESS, CMD_UPDATE, [0xFF])


i2c = SMBus(0)

# generate a good default gamma table
default_gamma_table = [int(pow(255, float(i - 1) / 255)) for i in range(256)]
channel_gamma_table = [default_gamma_table] * 18

enable_leds(0b111111111111111111)

if __name__ == "__main__":
    print("sn3218 test cycles")
    
    import time
    import sys
    import os
    import math

    # disable output buffering for our test activity dots
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    # enable output
    enable()
    enable_leds(0b111111111111111111)
    
    print(">> test enable mask (on/off)")
    enable_mask = 0b000000000000000000
    output([0x10] * 18)
    for i in range(10):
        enable_mask = ~enable_mask
        enable_leds(enable_mask)
        time.sleep(0.15)
    print("")

    print(">> test enable mask (odd/even)")
    enable_mask = 0b101010101010101010
    output([0x10] * 18)
    for i in range(10):
        enable_mask = ~enable_mask
        enable_leds(enable_mask)
        time.sleep(0.15)
    print("")

    print(">> test enable mask (rotate)")
    enable_mask = 0b100000100000100000
    output([0x10] * 18)
    for i in range(10):
        enable_mask = ((enable_mask & 0x01) << 18) | enable_mask >> 1
        enable_leds(enable_mask)
        time.sleep(0.15)
    print("")

    print(">> test gamma gradient")
    enable_mask = 0b111111111111111111
    enable_leds(enable_mask)
    for i in range(256):
        output([((j * (256/18)) + (i * (256/18))) % 256 for j in range(18)])
        time.sleep(0.01)
    print("")

    print(">> test gamma fade")
    enable_mask = 0b111111111111111111
    enable_leds(enable_mask)
    for i in range(512):
        output([int((math.sin(float(i)/64.0) + 1.0) * 128.0)]*18)
        time.sleep(0.01)
    print("")

    # turn everything off and disable output
    output([0 for i in range(18)])
    disable()
