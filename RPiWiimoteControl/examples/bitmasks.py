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
wm.rpt_mode = cwiid.RPT_BTN

def main():
	time.sleep(x)
	while True:
	
		# If button 2 is pressed...
		if wm.state['buttons'] & 1:
			print('2 pressed')
		
		# If button 1 is pressed...
		if wm.state['buttons'] & 2:
			print('1 pressed')
		
		if wm.state['buttons'] & 0x0F00: # (2048 | 1024 | 512 | 256) = 0x0F00
			print('dpad pressed')
		
		if wm.state['buttons'] & 0x1F9F: # better than checking state != 0 IMO
			print('any pressed')
			
		# If + (Plus) is pressed...
		if wm.state['buttons'] == 4096:
			print('Keep holding + (Plus) to close Bluetooth connection...')
			time.sleep(1)
			if wm.state['buttons'] == 4096:
				print('Closing Bluetooth connection. Good Bye!')
				exit(wm)
				
		time.sleep(x)

if __name__ == '__main__':
    main()
