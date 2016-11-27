import pandas as pd
import numpy as np
import random
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
import progressbar
from nltk import NaiveBayesClassifier, classify

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

def train(features, sample_proportion):
	train_size = int(len(features) * sample_proportion)
	train_set, test_set = features[:train_size], features[train_size:]
	print 'Training set size = ' + str(len(train_set)) + ' sms'
	print 'Test set size = ' + str(len(test_set)) + ' sms'
	# train the classifier
	classifier = NaiveBayesClassifier.train(train_set)
	return train_set, test_set, classifier

def evaluate(train_set, test_set, classifier):
	print "Accuracy on the training set = " + str(classify.accuracy(classifier, train_set))
	print "Accuracy on the test set = " + str(classify.accuracy(classifier, test_set))
	classifier.show_most_informative_features(20)

if __name__ == "__main__":
	data = pd.read_table('../smsSpam/smsspamcollection/SMSSpamCollection', 
		delimiter='\t', 
		names=['Label', 'Message'])

	print "The length of the dataset is: " + str(len(data))

	x = data.Message
	y = data.Label

	all_features = []
	bar = progressbar.ProgressBar()
	for n in bar(range(len(data))):
		feat = get_features(unicode(data.Message[n], errors='replace'), 'bow')
		# There is character problem in the dataset, encoding problem
		all_features.append([feat, data.Label[n]])
	train_set, test_set, classifier = train(all_features, 0.8)
	#Evaluate..............89%...............
	evaluate(train_set, test_set, classifier)