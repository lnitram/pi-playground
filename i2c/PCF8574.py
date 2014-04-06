#!/usr/bin/python
import sys
import smbus
import time
import argparse

# Reads data from PCF8574 and prints the state of each port
def readPCF8574(busnumber,address):
    address = int(address,16)
    busnumber = int(busnumber)
    bus = smbus.SMBus(busnumber)
    state = bus.read_byte(address);
    for i in range(0,8):
        port = "port " + str(i) 
        value = 1&(state>>7-i)
        print str(port) + ': ' + str(value)   

# Reads data from PCF8574 and prints the inverted state of each port
def readPCF8574_INV(busnumber,address):
    address = int(address,16)
    busnumber = int(busnumber)
    bus = smbus.SMBus(busnumber)
    state = 255 - bus.read_byte(address);
    for i in range(0,8):
        port = "port " + str(i)
        value = 1&(state>>(7-i))
        print str(port) + ': ' + str(value)

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i",action='store_true', help="Invert the bit of in- and output")
parser.add_argument('i2c_bus',  help='Number of active i2c-bus (0 or 1)')
parser.add_argument('i2c_address', help='address of PCF8574')
args = parser.parse_args()

# run commands
if args.i:
    readPCF8574_INV(args.i2c_bus,args.i2c_address)
else:
    readPCF8574(args.i2c_bus,args.i2c_address)
