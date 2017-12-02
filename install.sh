#!/bin/bash
echo "linking rpi-gpioOsc to /usr/local/bin"
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null

sudo cp  $SCRIPTPATH/gpioOSC.py /usr/local/bin/gpioOsc.py
echo "setting execute permission"
sudo chmod +x /usr/local/bin/gpioOsc.py
