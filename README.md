# rpi-interuptOsc
####raspberry pi GPIO interrupt to OSC in python  

OSC callback attached to a interrupt detection (ex:button press) on a GPIO input from raspberry pi


### Installation


#### Install the Dependencies
python 2.7,  python-rpi.gpio and pyOSC

```
sudo apt-get update && sudo apt-get install python-rpi.gpio
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install pyOSC

```


#### Install rpi-interuptOsc
from a command line : clone the program to your favorite directory  (~/src/rpi-interuptOsc)

```
cd ~/

mkdir src && cd src

git clone https://github.com/gllmAR/rpi-interuptOsc.git

cd rpi-interuptOsc

```

### Usage
Run from terminal

`sudo python interuptOsc.py`

You should see the default parameters :
```
RPI Gpio interrupt OSC
destination Address: 127.0.0.1
outputPort: 9999
InputPin: 23
gpioBoard: GPIO.BCM
oscPath: /gpioOSC
bouncetime: 200
resistance: GPIO.PUD_DOWN
trigger: GPIO.FALLING
Debug: 1
```

these parameters correspond to this line :

```
sudo python interuptOsc.py -g 0 -i 23 -d 127.0.0.1 -p 9999 -o /gpioOSC -b 200 -r 2 -t 0 -D 1


```

#### Options:
`python interuptOsc.py --help` return :
```
RPI Gpio interrupt OSC

optional arguments:
  -h, --help            show this help message and exit
  -g GPIOBOARD, --gpioBoard GPIOBOARD
                        gpio Board Mode (0=GPIO.BCM, 1=GPIO.BOARD)
  -i INPUTPIN, --inputPin INPUTPIN
                        input Pin
  -d DESTINATION, --destination DESTINATION
                        destination ip address
  -p OUTPUTPORT, --outputPort OUTPUTPORT
                        Output Port
  -o OSCPATH, --oscPath OSCPATH
                        Osc path
  -b BOUNCETIME, --bouncetime BOUNCETIME
                        (de)bouncetime
  -r RESISTANCE, --resistance RESISTANCE
                        pull_up_down resistance (0=off, 1=pullUp, 2=pullDown)
  -t TRIGGER, --trigger TRIGGER
                        trigger mode (0=FALLING, 1=RISING, 2=BOTH)
  -D DEBUG, --Debug DEBUG
                        Debug mode on

```

### todo

* multi pin,





### Usefull Links

[http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio](http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio)



[http://raspi.tv/2014/rpi-gpio-update-and-detecting-both-rising-and-falling-edges](http://raspi.tv/2014/rpi-gpio-update-and-detecting-both-rising-and-falling-edges)



[http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/](http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/)




[http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering](http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering)


[http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/](http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/)
