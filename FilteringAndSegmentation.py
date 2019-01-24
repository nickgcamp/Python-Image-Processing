'''
Lab 9 Filtering and Segmentation and Thresholding
@author Nick Campuzano
'''

from skimage import io, exposure, filters, color, measure
import matplotlib.pyplot as plt
from scipy import ndimage

DIR = '/users/nick/GoogleDrive/School/Fall 2018/Biophysics/'

io.use_plugin('matplotlib')
ic = io.imread_collection(DIR + 'bubbles.tif')
myIMG = ic[0]
io.imshow(myIMG, cmap="gray")
plt.show()
myIMG = color.rgb2gray(myIMG)

# histogram
(a, b) = exposure.histogram(myIMG)
plt.plot(b, a)
plt.title('Histogram')
plt.show()

# threshold
t = 0.2
dMyIMG = myIMG > t
plt.imshow(dMyIMG, cmap='gray')
plt.title('Threshold 0.2')
plt.show()

th = filters.threshold_otsu(myIMG)
fMyIMG = myIMG > th
plt.imshow(fMyIMG, cmap='gray')
plt.title('Threshold OTSU')
plt.show()

(dMyIMG, nLab) = measure.label(fMyIMG, return_num=True)
print('Count', nLab)
plt.imshow(dMyIMG, cmap='gray')
plt.show()
# part 2
f = io.imread(DIR + 'cottoncandy.tif')
plt.imshow(f, cmap='gray')
plt.title('Original')
plt.show()

blurred_f = ndimage.gaussian_filter(f, 3)
plt.imshow(blurred_f, cmap='gray')
plt.title('Blurred')
plt.show()

alpha = 50
filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
plt.imshow(sharpened, cmap='gray')
plt.title('Sharpened')
plt.show()

