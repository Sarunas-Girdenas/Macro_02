# This is value function iteration solution for Jack's tutorial

# to begin with, replicate the exercise

import numpy as np

# declare matrices of desired order

Q = np.zeros([1,1])
R = np.zeros([2,2])
A = np.zeros([2,2])
B = np.zeros([2,1])

Q[0,0] = 0.1
R[0,0] = 1
R[0,1] = 0
R[1,0] = 0
R[1,1] = 1
A[0,0] = 0.75
A[0,1] = 0
A[1,0] = 0
A[1,1] = 0.25

B[0,0] = -0.5
B[1,0] = -0.5

#Initial guess

P0 = np.eye(2)*(-0.000001)

d = 1
i = 0
beta = 0.99

while d >= 1e-10:

	P1 = R+beta*(A.T)*P0*A-(beta*(A.T)*P0*B)*(np.linalg.inv(Q + beta*(B.T)*P0*B))*(beta*(B.T)*P0*A)
	
	Pd = P1-P0

	d = abs(Pd).max()

	P0 = P1

	if i == 20:
		break

	i = i + 1

print i
print P0