# This is class of K-Nearest Neighbor Classifier

import numpy as np
from collections import Counter

class KNN_Classifier(object):
	
	def __init__(self,k,trainingSet,labels):

		self.k            = k           # number of neighbors
		self.trainingSet  = trainingSet # training set 
		self.labels       = labels      # labels of the training set

	def predictLabel(self,inputs):

		distance = np.zeros([self.trainingSet.shape[0],self.trainingSet.shape[1]])

		for j in xrange(0,self.trainingSet.shape[1]):

			for k in xrange(0,self.trainingSet.shape[0]):

				distance[k,j] = ( inputs[k] - self.trainingSet[k,j] ) ** 2

		distanceMean = np.zeros([self.trainingSet.shape[1]])
		distLabels   = np.vstack([distanceMean,self.labels])

		for j in xrange(0,self.trainingSet.shape[1]):

			distLabels[0,j] = np.mean(distance[0:distance.shape[0],j])

		sortedLabels   = distLabels[1,distLabels[0,:].argsort()]
		kLabels        = sortedLabels[0:self.k]
		dataCount      = Counter(kLabels.tolist())
		predictedLabel = int( dataCount.most_common()[0][0] )

		return predictedLabel


