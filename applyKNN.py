
# apply KNN classifier

import numpy as np
import matplotlib.pyplot as plt
from KNN_Class import KNN_Classifier

# training data

featureOne   = []
featureTwo   = []
featureThree = []
featureFour  = []
labels       = []
numFeatures  = 4 # we have 4 features in this data set

with open('IrisDataSet.txt','r') as importedData:

	for line in importedData:

		featureOne.append(line[0:3])
		featureTwo.append(line[4:7])
		featureThree.append(line[8:11])
		featureFour.append(line[12:15])

		if line[21:25] == 'seto':

			labels.append(0)

		elif line[21:25] == 'vers':

			labels.append(1)

		else:

			labels.append(2)

labels = np.asarray(labels)

featureOneF   = np.zeros([1,len(featureOne)])
featureTwoF   = np.zeros([1,len(featureTwo)])
featureThreeF = np.zeros([1,len(featureThree)])
featureFourF  = np.zeros([1,len(featureFour)])

for k in range(0,len(featureOne)):

	featureOneF[0,k]   = float(featureOne[k])
	featureTwoF[0,k]   = float(featureTwo[k])
	featureThreeF[0,k] = float(featureThree[k])
	featureFourF[0,k]  = float(featureFour[k])

del k

# plt.figure()
# plt.plot(featureFourF[0])
# plt.show()

trainingSet      = np.zeros([4,len(featureThree)])
trainingSet[0,:] = featureOneF
trainingSet[1,:] = featureTwoF
trainingSet[2,:] = featureThreeF
trainingSet[3,:] = featureFourF

inputs   = np.zeros([1,trainingSet.shape[0]])
label    = np.zeros([1,trainingSet.shape[1]])
label[0] = labels
label    = label.astype(int)

del labels, featureOneF,featureTwoF, featureThreeF, featureFourF
del featureOne, featureTwo, featureThree, featureFour, line, importedData

# sample the indices from the uniform distribution
# and the training data should be the rest of the sample

# define size of training set and input

trainingSetSize = 0.75
inputSize       = 0.25

trainingSetNum  = int( trainingSet.shape[1] * 0.75 ) # to make sure that index is integer
inputNum        = int( trainingSet.shape[1] * 0.25 )

# compute indices for training and input data

trainingSetIDX = np.zeros([trainingSetNum])
inputIDX       = np.zeros([inputNum])

counterOne = 0

while counterOne != trainingSetNum:

	newIdx = np.random.uniform(0,trainingSet.shape[1],1)

	if newIdx not in trainingSetIDX:

		trainingSetIDX[counterOne] = int( newIdx )

		counterOne += 1

counterTwo = 0

while counterTwo != inputNum:

	newIdx = np.random.uniform(0,trainingSet.shape[1],1)

	if newIdx not in inputIDX:

		inputIDX[counterTwo] = int( newIdx )

		counterTwo += 1

# since we have indices now, select the relevant observations from the sample

for j in xrange(0,len(trainingSetIDX)):

	trainingSetIDX[j] = int(trainingSetIDX[j])

# choose the training and input data from the sample

trainingSetData = trainingSet[:,trainingSetIDX.astype(int)]
inputData       = trainingSet[:,inputIDX.astype(int)]

# choose corresponding label

trainingLabel = label[:,trainingSetIDX.astype(int)]
inputLabel    = label[:,inputIDX.astype(int)]

# now do the loop for every observation in the input set

# instatiate class, inputs must be numpy arrays

neighbors = 1 # number of neighbors

ClassifierKNN = KNN_Classifier(neighbors,trainingSetData,trainingLabel)

# create list for predicted labels

predictedLabelList = np.zeros([inputNum])

countAcc = 0

for j in xrange(0,inputNum):

	predictedLabelList[j] = ClassifierKNN.predictLabel(inputData[0:numFeatures,j])

 	print inputData[0:numFeatures,j]

 	if predictedLabelList[j] == inputLabel[0,j]:

 		countAcc += 1

# calculate classifier accuracy

accuracyKNN = countAcc / float( inputLabel.shape[1] )

