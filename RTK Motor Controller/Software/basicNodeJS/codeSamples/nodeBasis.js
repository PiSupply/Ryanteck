/*
 * RTK-000-003 Node.js and Cylon Basis
 * Licensed under the GNU GPL V3 License
 * (C) Seravo Oy 2014
 * Contributors: Otto Kekäläinen
*/

/*
 * GPIO pin configuration:
 * 11 = right wheel forwards (BCM 17)
 * 12 = right wheel backwards (BCM 18)
 * 15 = left wheel forwards (BCM 22)
 * 16 = left wheel backwards (BCM 23)
 *
 * See also http://cylonjs.com/documentation/platforms/raspberry-pi/
*/

var Cylon = require('cylon');

Cylon.robot({
  connection: {
    name: 'raspi',
    adaptor: 'raspi'
  },
  devices: [
    {
      name: 'rwheelf',
      driver: 'led',
      pin: 11
    },
    {
      name: 'rwheelb',
      driver: 'led',
      pin: 12
    },
    {
      name: 'lwheelf',
      driver: 'led',
      pin: 15
    },
    {
      name: 'lwheelb',
      driver: 'led',
      pin: 16
    },
  ],
  work: function(my) {

    after((0).seconds(), function() {
    my.rwheelf.turnOn();
    my.lwheelf.turnOn();
      console.log('Driving RTK-000-003 forwards for 30 seconds unless aborted with Ctrl+C.')
    });

    after((30).seconds(), function() {
      my.rwheelf.turnOff();
      my.lwheelf.turnOff();
      console.log('Stopped RTK-000-003.')
    });

  }
}).start();

