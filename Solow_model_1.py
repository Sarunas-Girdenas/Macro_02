# This is code for BEE2026 third tutorial, Solow growth Model

import matplotlib.pyplot as plt
import numpy as np

# declare time horizon

time = 300

# declare parameter values

alpha = 0.5   # production function parameter
n     = 0.05  # population growth
s     = 0.65  # savings rate
d     = 0.04  # depreciation rate
z     = 1     # productivity


Y = np.zeros([time+1,1])
y = np.zeros([time+1,1])
I = np.zeros([time+1,1])
N = np.zeros([time+1,1])
K = np.zeros([time+1,1])
k = np.zeros([time+1,1])
c = np.zeros([time+1,1])
i = np.zeros([time+1,1])
breake = np.zeros([time+1,1])
invest = np.zeros([time+1,1])

# initial values of variables

Y[0] = 100                # capital
I[0] = s*Y[1]             # investment
N[0] = 100                # population
K[0] = I[1] + (1-d)*10.0  # capital

# implement the Model

for t in range(0,time):

	Y[t,:] = z * ((K[t]**alpha) * N[t]**(1-alpha)); # production function

	N[t+1,:] = (1+n)*N[t];                        # population growth

	I[t,:] = s*Y[t];                              # investment (investment = savings)

	K[t+1,:] = I[t] + (1-d)*K[t];				  # capital

	y[t,:] = Y[t] / N[t];                         # production per capita

	i[t,:] = I[t] / N[t];                         # investment (savings) per capita

	k[t,:] = K[t] / N[t];                         # capital per capita

	breake[t,:] = (d+n)*k[t];                     # break-even investment

	c[t,:] = (1-s)*k[t];                          # consumption per capita

	invest[t,:] = s*y[t];                         # investment




# plot results

plt.figure
plt.plot(y[0:len(y)-1],'k',label='Y / C')
plt.plot(c[0:len(c)-1],'r',label='C / N')
plt.legend()
plt.xlabel('Time Horizon')
plt.ylabel('Y / N')
plt.title('Production and Consumption per Capita')
plt.show()

plt.figure
plt.plot(k[0:len(k)-1],'k',label='Capital per Worker')
plt.plot((((invest-breake)/k)*100.0)[0:len(c)-1],'r',label='Growth Rate (Magnified x100)')
plt.legend()
plt.xlabel('Time Horizon')
plt.ylabel('Value')
plt.title('Capital per Worker & Growth Rate')
plt.show()

plt.figure
plt.plot(i[0:len(i)-1],'k')
plt.xlabel('Time Horizon')
plt.ylabel('I / N')
plt.title('Investment per Capita')
plt.show()

plt.figure
plt.plot(breake[0:len(breake)-1],'k',label='(d+n)k')
plt.plot(invest[0:len(invest)-1],'r',label='szy(k)')
plt.legend()
plt.xlabel('Time Horizon')
plt.ylabel('Values')
plt.title('Investment per Capita')
plt.show()

plt.figure
plt.plot(k[0:len(k)-1],breake[0:len(breake)-1],'k',label='(d+n)k')
plt.plot(invest[0:len(invest)-1],'r',label='szy(k)')
plt.legend()
plt.xlabel('k')
plt.ylabel('i')
plt.title('Capital & Investment')
plt.show()








