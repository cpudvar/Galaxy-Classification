from astropy.io import fits
import numpy
import scipy
import matplotlib
import pylab
import os
from scipy import ndimage
import sys

def main():
    imageName = "658nmos.fits"
    #We should make this non-hardcoded in ANY way
    ###
    #if (len(sys.argv)!=2):
        #imageName = sys.argv[1]
    ###
    #read in FITS file, find midpoint
    #Get location of script because path is basically
    #  hardcoded in. Find a better way?
    os.chdir(os.path.dirname(sys.argv[0]))
    imageFileLocation = os.path.abspath(os.path.join(os.pardir, 'images'))
    print imageFileLocation
    #from location of python script
    
    #header data unit    
    hdulist = fits.open(os.path.join(imageFileLocation, imageName))
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
    return data.shape
    
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
    # maxBright = -1
    # brightx = 0
    # brighty = 0
    # for brightx in blurred:
    #     for brighty in blurred:
    #         if blurred [brightx][brighty] > maxBright:
    #             maxBright = blurred[brightx][brighty]
    # print maxBright
    return blurred

def drawContour(imag):
    print countour

    
if __name__ == '__main__':
    main()
