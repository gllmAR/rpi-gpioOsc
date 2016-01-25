#!/usr/bin/env python2.7

import sys
import RPi.GPIO as GPIO
import time

print("sys.version:")
print(sys.version + "\n")

print("GPIO.VERSION: " + GPIO.VERSION)
print("GPIO.RPI_INFO['P1_REVISION'] = " + str(GPIO.RPI_INFO['P1_REVISION']));

inputPin = 23


GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


print("Press button to turn ON LED");
try:
    while(True):
        if (GPIO.input(inputPin)):

            print("in")
        else:

            print("out")

except KeyboardInterrupt:
    print ("\n")
    print ("Exit by KeyboardInterrupt\n")

except:
    print ("\n")
    print ("Exit by Other case!\n")

finally:
    GPIO.cleanup(inputPin)
    print ("Clean up GPIO\n")
