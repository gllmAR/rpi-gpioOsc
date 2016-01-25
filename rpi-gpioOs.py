#!/usr/bin/env python2.7

## RPI Gpio interrupt OSC ##
## v0.02 ##
## gllmar 2015 ##


import OSC              #de pyosc
import RPi.GPIO as GPIO
import time
import argparse
import errno
import datetime
import sys

__author__ = 'gllmAr'

# gestion des arguments
parser = argparse.ArgumentParser(description='RPI Gpio interrupt OSC')

parser.add_argument('-g','--gpioBoard', help='gpio Board Mode (0=GPIO.BCM, 1=GPIO.BOARD)', default='0', type=int)
parser.add_argument('-i','--inputPin', help='input Pin', default='23', type=int)
parser.add_argument('-d','--destination',help='destination ip address', default='127.0.0.1')
parser.add_argument('-p','--outputPort', help='Output Port ', default='9999', type=int)
parser.add_argument('-o','--oscPath', help='Osc path', default='/gpioOSC')
parser.add_argument('-b','--bouncetime', help='(de)bouncetime', default='200', type=int)
parser.add_argument('-r','--resistance', help='pull_up_down resistance (0=off, 1=pullUp,  2=pullDown)', default='2', type=int)
parser.add_argument('-t','--trigger', help='trigger mode (0=FALLING, 1=RISING, 2=BOTH)', default='0', type=int)
parser.add_argument('-D','--Debug', help='Debug mode on ', default='1', type=int)

args = parser.parse_args()


# definir le callback,
# sera envoye dans un thread par la fonction gpio.add_event_detect
flag = 0 # quand un interrupt est detecte ajouter 1 et envoyer le message OSC
def flagUp(channel):
    global flag    # rendre la variable globale  (pas tres clair pourquoi ca ne communique pas )
    flag += 1      # incrementer de 1 a chaque interrupt


gpioBoardMode = "0"
#PUD_OFF, PUD_UP or PUD_DOWN
if args.gpioBoard == 0:
    gpioBoardMode = "GPIO.BCM"
    GPIO.setmode(GPIO.BCM)
elif args.gpioBoard == 1:
    gpioBoardMode = "GPIO.BOARD"
    GPIO.setmode(GPIO.BOARD)
else:
    print("gpioBoard number not valid(try 0/1)")
    sys.exit()


resistanceType = "0"
#PUD_OFF, PUD_UP or PUD_DOWN
if args.resistance == 0:
    resistanceType = "GPIO.PUD_OFF"
    GPIO.setup(args.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
elif args.resistance == 1:
    resistanceType = "GPIO.PUD_UP"
    GPIO.setup(args.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
elif args.resistance == 2:
    resistanceType = "GPIO.PUD_DOWN"
    GPIO.setup(args.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
else:
    print("resistance number not valid(try 0/1/2)")
    sys.exit()

triggerType = "0"
#GPIO.FALLING , GPIO.RISING, GPIO.BOTH
if args.trigger == 0:
    triggerType = "GPIO.FALLING"
    GPIO.add_event_detect(args.inputPin, GPIO.FALLING, callback=flagUp, bouncetime=args.bouncetime)
elif args.trigger == 1:
    triggerType = "GPIO.RISING"
    GPIO.add_event_detect(args.inputPin, GPIO.RISING, callback=flagUp, bouncetime=args.bouncetime)
elif args.trigger == 2:
    triggerType = "GPIO.BOTH"
    GPIO.add_event_detect(args.inputPin, GPIO.BOTH, callback=flagUp, bouncetime=args.bouncetime)
else:
    print("trigger number not valid(try 0/1/2)")
    sys.exit()



## Printer les arguments ##

print ("RPI Gpio interrupt OSC")
print ("destination Address: %s" % args.destination )
print ("outputPort: %s" % args.outputPort )
print ("InputPin: %s" % args.inputPin )
print ("gpioBoard: %s" % gpioBoardMode )
print ("oscPath: %s" % args.oscPath )
print ("bouncetime: %s" % args.bouncetime )
print ("resistance: %s" % resistanceType )
print ("trigger: %s" % triggerType )
print ("Debug: %s" % args.Debug )


## definir la fonction d envoi ##
c = OSC.OSCClient()

def sendOSC(value):
    try:
        c.connect((args.destination, args.outputPort))   # connection
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress(args.oscPath)
        oscmsg.append(1)
        c.send(oscmsg)
        if args.Debug:
            now = datetime.datetime.now()
            print now.isoformat()
    except OSC.OSCClientError:
        print "Connection Refused"


# une loop infinie sur le thread principale qui attend
# et qui envois si la variable change
try:
    while 1:
        if flag > 0:
            sendOSC(1)
            flag = 0
        time.sleep(.1)


# sortir du programme avec CTRL+C et cleaner le GPIO
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
