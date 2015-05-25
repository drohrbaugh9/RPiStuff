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
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_CLASSIC

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
			
		# If + (Plus) is pressed...
		if wm.state['buttons'] == 4096:
			print('Keep holding + (Plus) to close Bluetooth connection...')
			time.sleep(1)
			if wm.state['buttons'] == 4096:
				print('Closing Bluetooth connection. Good Bye!')
				exit(wm)
				
		time.sleep(x)
		print('buttons\n' + wm.state['classic']['buttons'])
		print('left stick\n' + wm.state['classic']['l_stick'])
		print('right stick\n' + wm.state['classic']['r_stick'])
		print('\n' + wm.state['classic']['l'])
		print('\n' + wm.state['classic']['r'])

if __name__ == '__main__':
    main()
