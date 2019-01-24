import numpy as np
import matplotlib.pyplot as plt
import skimage as ski
from skimage import data

'''
Lab 11 Filtering in the frequency domain

@author nick campuzano
'''
sawtooth = np.array([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0]) / 10

xForm1 = np.fft.fft(sawtooth)
xform2 = np.fft.fftshift(xForm1)
plt.figure()
plt.plot(sawtooth, color='green')
plt.plot(xForm1, color='red')
plt.plot(xform2, color='blue')
plt.title('Transforms')
plt.show()

'''
Part 2
'''

cameraMan = ski.data.camera()
plt.imshow(cameraMan, cmap='gray')
plt.title('Camera dude gray scale')
plt.show()

mask1 = np.ones((9, 9))
mask1 /= mask1.sum()

img = np.fft.fft2(cameraMan)
img2 = np.fft.fft2(mask1, cameraMan.shape)
img3 = img * img2
img4 = np.fft.ifft2(img3)

plt.imshow(mask1, cmap='jet')
plt.show()

plt.imshow(abs(img4))
plt.title('Filter Mask')
plt.show()




