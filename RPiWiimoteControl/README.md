RPiWiimoteControl
=================
RPiWiimote.py is based off Brian Hensley's [wiimotetest.py](https://sites.google.com/site/brianhensleyfiles/wiimotetest.py). It is in a prototype stage right now, but I will use at some point.

This code makes use of abstrakraft's [cwiid](http://abstrakraft.org/cwiid) library. It is available [here](https://github.com/abstrakraft/cwiid) on GitHub.

This code uses these values for the buttons on the Wiimote:
<p align="center">
  <img src="https://raw.githubusercontent.com/drohrbaugh9/RPiStuff/master/RPiWiimoteControl/examples/diagram.png" alt="Diagram of Wiimote buttons. This image is in the repository."/>
</p>
This code also uses these axes when reporting accelerometer data:
<p align="center">
  <img src="https://raw.githubusercontent.com/drohrbaugh9/RPiStuff/master/RPiWiimoteControl/examples/wiimote_axes.png" alt="Diagram of Wiimote axes. This image is in the repository."/>
</p>

This repository also includes [example code](https://github.com/drohrbaugh9/RPiStuff/tree/master/RPiWiimoteControl/examples) for using the built-in [accelerometer](https://github.com/drohrbaugh9/RPiStuff/blob/master/RPiWiimoteControl/examples/accelerometer.py) and the  [nunchuk](https://github.com/drohrbaugh9/RPiStuff/blob/master/RPiWiimoteControl/examples/nunchuk.py), [MotionPlus](https://github.com/drohrbaugh9/RPiStuff/blob/master/RPiWiimoteControl/examples/motionplus.py), and [Classic Controller](https://github.com/drohrbaugh9/RPiStuff/blob/master/RPiWiimoteControl/examples/classicController.py) accessories with cwiid.

(Assuming you have a Raspberry Pi) Follow the instructions at Mr. Hensley's website [here](http://www.brianhensley.net/2012/08/wii-controller-raspberry-pi-python.html). After the step in which you install python-cwiid, you can just use RPiWiimote.py.

A good example of all you can do with cwiid is [sguernion's](https://github.com/sguernion) [wiimote.py](https://github.com/sguernion/myPI/blob/07927754376d677f14e363a2549d1ecef65e56e5/serveur/python/wii/wiimote.py). This code does not, however, use the MotionPlus extension. For this, the [MotionPlus page](http://abstrakraft.org/cwiid/wiki/MotionPlus) on the cwiid website is helpful.
