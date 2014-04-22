from astropy.io import fits
import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt


hdulist = fits.open('m101_050511_12i60m_L.fits')
imageData = hdulist[0].data

#img = ndimage.imread('image.png')
plt.imshow(imageData, interpolation='nearest')
plt.show()
# Note the 0 sigma for the last axis, we don't wan't to blurr the color planes together!
img = ndimage.gaussian_filter(imageData, sigma=8, order=0)
plt.imshow(img, interpolation='nearest')
plt.show()

contour_image = plt.contour(img, 5)
plt.clabel(contour_image, inline=1, fontsize=10)
plt.show()