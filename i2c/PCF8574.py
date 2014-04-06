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

# Writes bitstring to PCF8574
def writePCF8574(busnumber,address,bitstring):
    address = int(address,16)
    busnumber = int(busnumber)
    bus = smbus.SMBus(busnumber)
    state = int(bitstring,2)
    bus.write_byte(address,state)

# Writes inverted bitstring to PCF8574
def writePCF8574_INV(busnumber,address,bitstring):
    address = int(address,16)
    busnumber = int(busnumber)
    bus = smbus.SMBus(busnumber)
    state = int(bitstring,2)
    state = 255 - state 
    bus.write_byte(address,state)

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i",action='store_true', help="Invert the bit of in- and output")
parser.add_argument("-w","--write",help="Bitstring that will be written to PCF8574")
parser.add_argument('i2c_bus',  help='Number of active i2c-bus (0 or 1)')
parser.add_argument('i2c_address', help='address of PCF8574')
args = parser.parse_args()

# run commands
if args.write:
    if args.i:
        writePCF8574_INV(args.i2c_bus,args.i2c_address,args.write)
    else:
        writePCF8574(args.i2c_bus,args.i2c_address,args.write)

if args.i:
    readPCF8574_INV(args.i2c_bus,args.i2c_address)
else:
    readPCF8574(args.i2c_bus,args.i2c_address)

