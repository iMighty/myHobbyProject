from gtts import gTTS
import os
from tempfile import TemporaryFile

def generateAudio(str, lang):
	tts = gTTS(text=str, lang=lang, slow=False)
	tts.save("tmp.mp3")
	# print("File generated")
