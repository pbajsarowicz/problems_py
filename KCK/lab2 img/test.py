from skimage import data, io, filter, img_as_float, morphology
from matplotlib import pyplot as plt
from skimage.filter import threshold_otsu
from skimage.filter.edges import convolve
from skimage import measure
import numpy as np
from skimage.draw import polygon

s1 = img_as_float(data.imread('samolot01.jpg',True))
s2 = img_as_float(data.imread('samolot07.jpg',True))
s3 = img_as_float(data.imread('samolot08.jpg',True))
s4 = img_as_float(data.imread('samolot10.jpg',True))
sA = img_as_float(data.imread('samolot01.jpg'))
sB = img_as_float(data.imread('samolot07.jpg'))
sC = img_as_float(data.imread('samolot08.jpg'))
sD = img_as_float(data.imread('samolot10.jpg'))
# Albo: coins(), page(), moon()

image1=np.vstack((s1, s2))
image2=np.vstack((s3, s4))
image12=np.hstack((image1, image2))
imageA=np.vstack((sA, sB))
imageB=np.vstack((sC, sD))
imageAB=np.hstack((imageA, imageB))

image11=np.hstack((s1, s3))
image22=np.hstack((s2, s4))
image1122=np.vstack((image11, image22))
"""
img = np.zeros((10, 10), dtype=np.uint8)
rr, cc = polygon(image1122, image12)
img[rr, cc] = 1
print img"""

g = filter.gaussian_filter(image12,sigma=2)
result = filter.canny(g,sigma=12)
result += filter.sobel(result)

r = np.sin(np.exp((np.sin(result)**3 + np.cos(image12)**2)))
# Find contours at a constant value of 0.8
contours = measure.find_contours(r, 0.8)

img = np.zeros((1600, 1072), dtype=np.uint8)
rr, cc = polygon(image12, r)
img[rr, cc] = 1
# Display the image and plot all contours found


for n, contour in enumerate(contours):
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)
plt.imshow(imageAB)#, interpolation='nearest')


"""

from PIL import Image
from pylab import *

# read image to array
#im = array(Image.open('HOJA.jpg').convert('L'))

# create a new figure


# show contours with origin upper left corner
contour(image12, origin='image', colors='black', levels=[170])
#contour(image12, levels=[250], colors='black', origin='image')
axis('equal')"""




plt.axis('image')
plt.xticks([])
plt.yticks([])
plt.show()