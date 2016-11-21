import pandas as pd
import numpy as np
import random
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

stoplist = stopwords.words('english')

def preprocess(sentence):
	lemmatizer = WordNetLemmatizer()
	return [lemmatizer.lemmatize(word.lower()) \
		for word in word_tokenize(sentence) \
		if not word in stoplist]

def get_features(text, settings):
	if settings == 'bow':
		return {word: count \
			for word, count in Counter(preprocess(text)).items() \
			if not word in stoplist}
	else:
		return {word: True \
			for word, count in Counter(preprocess(text)).items() \
			if not word in stoplist}

data = pd.read_table('../smsSpam/smsspamcollection/SMSSpamCollection', 
	delimiter='\t', 
	names=['Label', 'Message'])

print "The length of the dataset is: " + str(len(data))

x = data.Message
y = data.Label

all_features = []

for n in range(len(data)):
	feat = get_features(data.Message[n], 'bow')
	# There is character problem in the dataset
	all_features.append([feat, data.Label[n]])