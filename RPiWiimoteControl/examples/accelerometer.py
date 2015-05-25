#!/usr/bin/env python

import cwiid
import time
x = 0.05

print('Press button 1 + 2 on your Wii Remote...\n')
time.sleep(1)

wm=cwiid.Wiimote()
print('Wii Remote connected...    ...LED should be on...')
wm.led = 1
print('\nPress the PLUS button to disconnect the Wii Remote and end the application.\n')
time.sleep(1)
print('Hold your Wii Remote like this...')
print(' ___________________________________________')
print('|      _            (+)                     |')
print('|   __| |__   ___             _      _      |')
print('|  |__   __| (_A_)  ()       (1)    (2)     |')
print('|     |_|                                   |')
print('|()_________________(|)_____________________|\n')
time.sleep(1)
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

def main():
	time.sleep(x)
	while True:
	
		# If button 2 is pressed...
		#if wm.state['buttons'] == 1:
			#print('Button 2 pressed'
			#time.sleep(x)
			
		# If button 1 is pressed...
		#if wm.state['buttons'] == 2:
			#print('Button 1 pressed'
			#time.sleep(x)
			
		# If Wii Remote is tilted Forward...
		if wm.state['acc'][0] > 140:
			print('tilted Forward...')
			time.sleep(x)
			
		# If Wii Remote is tilted Backward...
		if wm.state['acc'][0] < 110:
			print('tilted Backward...')
			time.sleep(x)
			
		# If Wii Remote is tilted Right...
		if wm.state['acc'][1] > 140:
			print('tilted Right...')
			time.sleep(x)
			
		# If Wii Remote is tilted Left...
		if wm.state['acc'][1] < 110:
			print('tilted Left...')
			time.sleep(x)
			
		# If + (Plus) is pressed...
		if wm.state['buttons'] == 4096:
			print('Keep holding + (Plus) to close Bluetooth connection...')
			time.sleep(1)
			if wm.state['buttons'] == 4096:
				print('Closing Bluetooth connection. Good Bye!')
				exit(wm)
				
		print(wm.state['acc'])

if __name__ == '__main__':
    main()
