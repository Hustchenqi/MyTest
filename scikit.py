import numpy as np 
import urllib

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data'

raw_data = urllib.urlopen(url)

dataset = np.loadtxt(raw_data,delimiter = ',')

X = dataset[:,0:7]
Y = dataset[:,8]
# data1 = open('Xfile.txt', 'w+')
# data2 = open('Yfile.txt', 'w+')

# data1.write(X)
# print (Y, data2)

# data1.close()
# data2.close()

from sklearn import preprocessing
normalized_X = preprocessing.normalize(X)
standardzed_X = preprocessing.scale(X)
print normalized_X
print standardzed_X

from sklearn import metrics
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X, Y)
print model

# expected = Y
# predicted = model.predict(X)

# print metrics.classification_report(expected, predicted)
# print metrics.confusion_matrix(expected, predicted)

