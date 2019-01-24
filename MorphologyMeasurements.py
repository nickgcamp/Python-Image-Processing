from skimage import io, color, measure, filters, exposure, segmentation, morphology
import matplotlib.pyplot as plt
import numpy as np

'''
Lab 10 Morphology & Measurement
'''
plt.close('all')

DIR = '/users/nick/GoogleDrive/School/Fall 2018/Biophysics/'

# read image in. convert to gray scale
cells = io.imread(DIR + '/blurring.png', as_gray=True)
plt.imshow(cells, cmap='gray')
plt.title('Grayscale Original')
plt.show()
print('shape', cells.shape, '\tdtype', cells.dtype)

# histogram
(a, b) = exposure.histogram(cells)
plt.stem(b, a, markerfmt='b', linefmt='b-')
plt.title('Histogram')
plt.show()

# threshold
t = filters.threshold_yen(cells)
print('threshold yen value', t)
cellsBW = cells > t
plt.imshow(cellsBW, cmap='gray')
plt.title('Threshold Yen')
plt.show()

# counting
(ChipsLB, count) = measure.label(cellsBW, return_num=True)
print('Count', count)
plt.imshow(ChipsLB, cmap='terrain')
plt.colorbar()
plt.title('Color Count')
plt.show()

# label image
P = measure.regionprops(ChipsLB)
l = 0
for a in P:
    # print(l, a.area, a.centroid, a.equivalent_diameter)
    l += 1
# redo image with numbers
im = np.zeros(cells.shape)
for j in range(count):
    cords = P[j].coords
    for i in cords:
        im[i[0], i[1]] = 1
    centre = P[j].centroid
    plt.text(centre[1], centre[0], str(j), color='r')
plt.imshow(im, cmap='gray')
plt.show()

# morphology to separate cells
cellsOP = morphology.opening(cellsBW)
plt.imshow(cellsOP, cmap='gray')
plt.title('Sepearated cells')
plt.show()
(cellsOP, counttwo) = measure.label(cellsOP, return_num=True)
print('count after opening', counttwo)

# measure region props

# cellProps = measure.regionprops(cellsBW)
# print('cell props', cellProps)

# ----------------------
# Part 2
# ----------------------

# read circuit image convert to gray scale
circuit = io.imread(DIR + '/circuitboard.jpg', as_gray=True)

# t = filters.threshold_otsu(circuit)
t = .65
print(t)
circuitBW = circuit > t
plt.imshow(circuitBW, cmap='gray')
plt.title('circuit BW')
plt.show()

# morphology.remove_small_holes()
circuitSH = morphology.remove_small_holes(circuitBW, area_threshold=256, connectivity=2)
plt.imshow(circuitSH, cmap='gray')
plt.title('remove small holes')
plt.show()

# erosion
circuitNEWm = morphology.binary_erosion(circuitSH)
plt.imshow(circuitNEWm, cmap='gray')
plt.title('binary erosion')
plt.show()

# structuring element
sElement = morphology.rectangle(5, 5)
circuitFinal = morphology.erosion(circuitNEWm, sElement)
plt.imshow(circuitFinal, cmap='gray')
plt.title('last')
plt.show()


