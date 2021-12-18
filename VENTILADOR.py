#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# VENTILADOR.py
#___________________________________________________
# Author: 
#           Marín Jiménez Irving
#           Salas Garcia Alejandra
#___________________________________________________
# License: MIT
#
# ## ###############################################
# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
import threading
#Importamos sleep
from time import sleep
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Configurando los pins de salida como bajos por defecto
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) #Ventilador por pwm
pwm = GPIO.PWM(12, 1)

def inicia(potencia):
	pot = int(potencia)
	continua = verifica(potencia)
	pwm.start(0)
	if(continua == False):
		print("OFF")
		pwm.stop()
	else:
		try:
			while (continua ):
				print("Ventilador: ON")
				print(pot)
				pwm.ChangeDutyCycle(pot)
				time.sleep(0.2)
				
		except:
			pwm.ChangeDutyCycle(0)
	#pwm.stop()
	# Reset all ports to its default state (inputs)
	GPIO.cleanup()	

def verifica(potencia):
	pot = int(potencia)
	if (pot == 0):
		continua = False
	else:
		continua = True
	return continua

def VENTILADOR(potencia):
	h1 = threading.Thread(target = inicia, args = (potencia,))
	h2 = threading.Thread(target = verifica, args = (potencia,))
	print("La potencia del ventilador es de: ",potencia)
	h1.start()
	h2.start()
