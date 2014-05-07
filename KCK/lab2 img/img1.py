from Cython import array

from skimage import data, io, filter, img_as_float, morphology
from matplotlib import pyplot as plt
from skimage.filter import threshold_otsu
from skimage.filter.edges import convolve
from skimage import measure
import numpy as np

plt.xticks(())
plt.yticks(())


s1 = img_as_float(data.imread('samolot01.jpg',True))
s2 = img_as_float(data.imread('samolot07.jpg',True))
s3 = img_as_float(data.imread('samolot08.jpg',True))
s4 = img_as_float(data.imread('samolot10.jpg',True))
# Albo: coins(), page(), moon()

image1=np.vstack((s1, s2))
image2=np.vstack((s3, s4))
image12=np.hstack((image1, image2))
#filters
#cannyI = filter.canny(image12, sigma=5)

#c = filter.canny(image12, sigma=6)
#result =   filter.sobel(image12) #filter.canny(image12,sigma=5)
g = filter.gaussian_filter(image12,sigma=2)
result = filter.canny(g,sigma=7)
result += filter.sobel(result)
x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
r = np.sin(np.exp((np.sin(x)**3 + np.cos(y)**2)))
contours = measure.find_contours(r, 0.8)

#result = morphology.dilation(sob, np.square(3))
io.imshow(result,cmap=plt.cm.gray,interpolation='nearest')
#morphology.dilation(image12, square(3), )


#plt.savefig('myimg.pdf')

"""for n, contour in enumerate(contours):
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)"""

plt.axis('image')
plt.xticks([])
plt.yticks([])
plt.show()
plt.close()
# Niepotrzebne, jesli ipython notebook --pyla