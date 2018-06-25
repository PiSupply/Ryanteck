# Programming the RTK-000-001 / RTK-000-003 using Node.js #

In this tutorial we will be showing you how to program your RTK-000-001 Motor Contoller to move around two motors for robots including the RTK-000-003 Budget Robotics Kit

## Creating the basis ##

First install 0.10 on newer version of Node.js and the Cylon modules:

```
# Raspbian-compatible version of Node (source http://weworkweplay.com/play/raspberry-pi-nodejs/)
wget http://node-arm.herokuapp.com/node_latest_armhf.deb
sudo dpkg -i node_latest_armhf.deb

# Install Cylon.js with Raspberry Pi compatibility
npm install cylon cylon-gpio cylon-raspi
```


## Run the basis ##

Download example script and run as root to have access to the GPIO interface:
```
wget https://raw.githubusercontent.com/RyanteckLTD/RTK-000-003/master/basicNodeJS/codeSamples/nodeBasis.py
sudo node nodeBasis.js
```

Cylon.js documentation mentions stuff about configuring I2C drivers and others, but for this example fiddling with any kernel modules or additional controller software is not required.

