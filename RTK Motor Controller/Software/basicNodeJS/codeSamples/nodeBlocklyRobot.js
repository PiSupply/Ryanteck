/*
 * RTK-000-003 Node.js, Cylon.js and Async.js to support Blockly/code.org
 * style of syntax (moveForward(), turnLeft() etc..).
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
var async = require('async');

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

    function runStep(stepName, callback) {

      var delay = 1; // how many seconds to do each step

      switch (stepName) {
        case 'moveForward':
          my.rwheelf.turnOn();
          my.lwheelf.turnOn();
          after((delay).seconds(), function () {
            my.rwheelf.turnOff();
            my.lwheelf.turnOff();
            callback();
          });
          break;

        case 'moveBackward':
          my.rwheelb.turnOn();
          my.lwheelb.turnOn();
          after((delay).seconds(), function () {
            my.rwheelb.turnOff();
            my.lwheelb.turnOff();
            callback();
          });
          break;

        case 'turnLeft':
          my.rwheelf.turnOn();
          my.lwheelb.turnOn();
          after((delay).seconds(), function () {
            my.rwheelf.turnOff();
            my.lwheelb.turnOff();
            callback();
          });
          break;

        case 'turnRight':
          my.rwheelb.turnOn();
          my.lwheelf.turnOn();
          after((delay).seconds(), function () {
            my.rwheelb.turnOff();
            my.lwheelf.turnOff();
            callback();
          });
          break;

       }
    }

    function moveForward() {
      q.push({name: 'moveForward'});
    }

    function moveBackward() {
      q.push({name: 'moveBackward'});
    }

    function turnLeft() {
      q.push({name: 'turnLeft'});
    }

    function turnRight() {
      q.push({name: 'turnRight'});
    }

    // Create queue that processes one task at the time
    var q = async.queue(function (task, callback) {
      console.log(task.name);
      runStep(task.name, callback);
    }, 1);


    // assign a callbacks
    q.saturated = function() {
      console.log('Queue max concurrency.');
    }
    q.drain = function() {
      console.log('Program completed.');
    }



    // ** EDIT BELOW TO MAKE YOUR OWN MOVEMENT PATTERN **

    // Use same syntax for movement as in code.org tutorials and Blockly
    moveForward();
    moveBackward();
    turnLeft();
    turnRight();

    // ** EDIT ABOVE TO MAKE YOUR OWN MOVEMENT PATTERN **



    // Reset all pins, just to be sure
    my.rwheelf.turnOff();
    my.lwheelf.turnOff();
    my.rwheelb.turnOff();
    my.lwheelb.turnOff();

  }
}).start();

