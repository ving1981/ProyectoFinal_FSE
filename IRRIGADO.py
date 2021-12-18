#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# IRRIGADO.py
#
#___________________________________________________
# Authors: 
#           Marín Jiménez Irving
#           Salas Garcia Alejandra
#___________________________________________________
# License: MIT
#
# ## ###############################################

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up pin no. 10 as output and default it to low
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

#apaga y enciede irrigación 
def IRRIGACION(status):
    if (status == "ON"):          
        GPIO.output(10, GPIO.HIGH) #Enciende valvula para la Irrigación
        print("IRRIGACION ENCENDIDA")
    if (status == "OFF"):    
        GPIO.output(10, GPIO.LOW)# Apaga valvula para la Irrigación
        print("IRRIGACION APAGADA")#mensaje apagado