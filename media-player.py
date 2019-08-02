#!/usr/bin/python3

import os
import datetime
from time import sleep

import glob

# THIS WILL GIVE TIME TO RPI4 TO MOUNT ALL USB STORAGES
sleep(10)

# PATH FOR MOUNT DIRECTORY OF USB STORAGES
usb_folders = os.listdir('/media/pi/')

os.system('unclutter -idle 3 & ')

try:
	# READING ALL USB STORAGE CONNECT
	for pen in usb_folders:

		if os.path.isfile('/media/pi/%s/dev.txt' % (pen)):
			raise Exception('Scrip will stop! Dev Mode Activated by USB Storage');

		# LISTING ALL MP4 ON ROOT OF THAT USB STORAGE
		usb_files = glob.glob('/media/pi/%s/*.mp4' % (pen))

		# IF THE PRESENT USB STORAGE HAS A MP4 ON THERE ROOT, IT WILL STUCK IN THIS WHILE RPI4 IS TURN ON
		if len(usb_files) > 0:
			# LOOPING IN THIS LIST OF MP4
			while True:
				for file in usb_files:
					# PLAYING MP4 ONE BY ONE
					os.system('omxplayer -o local "%s"' % file)

	# IF DOESN'T EXIST ANY USB STORAGE, IT WILL PLAY A DEFAULT MP4 STORAGE IN VIDEOS FOLDER OF PI USER
	os.system('omxplayer -o local --loop "/home/pi/Videos/default.mp4"')

except Exception as e:
	print(e)
