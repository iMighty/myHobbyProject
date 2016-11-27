#Using twitch API to fetch current top most viewers on twitch.tv or the streamers you follow

# v1.1	Fixed an error that occurs when a streamer has undefined characters
# v1.2 	Added a progressbar, also there is a notification function. None of these are fully tested yet aka. 
# 		not implemented not working

import requests, os, json
from pync import Notifier
import progressbar


topStreamerList = []
topUser = []
topStatus = []
followingList = []
followingUser = []
followingStatus = []
#Add your unique key
auth_key = 'q2rcoimmqi7m95tozjqnw9aqk00vkk'
check = False
	
def fetchTopStreamer():
	r = requests.get('https://api.twitch.tv/kraken/streams?oauth_token=' + auth_key)
	jsonData = r.json()
	i = 0
	for item in jsonData['streams']:
		try:
			print str(i) + "." + item['channel']['display_name'] + " is currently playing " + item['game'] + ". Viewers: " + str(item['viewers'])
			i += 1
		#print item['channel']['url']
			topStreamerList.append(item['channel']['url'])
			topUser.append(item['channel']['display_name'])
			topStatus.append(item['channel']['status'])
		except UnicodeEncodeError:
			print str(i) + ". Streamer is playing " + item['game'] + ". Viewers: " + str(item['viewers'])
	'''
	for i in range(len(streamerList)):
		print streamerList[i]
	'''

def checkFollowing():
	global check
	if not check:
		fetchFollowing()
		check = True
	else:
		r = requests.get('https://api.twitch.tv/kraken/streams/followed?oauth_token=' + auth_key)
		jsonData = r.json()
		for item in jsonData['streams']:
			for n in range(len(followingUser)):
				if not item['channel']['display_name'] == followingUser[n]:
					# NOTIFY THE USER THAT A NEW STREAMER HAS COME ONLINE
					newStreamer = item['channel']['url']
					# Somehow change 
					Notifier.notify(newStream + " is online", 
						sound="default", 
						title="twitchTVRPI", 
						appIcon="kyckling.jpg",
						open="twitch.tv/" + newStreamer)

def chooseTopStreamer(arg):
	return topStreamerList[arg], topUser[arg], topStatus[arg]
'''
fetchTopStreamer()
arg = input(": ")
print chooseStreamer(arg)
'''

def fetchFollowing():
	global check
	r = requests.get('https://api.twitch.tv/kraken/streams/followed?oauth_token=' + auth_key)
	jsonData = r.json()
	i = 0
	for item in jsonData['streams']:
		try:
			if not check:
				print str(i) + "." + item['channel']['display_name'] + " is currently playing " + item['game'] + ". Viewers: " + str(item['viewers'])
				i += 1
			followingList.append(item['channel']['url'])
			followingUser.append(item['channel']['display_name'])
			followingStatus.append(item['channel']['status'])
		except UnicodeEncodeError:
			if not check:
				print str(i) + ". Streamer is playing " + item['game'] + ". Viewers: " + str(item['viewers'])
			else:
				pass

def chooseFollowingStreamer(arg):
	return followingList[arg], followingUser[arg], followingStatus[arg]
