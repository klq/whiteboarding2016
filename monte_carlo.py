import numpy as np
import math

x = np.random.rand(N)
y = np.random.rand(N)

count = 0
for i in xrange(len(x)):
  if math.sqrt((x[i]-0.5)**2 + (y[i]-0.5)**2) < 0.5:
    count = count + 1

porportion_in = count * 1.0 / N
r = 0.5
pi = porportion_in / r**2

