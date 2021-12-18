#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# TEMP.py
#___________________________________________________
# Author: 
#           Marín Jiménez Irving
#           Salas Garcia Alejandra
#___________________________________________________
# License: MIT
#
# ## ###############################################
import smbus2
import struct
import time
import threading
from time import sleep
# Arduino's I2C device address
SLAVE_ADDR = 0x0A # I2C Address of Arduino

# Initialize the I2C bus;
# RPI version 1 requires smbus.SMBus(0)
i2c = smbus2.SMBus(1)

def readTemperature(clima):
	temp = float(clima)
	"""Reads a temperature bytes from the Arduino via I2C"""
	try:
		msg = smbus2.i2c_msg.read(SLAVE_ADDR, 2)
		i2c.i2c_rdwr(msg)
		temp = struct.unpack('<H', msg.buf)[0]
		tempFinal = temp * (2.05/10.24)#convierte los valores del voltaje
		print(tempFinal)
	except:
		None
#	return tempFinal
#end def

def TEMPERATURA(temp):
	temp = float(temp)
	try:
		ctemp = readTemperature(temp)
		print("La temperatura es de: ",temp)
		time.sleep(1)
	except KeyboardInterrupt:
		return
#end def
