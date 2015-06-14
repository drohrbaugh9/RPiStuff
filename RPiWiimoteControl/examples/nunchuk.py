#!/usr/bin/env python

# Nunchuk stick values [0, 1]:
#  middle:  [128, 128]
#  up:      [128, 223]
#  down:    [128, 29]
#  right:   [227, 128]
#  left:    [29, 128]

import time
import cwiid
import math
import turtle
turtle.setup(100, 100)
c = 8

screen = turtle.Screen()
#screen.colormode(255)
t = turtle.Turtle()
t.shape("blank")
t.penup()
t.sety(-18)
t.pendown()

h = 22.5
for i in range(0, 360, 45):
    t.setheading(h + i)
    t.forward(14)

n = turtle.Turtle()
n.shape("circle")
n.penup()
n.speed(0)

print('Press button 1 + 2 on your Wii Remote...\n')
time.sleep(1)

wm = cwiid.Wiimote()
print('Wii Remote connected...    ...LED should be on...')
wm.led = 1
print('\nPress the PLUS button to disconnect the Wii Remote and end the application.\n')
time.sleep(1)
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_NUNCHUK

def updateTurtle():
    n.setx(((wm.state['nunchuk']['stick'][0] - 128) / c) + 1)
    n.sety((wm.state['nunchuk']['stick'][1] - 128) / c)

def main():
	time.sleep(0.05)
	while True:
                
		# If button 2 is pressed...
		if wm.state['buttons'] == 1:
			print('Button 2 pressed')
			
		# If button 1 is pressed...
		if wm.state['buttons'] == 2:
			print('Button 1 pressed')
			
		# If + (Plus) is pressed...
		if wm.state['buttons'] == 4096:
			print('Keep holding + (Plus) to close Bluetooth connection...')
			time.sleep(1)
			if wm.state['buttons'] == 4096:
				print('Closing Bluetooth connection. Good Bye!')
				exit(wm)
				
		time.sleep(0.05)
		print('buttons:       ' + str(wm.state['nunchuk']['buttons']))
		print('stick:         ' + str(wm.state['nunchuk']['stick']))
                print('accelerometer: ' + str(wm.state['nunchuk']['acc']))
		updateTurtle()
                         
if __name__ == '__main__':
    main()
