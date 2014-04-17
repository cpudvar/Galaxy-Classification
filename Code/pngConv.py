import f2n
from astropy.io import fits
import numpy
import scipy
import matplotlib
import pylab
import os

def convert(imageName):
    
    imageFileLocation = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'images'))
    
    myimage = f2n.fromfits(os.path.join(imageFileLocation, imageName))
    
    myimage.setzscale()
    myimage.makepilimage("log", negative = False)
    
    myimage.tonet("image.png")
