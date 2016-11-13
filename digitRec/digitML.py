import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()

#print digits.images[0]

images_and_labels = list(zip(digits.images, digits.target))

n_samples = len(digits.images)

data = digits.images.reshape((n_samples, -1))

classifier = svm.SVC(gamma=0.001)
#Uses first halve of the data to train
classifier.fit(data[:n_samples/2], digits.target[:n_samples / 2])
#The rest of data as testing data
expected = digits.target[n_samples/2:]
predicted = classifier.predict(data[n_samples/2:])

print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))

plt.imshow(digits.images[0], cmap=plt.cm.gray, interpolation='nearest')
plt.show()