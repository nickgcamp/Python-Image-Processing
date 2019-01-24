# Edge processing and histogram

from skimage import io, exposure
import matplotlib.pyplot as plt

plt.close('all')

DIR = '/users/nick/GoogleDrive/School/Fall 2018/Biophysics/'

# read image and show
# aCity = io.imread('/users/nick/GoogleDrive/School/Fall 2018/Biophysics/city.tif')
aCity = io.imread(DIR + 'city.tif')
io.imshow(aCity)
plt.title('Original')
io.imsave((DIR + 'ImagesLab8/Original.jpeg'), aCity)
plt.show()

# histogram equalization
bCity = exposure.equalize_hist(aCity)
io.imshow(bCity)
plt.title('Equalize Original')
io.imsave((DIR + 'ImagesLab8/Equalized Original.jpeg'), bCity)
plt.show()

# histogram of each image

(a,b) = exposure.histogram(aCity)
plt.bar(b, a)
plt.title('Histogram Original')
# io.imsave((DIR + 'ImagesLab8/Histogram Original.jpeg'), ???)
plt.show()
(c, d) = exposure.histogram(bCity)
plt.bar(d, c)
plt.title('Histogram Equalized')
# io.imsave((DIR + 'ImagesLab8/Histogram Equalized.jpeg'), ???)
plt.show()

# adaptive histogram
cCity = exposure.equalize_adapthist(aCity)
io.imshow(cCity)
io.imsave((DIR + 'ImagesLab8/Adaptive Histogram.jpeg'), cCity)
plt.title('Adaptive Histogram')
plt.show()

# adaptive histogram again
dCity = exposure.equalize_adapthist(aCity,
                                    kernel_size=10,
                                    clip_limit=0.01)
io.imshow(dCity)
io.imsave((DIR + 'ImagesLab8/Adaptive Histogram 2.jpeg'), dCity)
plt.title('Adaptive Histogram two')
plt.show()
