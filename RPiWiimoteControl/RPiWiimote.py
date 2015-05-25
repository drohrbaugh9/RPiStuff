#-------------------------------------------------------------------------------
# Name:        RPiWiimote
# Purpose:     Control RPi with Wii Remote
#
# Original Author:     Brian Hensley
# Modified by:         David Rohrbaugh
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import cwiid
import time
x = 0.05

print('Press button 1 + 2 on your Wii Remote...\n')
time.sleep(1)

wm = cwiid.Wiimote()
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
# print('Controls:\nbutton 2: Decrease altitude\n+ControlPad: Increase altitude\ntilt Forward: move Forward\ntilt Backward: move Backward\ntilt Right: move Right\ntilt Left: move Left\n'
print('Controls:\nbutton 2: Down\n+ControlPad: Up\ntilt Forward: Forward\ntilt Backward: Backward\ntilt Right: Right\ntilt Left: Left\n')

print('Battery: ' + int(100.0 * wm.state['battery'] / cwiid.BATTERY_MAX))

wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

def main():
	time.sleep(x)
	Paused = False
	
	while True:
		if not Paused:
			# If button 2 is pressed...
			if wm.state['buttons'] == 1:
				print('moving Down...')
				time.sleep(x)
				
			# If +ControlPad is pressed...
			if wm.state['buttons'] == 256 or wm.state['buttons'] == 512 or wm.state['buttons'] == 1024 or wm.state['buttons'] == 1280 or wm.state['buttons'] == 1536 or wm.state['buttons'] == 2048 or wm.state['buttons'] == 2304 or wm.state['buttons'] == 2560:
				print('moving Up...')
				time.sleep(x)
				
			# If Wii Remote is tilted Forward...
			if wm.state['acc'][0] > 140:
				print('moving Forward')
				time.sleep(x)
				
			# If Wii Remote is tilted Backward...
			if wm.state['acc'][0] < 110:
				print('moving Backward...')
				time.sleep(x)
				
			# If Wii Remote is tilted Right...
			if wm.state['acc'][1] > 140:
				print('moving Right...')
				time.sleep(x)
				
			# If Wii Remote is tilted Left...
			if wm.state['acc'][1] < 110:
				print('moving Left...')
				time.sleep(x)

		# If - (Minus) button is pressed...
		if wm.state['buttons'] == 16:
			if Paused == False:
				print('*************************************Paused*************************************')
				Paused = True
			elif Paused:
				print('************************************Unpaused************************************')
				Paused = False
			time.sleep(1)
			
		# If Home button is pressed
		if wm.state['buttons'] == 128:
			print('Battery: ' + int(100.0 * wm.state['battery'] / cwiid.BATTERY_MAX))
			time.sleep(x)
			
		# If + (Plus) button is pressed...
		if wm.state['buttons'] == 4096:
			print('Keep holding + (Plus) to close Bluetooth connection...')
			time.sleep(1)
			if wm.state['buttons'] == 4096:
				print('Closing Bluetooth connection. Good Bye!')
				exit(wm)

if __name__ == '__main__':
    main()