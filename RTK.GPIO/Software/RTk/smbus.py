#RTK.GPIO implementation of SMBUS
import RTk.rtkserial as rtkserial
from pprint import pprint
from time import sleep
import binascii
serial = rtkserial.s
print("imported rtkbus")
i = 0.0017
class SMBus:

    def __init__(self,bus):
        self.bus = bus
    def _write(self,str):

        serial.write(str.encode("raw_unicode_escape"))
    def _writec(self,str):
        #print((str))
        serial.write(bytes(str.encode("raw_unicode_escape")))
    def _read(self, maxsize=1, minsize=None, termset=None, timeout=None):
        if minsize == None:
          minsize = maxsize

        remaining = maxsize
        if termset != None:
          readsz = 1
        else:
          readsz = remaining

        buf = b''

        while len(buf) < minsize:
          data = serial.read(readsz)
          if (len(data) == 0):
              time.sleep(0.1) # prevent CPU hogging
          else:
              #print("just read:" + data)
              buf = buf + data
              remaining -= len(data)
              if termset != None:
                  if data[0] in termset:
                      break # terminator seen

        return buf

    def write_i2c_block_data(self,i2caddress,command,data):
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),16))
        #and now convert that to a letter
        self._write("IW") #I2C write
        self._write(i2caddrchar) # Write the 8 Bit I2C address
        self._write(chr(int(len(data))))
        self._write(chr(int(hex(command),0))) # Write the command char
        for idx, dataVal in enumerate(data): #Write each item of data
            self._write(chr(int(hex(dataVal),16))) #Data
            sleep(i)
    def write_byte_data(self,i2caddress,command,data):
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        #and now convert that to a letter
        self._write("IW") #I2C write
        self._write(i2caddrchar) # Write the 8 Bit I2C address
        self._write(chr(int(1)))
        self._write(chr(int(hex(command),0))) # Write the command char
        self._write(chr(int(hex(data),0))) #Data
        sleep(i)

    def write_word_data(self,i2caddress,command,data):
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        #and now convert that to a letter
        self._write("IW") #I2C write
        self._write(i2caddrchar) # Write the 8 Bit I2C address
        self._write(chr(int(1)))
        self._write(chr(int(hex(command),0))) # Write the command char
        self._write(chr(int(hex(data),0))) #Data
        sleep(i)

    def write_byte(self,i2caddress,command):
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        #and now convert that to a letter
        self._write("IW") #I2C write
        self._write(i2caddrchar) # Write the 8 Bit I2C address
        self._write(chr(int(0)))
        self._write(chr(int(hex(command),0))) # Write the command char
        #self._write(chr(int(hex(data),0))) #Datas
        sleep(i)

    def read_word_data(self,i2caddress,command) :
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        self._write("IR") #I2C Read
        self._write(i2caddrchar)
        self._write(chr(int(2)))
        self._write(chr(int(hex(command),0)))
        wordDat1 =int(binascii.hexlify(serial.read()))
        wordDat2 = int(binascii.hexlify(serial.read()))
        print(wordDat1)
        print(wordDat2)
        print("read")
        #return(wordDat2)
        wordDat = int(hex((wordDat2<<8)+wordDat1),0)
        sleep(i)

        return(wordDat)

    def read_word_dataT(self,i2caddress,command) :
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        self._write("IR") #I2C Read
        self._write(i2caddrchar)
        self._write(chr(int(2)))
        self._write(chr(int(hex(command),0)))
        serIn1 = serial.read()


        return(serIn1)

    def read_byte_data(self,i2caddress,command):
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        self._write("IR") #I2C Read
        self._write(i2caddrchar)
        self._write(chr(int(1)))
        self._write(chr(int(hex(command),0)))
        wordDat1 =int(binascii.hexlify(serial.read()))
        #return(wordDat2)
        byteDat = int(hex((wordDat1)),16)
        sleep(i)

        return(byteDat)

    def read_i2c_block_data(self,i2caddress,command):
        #Read a block (16 Bytes) of I2C Data
        blockData = []
        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        self._write("IR") #I2C Read
        self._write(i2caddrchar)
        self._write(chr(int(16)))
        self._write(chr(int(hex(command),0)))
        ii = 0;
        while(ii<16):
             byteDat=int(binascii.hexlify(serial.read()),16)
             blockData.append(int(hex((byteDat)),0))
             ii = ii+1
        sleep(i)

        return(blockData)

    def read_byte(self,i2caddress):
        #Currently does nothing
        pass
