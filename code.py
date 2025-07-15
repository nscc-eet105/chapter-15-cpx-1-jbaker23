# My name is Jacob Baker and this is Chapter 15 CPX 1 being completed on July 15
import time
from adafruit_circuitplayground import cp

class Region:
    def __init__(self, color, leds):
        self.__color = color
        self.__leds = leds

    def set_color(self, color):
        self.__color = color

    def set_leds(self, leds):
        self.__leds = leds

    def get_color(self):
        return self.__color

    def get_leds(self):
        return self.__leds

    def all_on(self):
        for i in self.__leds:
            cp.pixels[i] = self.__color

    def all_off(self):
        for i in self.__leds:
            cp.pixels[i] = (0, 0, 0)




# === Create Region Objects ===
red = Region((255, 0, 0), (0, 1, 2))
blue = Region((0, 0, 255), (6, 7, 8))

# === Main Loop ===
while True:
    red.all_on()
    blue.all_on()
    time.sleep(0.5)
    red.all_off()
    blue.all_off()
    time.sleep(0.5)
