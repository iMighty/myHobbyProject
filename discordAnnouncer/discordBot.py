# Written by Robin =3

import discord
import asyncio
from datetime import datetime
import ttsPython

token = 'MzExMDUyMzg5MTg2NjY2NTA2.C_HB7Q.dTi64HQfH5xqXnmoMRnpbAOYijA'
testChannelID = '311058462673076225' # NEED TO BE DYNAMIC
channelID = '256081079608279041'
testVoiceChannelID = '311058462673076226'
voiceChannelID = '256081079608279042'
voice = None
client = discord.Client()
lang = 'en'
supportedLang = ['en', 'en-us', 'ja']

print("Checking if opus is loaded...")
if not discord.opus.is_loaded():
	print("Opus not loaded, loading Opus...")
	discord.opus.load_opus('opus')
	print("Opus loaded...")
else:
	print("Opus is loaded...")


async def joinVoice():
	print("Attempting to join channel")
	global voice 
	voice = await client.join_voice_channel(client.get_channel(voiceChannelID))

async def playVoice():
	player = voice.create_ffmpeg_player('tmp.mp3')
	player.start()
	while player.is_playing():
		pass


@client.event
async def on_message(message):
	if message.content.startswith('!change'):
		content = message.content
		tokens = str.split(content)
		if len(tokens) == 2:
			if tokens[1] in supportedLang:
				global lang
				await client.send_message(client.get_channel(channelID), 'Language changed from ' + lang + " to " + tokens[1])
				lang = tokens[1]
			elif tokens[1] == 'current':
				await client.send_message(client.get_channel(channelID), 'My current language is set to ' + lang)
			else:
				await client.send_message(client.get_channel(channelID), 'Error: argument unknown')
		else:
			pass

		
		
@client.event
async def on_voice_state_update(before, after):
	mode = ['en', 'en-au', 'en-us', 'en-uk', 'ja']
	n = 2
	if after.voice.mute:
		await client.send_message(client.get_channel(channelID), '{0.display_name}'.format(after) + ' has been muted')
		pass
	if not(after.name == 'AnnouncerForChannels' or after.voice.self_mute):
		# LEAVING
		if after.voice.voice_channel is None:
			#await client.send_message(client.get_channel(channelID), '{0.display_name}'.format(after) + ' has left the channel')
			#ttsPython.generateAudio('{0.display_name}'.format(after) + ' san chaneru o satta', 'ja')
			ttsPython.generateAudio('{0.display_name}'.format(after) + ' left', lang)
			await playVoice()
		# ENTERING
		elif after.name == 'Spycrab':
			ttsPython.generateAudio('Kiirotori ' + 'san chaneru o satta', 'ja')
			await playVoice()
		else:
			#await client.send_message(client.get_channel(channelID), '{0.display_name}'.format(before) + ' has joined channel')
			#ttsPython.generateAudio('{0.display_name}'.format(before) + ' san chaneru ni sanka shimashita', 'ja')
			ttsPython.generateAudio('{0.display_name}'.format(before) + ' joined', lang)
			await playVoice()


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(datetime.now())
	print('------')
	await joinVoice()


client.run(token)