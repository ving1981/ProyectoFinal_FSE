#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# RADIADOR.py
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
import RPi.GPIO as GPIO

# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Configurando los pins de salida como bajos por defecto
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #Ventilador por pwm

# Arduino's I2C device address
SLAVE_ADDR = 0x0A # I2C Address of Arduino

# Initialize the I2C bus;
# RPI version 1 requires smbus.SMBus(0)
i2c = smbus2.SMBus(1)

def escribePotencia(potencia):
	try:
		data = struct.pack('<f', potencia) 
		#Generación del mensaje I2C de tipo escritura
		msg = smbus2.i2c_msg.write(SLAVE_ADDR, data)
		i2c.i2c_rdwr(msg) #Escritura en el canal SDA
	except:
		None
def factorPotencia(pw):
	tabla = {100: 0, 95: 1.196, 90: 1.707, 85: 2.11, 80: 2.46, 75: 2.778, 
	70: 3.075, 65: 3.3582, 60: 3.6328, 55: 3.901, 50: 4.1666, 45: 4.4322, 
	40: 4.701, 35: 4.975, 30: 5.258, 25: 5.5555, 20: 5.8739, 15: 6.2235, 
	10: 6.626, 5: 7.137, 0: 8.33}
	for i in range(0, 100, 5):
		if (i <= pw <= (i+5)):
			pw = (((tabla[i+5] - tabla[i])/5)*(pw-i)) + tabla[i]
			break
	return pw

def RADIADOR(potencia):
	pot = float(potencia)
	pw = factorPotencia(pot)
	escribePotencia(pw)
	print("La potencia del radiador es de: ",pot)
	GPIO.output(10, GPIO.LOW)
	