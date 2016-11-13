#Using twitch API to fetch current top most viewers on twitch.tv or the streamers you follow

import requests, os, json

followingList = []
topStreamerList = []
topUser = []
followingUser = []
auth_key = 'q2rcoimmqi7m95tozjqnw9aqk00vkk'

	
def fetchTopStreamer():
	r = requests.get('https://api.twitch.tv/kraken/streams?oauth_token=' + auth_key)
	jsonData = r.json()
	i = 0
	for item in jsonData['streams']:
		print str(i) + "." + item['channel']['display_name'] + " is currently playing " + item['game'] + ". Viewers: " + str(item['viewers'])
		i += 1
	#print item['channel']['url']
		topStreamerList.append(item['channel']['url'])
		topUser.append(item['channel']['display_name'])
	'''
	for i in range(len(streamerList)):
		print streamerList[i]
	'''
def chooseTopStreamer(arg):
	return topStreamerList[arg], topUser[arg]
'''
fetchTopStreamer()
arg = input(": ")
print chooseStreamer(arg)
'''

def fetchFollowing():
	r = requests.get('https://api.twitch.tv/kraken/streams/followed?oauth_token=' + auth_key)
	jsonData = r.json()
	i = 0
	for item in jsonData['streams']:
		print str(i) + "." + item['channel']['display_name'] + " is currently playing " + item['game'] + ". Viewers: " + str(item['viewers'])
		i += 1
		followingList.append(item['channel']['url'])
		followingUser.append(item['channel']['display_name'])

def chooseFollowingStreamer(arg):
	return followingList[arg], followingUser[arg]