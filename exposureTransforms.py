import skimage as ski
from skimage import io, color, exposure, transform, filters
import matplotlib.pyplot as plt

img = io.imread('/Users/nick/Desktop/carotidstenosis.jpg')
io.imshow(img)
plt.title("Original")
plt.show()

grayImg = ski.color.rgb2gray(img)

# image is now gray scale
# apply sigmoid, gamma, log, inverse transforms
# show all four

imgSigmoid = exposure.adjust_sigmoid(grayImg)
io.imshow(imgSigmoid)
plt.title("Sigmoid")
plt.show()

imgGamma = exposure.adjust_gamma(grayImg)
io.imshow(imgGamma)
plt.title("Gamma")
plt.show()

imgLog = exposure.adjust_log(grayImg)
io.imshow(imgLog)
plt.title("Log")
plt.show()

# true parameter inverts image
imgInverse = exposure.adjust_log(grayImg, 1, True)
io.imshow(imgInverse)
plt.title("Inverse Log")
plt.show()

# part 2

cottonCandy = io.imread('/Users/nick/Desktop/cottoncandy.tif')
io.imshow(cottonCandy)
plt.title("Cotton Candy Original")
plt.show()

reSizeCC = ski.transform.resize(cottonCandy, (cottonCandy.shape[0] / 2, cottonCandy.shape[1] / 2), anti_aliasing=True)
io.imshow(reSizeCC)
plt.title("Re sized Cotton Candy")
plt.show()

# perform two gaussian tranforms on the resized img. 2x
gaussianCC = ski.filters.gaussian(reSizeCC, sigma=4)
io.imshow(gaussianCC)
plt.title("Gaussian Filter Cotton Candy")
plt.show()

gaussianCC2 = ski.filters.gaussian(gaussianCC, sigma=4)
io.imshow(gaussianCC2)
plt.title("2 Gaussian Filter Cotton Candy")
plt.show()
