import RPi.GPIO as GPIO
import time
import sys


def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)


def loop():
        option = input()
        if option == "e":
            GPIO.output(18,True)
        if option == "a":
            GPIO.output(18,False)


setup()
while True:
        loop()