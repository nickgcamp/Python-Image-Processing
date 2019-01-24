from skimage import io
import matplotlib.pyplot as plt
import os

DIR = '/users/nick/GoogleDrive/School/Fall 2018/Biophysics/'
io.use_plugin('matplotlib')

ic = io.imread_collection([DIR + '/pathologySlides/pathology_slide_1.PNG',
                           DIR + '/pathologySlides/pathology_slide_2.PNG',
                           DIR + '/pathologySlides/pathology_slide_3.PNG',
                           DIR + '/pathologySlides/pathology_slide_4.PNG',
                           DIR + '/pathologySlides/pathology_slide_5.PNG',
                           DIR + '/pathologySlides/pathology_slide_6.PNG',
                           DIR + '/pathologySlides/pathology_slide_7.PNG',
                           DIR + '/pathologySlides/pathology_slide_8.PNG',
                           DIR + '/pathologySlides/pathology_slide_9.PNG',
                           DIR + '/pathologySlides/pathology_slide_10.PNG'])

io.imshow_collection(ic)
plt.figure()
for img in ic:
    io.imshow(img)
    plt.pause(1 / 50)  # 1/10 of a second

# need a loop here to run through images
# loops through all images
for i in range(0, 10):
    img = ic[i]
    print('\n Image ', i + 1, ' in collection is:', type(img), img.shape)
    plt.figure()
    io.imshow(img)

im1 = ic[0]
print("\n First image in collection is:", type(im1), im1.shape)
plt.figure()
io.imshow(im1)


# writing collection to .tiff file
try:
    os.remove('/Users/nick/Desktop/pathologySlides/ngc.tiff')
except:
    pass  # ignore error

for i in range(10):
    io.imsave(ic[0],im1.shape,append=True, compress=6)
    plt.savefig()

newIC = io.ImageCollection(DIR + '/pathologySlides/ngc.tif')
print('Length of newIC:', len(newIC))

assert (len(ic) == len(newIC))
io.imshow_collection(newIC)
plt.show()
