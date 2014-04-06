#!/usr/bin/python
import sys
import smbus
import time

# Reads data from PCF8574 and prints the state of each port

def readPCF8574(busnumber,address):
    address = int(address,16)
    busnumber = int(1)
    bus = smbus.SMBus(busnumber)
    state = bus.read_byte(address);

    for i in range(0,8):
        port = "port " + str(i) 
        value = 1&(state>>7-i)
        print str(port) + ': ' + str(value)   



if len(sys.argv) != 3:
    print "Usage: python PCF8574.py bus address"
    exit(1)

bus = sys.argv[1]
address = sys.argv[2]

readPCF8574(bus,address)
