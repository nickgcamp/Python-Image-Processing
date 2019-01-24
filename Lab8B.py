'''
# 2 lab *
@author Nick Campuzano
'''

import numpy as np
import matplotlib.pyplot as plt

y = np.array([0, 0, 0, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.3,
              0.4, 0.5, 0.6, 0.7, 0.6, 0.5, 0.4, 0.3, 2,
              0.1, 0.1, 0.1, 1, 1, 1, .4, .4, .4])

dy = np.diff(y)
d2y = np.diff(dy)

print('y: \n', y)
print('dy:\n', dy)
print('d2y\n', d2y)

plt.plot(y)
plt.title('plot 1')
plt.show()

N = len(y)
im = np.zeros((N, N)).reshape((N, N))
im[:, 0:] = y
plt.figure()
plt.imshow(im, cmap='viridis')
plt.colorbar()
plt.show()
