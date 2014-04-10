#!/usr/bin/python

# reads data from I2C-A/D-Module from http://www.horter.de/blog/i2c-analog-input-5-kanaele-10-bit/

import smbus
VMAX=29.97527273
I2CBUS=1
ADDRESS=0x08

# converts raw-value to voltage
def convert(raw):
    return raw * (VMAX/1024.)

# reads 11 bytes from ic2bus - address
def readAnalogIn(busnumber,address):
    bus = smbus.SMBus(busnumber)
    data = bus.read_i2c_block_data(address,0,11)
    print "Reading 11 bytes: ", data

    pointer = data[0]
    raw1 = data[1] + data[ 2] * 256
    raw2 = data[3] + data[ 4] * 256
    raw3 = data[5] + data[ 6] * 256
    raw4 = data[7] + data[ 8] * 256
    raw5 = data[9] + data[10] * 256
 
    print "Port 1 - raw: ",raw1," => ",convert(raw1),"V"
    print "Port 2 - raw: ",raw2," => ",convert(raw2),"V"
    print "Port 3 - raw: ",raw3," => ",convert(raw3),"V"
    print "Port 4 - raw: ",raw4," => ",convert(raw4),"V"
    print "Port 5 - raw: ",raw5," => ",convert(raw5),"V"

# run commands
readAnalogIn(I2CBUS,ADDRESS)

