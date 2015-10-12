# This file answers question 2 from tutorial
import numpy as np
from matplotlib import pyplot as plt

# Economy is defined as:
# infl[t]=infl[t-1]+0.1*y[t-1]
# y[t]=0.5*y[t-1]-r[t-1]

# first policy rule
# r[t]=1.1*inf[t]
# second one
# r[t]=r_coef1*inf[t]+r_coef2*y[t]

# loss function
# L[t]=inf[t]**2+y[t]**2

time = 25 # model horizon
y1    = np.zeros([time,1])
y2    = np.zeros([time,1])
infl1 = np.zeros([time,1])
infl2 = np.zeros([time,1])
r1    = np.zeros([time,1])
r2    = np.zeros([time,1])
L1    = np.zeros([time,1])
L2    = np.zeros([time,1])

# first case

# initial values
infl1[0] = 0
infl2[0] = 0
y1[0]    = -1
y2[0]    = -1
r1[0]    = 1.1*infl1[0]
r2[0]    = 1.1*infl2[0]+1.1*y2[0] 

# calculate inflation, output and loss

for k in range(1,time):

	# first monetary regime

	infl1[k] = infl1[k-1] + 0.1*y1[k-1]   # inflation
	y1[k] = 0.5*y1[k-1] - r1[k-1]         # output
	r1[k] = 1.1*infl1[k]      # policy rule
	L1[k] = infl1[k]**2 + y1[k]**2        # loss function

	# second monetary regime

	infl2[k] = infl2[k-1] + 0.1*y2[k-1]   # inflation
	y2[k] = 0.5*y2[k-1] - r2[k-1]         # output
	r2[k] = 1.1*infl2[k] + 1.1*y2[k]      # policy rule
	L2[k] = infl2[k]**2 + y2[k]**2        # loss function

plt.figure
plt.plot(infl1,'-ko',label='Inflation 1 Rule')
plt.plot(infl2,'-ro',label='Inflation 2 Rule')
plt.xlabel('Time Period')
plt.title('INFLATION')
plt.legend(loc='upper right')
plt.show()

plt.figure
plt.plot(y1,'-ko',label='Output 1 Rule')
plt.plot(y2,'-ro',label='Output 2 Rule')
plt.xlabel('Time Period')
plt.title('OUTPUT')
plt.legend(loc='upper right')
plt.show()

plt.figure
plt.plot(L1,'-ko',label='Loss 1 Rule')
plt.plot(L2,'-ro',label='Loss 2 Rule')
plt.xlabel('Time Period')
plt.title('LOSS FUNCTION')
plt.legend(loc='upper right')
plt.show()

print infl1[0:4]
print '======='
print y1[0:4]