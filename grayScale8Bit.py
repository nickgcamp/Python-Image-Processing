import skimage as ski
from skimage import io, exposure
from skimage.color import rgb2gray
from skimage import img_as_ubyte
import matplotlib.pyplot as plt

plt.close('all')
# import image
img = ski.io.imread('/Users/nick/GoogleDrive/School/'  # image location
                    'Fall 2018/Biophysics/dna-coloured.jpg')
# showing original image to check the image is correct
ski.io.imshow(img)
plt.title("Original")
plt.show()  # show
# printing out the size, data, type etc..
print("img\n", img)
print("Type", type(img))
# print("size", size(img))

# gray scale image
# convert to gray scale
imgGray = rgb2gray(img)
ski.io.imshow(imgGray)
plt.title("Gray")
plt.show()  # show
print("imGray\n", imgGray)
print("Type", type(imgGray))

# 8 bit image
img8 = img_as_ubyte(img)
ski.io.imshow(img8)
plt.title("img8")
plt.show()  # show
print("img8\n", img8)
print("Type", type(img8))

# Histogram
(a, b) = exposure.histogram(img8)
plt.plot(b, a)
plt.title("Histogram")
plt.show()
