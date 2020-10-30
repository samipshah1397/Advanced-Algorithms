import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(1,20,num=50).reshape(-1,1)

y = x**2 + (10.5*np.random.randn(50,1) + 5)+np.random.randn()

#10.5 is the std and 5 is the mean of the randn function

y = y.reshape(-1,1)

print(y.shape,x.shape)

plt.scatter(x,y)