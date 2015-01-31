# written by Sarunas Girdenas, 2015, sg325@exeter.ac.uk

from polyn_fit import polynomial_fit
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

df = pd.read_csv('report.2015012200.day-two.csv')
colm = df.offer_price
time_purchase = df.purchase_time

Y1 = np.zeros([len(colm),1])
Y = np.zeros([len(colm),1])

colm2 = pd.Series((colm),index = time_purchase)

for k in range(0,len(colm)):
	colm2[k] = colm[k]

for k in range(0,len(colm)):
	Y1[k] = colm[k]

Y2 = stats.boxcox(Y1) # use BoxCox data transform

for k in range(0,len(Y1)):
	Y[k] = Y2[0][k][0]

Y = Y.T 

### Fit polyniam, choose any degree you like

n = 2 # degree of polyn
alpha = 0.001 # learning rate

H = polynomial_fit(Y,n,alpha)
H.grad_descent()
coefficients = H.get_coefs() # get coefficients values
X = H.get_matrix() # get coefficients matrix

### end of polynomial fit

### plot results from fitting polynomial

def plot_res(coefficients,interval):

	fit = X.dot(coefficients).flatten()
	Fig1 = plt.figure
	plt.plot(fit[1:interval],'r')
	plt.plot(Y[0][1:interval],'o')
	plt.xlabel('Data')
	plt.title('Fitted Polynomial after Box Cox Transform')
	plt.show()

	return Fig1

int_lengt = 200

plot_res(coefficients,int_lengt)

### end of plotting results, choose any length of interval you like (must be less than number of obs)

### compute moving average for any given window (smaller than number of obs)

def moving_average(data,window):

	weights = np.repeat(1.0,window)/window
	sma = np.convolve(data,weights,'valid')
	return sma

mov_avg = moving_average(colm,100)

plt.figure
#plt.plot(Y[0][1:1000],'--o')
colm2[1:3000].plot(style='k--')
plt.plot(mov_avg[1:3000],'r',linewidth = 3.0)
plt.title('Moving Average, Actual Data')
plt.show()