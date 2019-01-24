
# coding: utf-8

# ## Morphology & Measuring
# ### Segment a grayscale image
# ### Count regions
# ### Use morphological opening to separate connected regions
# ### Recount regions
# ### Label regions
# ### Get properties using regionprops()
# 

# In[ ]:


get_ipython().magic('matplotlib inline')
from skimage import io, color, measure, exposure, segmentation, morphology
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['image.cmap'] = 'gray'


# ### Prepare image of connected chips

# In[ ]:


chips = io.imread('/Users/ravi/Documents/Augsburg/PythonIM/IMAGES/chips.png')
chips = color.rgb2gray(chips)
plt.imshow(chips)
print(chips.shape, chips.dtype)


# In[ ]:


(v,b) = exposure.histogram(chips)
plt.stem(b,v,markerfmt='r',linefmt='r-')


# ### Segment image by thresholding
# #### Use histogram to detemine threshold
# #### Or use threshold determinig methods e.g: otsus method etc.

# In[ ]:


T = 0.24
ChipsBW = chips < T
plt.imshow(ChipsBW)


# ### Label regions
# #### Connected regions are counted as one
# #### Different colors represent different objects

# In[ ]:


(ChipsLB, NLab) = measure.label(ChipsBW, return_num=True)
print(NLab)
plt.imshow(ChipsLB, cmap='jet')
plt.colorbar()


# ### Get region properties
# #### Extract region properties

# In[ ]:


P = measure.regionprops(ChipsLB)
l=0
for a in P:
    print (l, a.area, a.centroid, a.equivalent_diameter)
    l+=1


# ### Assign region numbers and redraw image

# In[ ]:


im = np.zeros(chips.shape)
for j in range(NLab):
    cords = P[j].coords
    for i in cords:
        im[i[0], i[1]] = 1
    centre = P[j].centroid
    plt.imshow(im)
    plt.text(centre[1], centre[0], str(j), color='r')


# ### Disconnect connected objects
# ### Use morphology open function (erode + dilate)

# In[ ]:


Struct = morphology.disk(5)
ChipsOP = morphology.opening(ChipsBW, Struct)
#Struct = morphology.disk(3)
#ChipsOP = morphology.binary_dilation(ChipsOP, Struct)
plt.imshow(ChipsOP)


# ### Label regions and get region properties
# ### Region count after opening is different

# In[ ]:


(ChipsLB, NLab) = measure.label(ChipsOP, return_num=True)
print(NLab)
plt.imshow(ChipsLB, cmap='jet')
plt.colorbar()
P = measure.regionprops(ChipsLB)
l=0
for a in P:
    print (l, a.area, a.centroid, a.equivalent_diameter)
    l+=1


# ### Redraw regions with numbers

# In[ ]:


im = np.zeros(chips.shape)
for j in range(NLab):
    cords = P[j].coords
    for i in cords:
        im[i[0], i[1]] = 1
    centre = P[j].centroid
    plt.imshow(im)
    plt.text(centre[1], centre[0], str(j), color='r')


# ## Morphological function convex hull
# ### Over entire image

# In[ ]:


imconvex = morphology.convex_hull_image(ChipsOP)
plt.imshow(imconvex)


# ### Convex hull of each region
# ### Smooths boundary

# In[ ]:


imconvex = morphology.convex_hull_object(ChipsOP)
plt.imshow(imconvex)

