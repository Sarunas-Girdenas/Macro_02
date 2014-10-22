# This is code for BEE2026 second tutorial, Malthus growth Model

import matplotlib.pyplot as plt
import numpy as np

# declare time horizon

time = 300

# declare parameter values

alpha = 0.5
gamma = 0.18
z     = 1
L     = 200
N = np.zeros([time+1,1])
N[0]  = 1

# define shock to L (land)

shock                        = np.zeros([time,1])
shock[0:time/3,0]            = 0
shock[time/3:time*(2.0/3),0] = 200
shock[time*(2.0/3):time,0]   = 0

# implement the Model

Y = np.zeros([time,1])

MPL = Y

for t in range(0,time):

	# output

	Y[t,:] = z * ((L + shock[t])**alpha) * N[t]**(1-alpha)

	# population

	N[t+1,:] = ((Y[t] / N[t])**gamma) * N[t]

	# marginal product of land

	MPL[t,:] = z * alpha * ((L+shock[t])**(alpha-1)) * (N[t]**(1-alpha))



# plot results

plt.figure
plt.plot(N,'k')
plt.xlabel('Time Horizon')
plt.ylabel('Population Size')
plt.title('Population Growth')
plt.show()

plt.figure
plt.plot(MPL,'r')
plt.xlabel('Time Horizon')
plt.ylabel('Marginal Product of Land')
plt.title('Marginal Product of Land')
plt.show()














