#If you have the kbHit file in the same folder as this python script you can remove these 5 lines.
import os, sys, inspect
import paramiko
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

#NOTE!!!
#When the streams have the Xp30 / Xp60 format this doesn't work. Will look into this.

import kbhit
import jsonTest
import time

def cls():
	print "\n" * 100

#Update these if needed
username = ''
password = ''
#IP Adress
hostname = ''
#Paste your auth key here
authKey = ''

cls()
print "TESTING MENU"
print "1: To view top streamer currently on twitch.tv"
print "2: To following WIP"
arg = input(": ")

'''
Need to fix this bug.
[cli][info] Available streams:
'''


if arg == 1:
	cls()
	print "Fetching current top streamers..."
	jsonTest.fetchTopStreamer()
	arg = input(": ")
	url, streamer = jsonTest.chooseTopStreamer(arg)
elif arg == 2:
	print "Fetching streamer you're following"
	jsonTest.fetchFollowing()
	arg = input(": ")
	url, streamer = jsonTest.chooseFollowingStreamer(arg)
else: 
	print "Error"
	exit()

#streamer = str(sys.argv[1])
kb = kbhit.KBHit()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
	print "Conntecting to RPi.."
	ssh.connect(hostname, username=username, password=password)
	print "Connection established"
except paramiko.SSHException:
	print "Connection Failed"
	quit()

stdin, stdout, stderr = ssh.exec_command("livestreamer " + url + " high -np'omxplayer -o hdmi' --twitch-oauth-token " + authKey)
print "Opening " + streamer
print "Give it a few seconds..."
print "Press any key to close the stream"

while not kb.kbhit():
	time.sleep(0.5)
#Kills the mediaplayer
ssh.exec_command("killall omxplayer.bin")

kb.set_normal_term()