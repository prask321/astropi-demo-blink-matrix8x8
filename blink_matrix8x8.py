#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Arnauld Biganzoli pour la Compagnie du Code
@param aucun
@return: rien

Appeler ce script python depuis l'invite de commande
>>> python display.py

"""


import time
from sense_hat import SenseHat

sense = SenseHat()

red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
none = (0, 0, 0)

def color_screen(color):
	pixels = [color for i in range(64)]
	sense.set_pixels(pixels)

color_screen(none)
time.sleep(1)

color_screen(red)
time.sleep(2)

color_screen(green)
time.sleep(2)

color_screen(blue)
time.sleep(2)

# display temperature from HTS221 sensor
# http://www.farnell.com/datasheets/1836732.pdf
while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
