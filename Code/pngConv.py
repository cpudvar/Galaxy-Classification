import f2n
from astropy.io import fits
import numpy
import scipy
import matplotlib
import pylab
import os

def convert(imageName):
    
    imageFileLocation = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Images'))
    
    myimage = f2n.fromfits(imageFileLocation + imageName)
    
    myimage.setzscale()
    myimage.makepilimage("log", negative = False)
    
    myimage.tonet("file.png")
