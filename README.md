# gpioOSC
####raspberry pi GPIO interrupt to OSC in python  

OSC callback attached to a interrupt detection (ex:button press) on a GPIO input from raspberry pi


### Installation

#### dependencies

* python 3.6+
* [python-osc](https://github.com/attwad/python-osc)
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

```
pip install python-osc
pip install RPi.GPIO
```

#### Install rpi-interuptOsc
from a command line : clone the program to your favorite directory  (~/src/rpi-interuptOsc)

```
cd ~/

mkdir src && cd src

git clone https://github.com/gllmAR/rpi-gpioOSC.git

cd rpi-interuptOsc

./install.sh
```

### Usage
Run from terminal

`sudo python gpioOSC.py`

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
sudo python gpioOSC.py -g 0 -i 23 -d 127.0.0.1 -p 9999 -o /gpioOSC -b 200 -r 2 -t 0 -D 1


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
                        trigger mode (0= READING, 1=FALLING, 2=RISING, 3=BOTH)
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
