from astropy.io import fits
import numpy
import scipy
import matplotlib
import pylab
import os
from scipy import ndimage

def main():
    imageName = "/658nmos.fits"
    #read in FITS file, find midpoint
    imageFileLocation = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Images'))
    print imageFileLocation
    #from location of python script
    
    #header data unit    
    hdulist = fits.open(imageFileLocation + imageName)
    #print hdulist.info()
    
    imageData = hdulist[0].data
    
    # TODO: make sure this works for all images
    dimensions = getDimensions(hdulist["PRIMARY"])  
    brightest = blurring(imageData)
    
    minValue, maxValue, pixelValues = findPixelRange(imageData, dimensions)
    print "Min value: " , minValue , "\nMax value: " , maxValue
    print "brightest", brightest
    plotTable(pixelValues)

    
    
    hdulist.close()
    
def getDimensions(data):    
    dimensions = data.shape
    
    return dimensions

def plotTable(yData):
    numPoints = len(yData)
    xData = []
    
    for i in range(numPoints):
        xData.append(i+1)        
    
    entries = len(xData)
    
    #view vales that are plotted
    """
    for i in range(entries):
        print xData[i], yData[i]
    """
    
    matplotlib.pyplot.scatter(xData, yData)    
    pylab.show()
    
def findPixelRange(fileName, dimensions):
    minValue=9999
    maxValue=0
    pixelValues = []
    
    width = dimensions[0]
    height = dimensions[1]
    
    #find midpt of height -> values for horizontal line
    y = height/2

    """
    #finds range of pixel values for a given image (min and max)
    for x in range(1600):
        for y in range(1600):
            if fileName[x,y] < minValue:
                minValue = fileName[x,y]
            if fileName[x,y] > maxValue:
                maxValue = fileName[x,y]
    """
    
    for x in range(width):
        pixelValues.append(fileName[x,y])
                
    return minValue, maxValue, pixelValues  

def blurring(imag):
    blurred = ndimage.gaussian_filter(imag, 5)
    return blurred

    
if __name__ == '__main__':
    main()