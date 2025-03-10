from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)   # Set GPIO48 to output for NeoPixel
neo = NeoPixel(pin, 1)   # Create NeoPixel driver on GPIO48 for 1 pixel

colors = [(110, 220, 220),   # Red
          (0, 0, 0),   # Green
          (130, 340, 230)]   # Blue

while True:
    for color in colors:
        neo[0] = color  # Set the pixel to the current color
        neo.write()      # Write data to the NeoPixel
        time.sleep(0.3)  # Wait for 0.5 seconds before changing color

#This is our second lab for iot in this lab we imported 2 python libraries and used them to change the led status 
    