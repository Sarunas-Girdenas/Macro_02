# This code fits polynomial of degree n using gradient descent algorithm
# we use univariate time series model we use to the data is y = a + b*data + c*data^2+..+f*data^n
# variable data must be numpy array
# written by Sarunas Girdenas, 2015, sg325@exeter.ac.uk

import matplotlib.pyplot as plt
import numpy as np

#Y = np.array([1,3,5,7,6,3,1]).T

class polynomial_fit(object):	

	def __init__(self,data,degree,alpha):
		self.data   = data   # data to fit the model
		self.degree = degree # degree of polynomial
		self.alpha  = alpha # learning rate

		global X, coefs, polyn, g

		g = self.data.size # length of sample size

		coefs = np.ones([self.degree+1,1]) # container for coefficients

		polyn = np.ones([self.degree+1,g])

		for i in range(0,self.degree+1):
			polyn[i,:] = self.data ** i

		X = polyn.T

	def grad_descent(self):

		def cost_F(X,data,coefs):
			training = g
			pred     = X.dot(coefs).flatten()
			sq_err   = (pred - self.data) ** 2
			J = (1.0 / (2*training)) * sq_err.sum()
			return J

		
		max_iter = 7000 # No of maximum iterations
		no_iter  = 0 # initialize 
		Er       = 10e-15 # tolerance for error

		J_loss_hist = np.zeros([max_iter,1]) # empty array to store loss function values
		J_loss_new  = 0 # initialize loss function value
		J_loss      = cost_F(X,self.data,coefs) # initial loss
		err         = np.zeros([len(coefs),g]) # initialize errors
		coefs_hist  = np.zeros([max_iter,len(coefs)])

		# Gradient Descent Algorithm

		while abs(J_loss - J_loss_new) > Er:

			no_iter += 1

			if no_iter == max_iter:
				break

			J_loss_hist[no_iter,0] = cost_F(X,self.data,coefs)

			J_loss = cost_F(X,self.data,coefs)

			predictions = X.dot(coefs).flatten()

			for i in range(0,len(coefs)):
				err[i,:]   = (predictions - self.data) * X[:,i]
				coefs[i,0] = coefs[i,0] - self.alpha*(1.0/g) * err[i,:].sum()
				coefs_hist[no_iter,i] = coefs[i,0]

			J_loss_new = cost_F(X,self.data,coefs)

			
		print 'Algorithm Converged in: ', no_iter, 'Number of Iterations!'

		print 'Fitted Polynomial Coefficients Are:', coefs

	def save_results(self):

		f1 = open('save_coefs.txt','w')
		for item in coefs:
			f1.write(str(item) +'\n')
		f1.close()

	def get_coefs(self):
		return coefs

	def get_matrix(self):
		return X

	# def plot_res(self):

	# 	fit = X.dot(coefs).flatten()
	# 	Fig1 = plt.figure
	# 	plt.plot(fit,'r',label = 'Fitted Polynomial')
	# 	plt.plot(self.data,'o', label = 'Actual Data')
	# 	plt.xlabel('Data')
	# 	plt.title('Fitted Polynomial')
	# 	plt.legend(loc='lower center', shadow=True)
	# 	plt.show()

	# 	return Fig1



