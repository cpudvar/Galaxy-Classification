from astropy.io import fits
import numpy
import scipy
import matplotlib
import pylab
import os
import sys
from scipy import ndimage
from pngConv import *

def main():
    imageName = "m101_050511_12i60m_L.fits"
    
    # for testing, save image data as .png for viewing
    convert(imageName)    
        
    # We should make this non-hardcoded in ANY way --> Caleb agrees
    
    #if (len(sys.argv)!=2):
        #imageName = sys.argv[1]
        
    #read in FITS file, find midpoint
    #Get location of script because path is basically
    #  hardcoded in. Find a better way?
    #os.chdir(os.path.dirname(sys.argv[0]))
    imageFileLocation = os.path.abspath(os.path.join(os.pardir, 'images'))
    
    print imageFileLocation #from location of python script  
    
    # header data unit    
    hdulist = fits.open(os.path.join(imageFileLocation, imageName))
    print hdulist.info()
    
    imageData = hdulist[0].data
    
    # TODO: make sure this works for all images
    dimensions = getDimensions(hdulist["PRIMARY"])  
    
    minValue, maxValue, horizontalMidpointArray, verticalMidpointArray = findPixelRange(imageData, dimensions)
    
    # display range of pixel values for given image
    print "Min value: " , minValue , "\nMax value: " , maxValue
     
    brightest = blurring(imageData)
    print "brightest", brightest
    
    plotTable(horizontalMidpointArray)
    plotTable(verticalMidpointArray)
    hdulist.close()
    
def getDimensions(data):    
    return data.shape
    
def findPixelRange(fileName, dimensions):
    minValue = 999999
    maxValue = -999999
    horizontalMidpointArray = []
    verticalMidpointArray = []
    
    #retrieve height and width of image
    width = dimensions[0]
    height = dimensions[1]
    
    #find midpoint values of image
    horizontalMidpoint = height/2
    verticalMidpoint = width/2
    
    #finds range of pixel values for a given image (min and max)
    for x in range(width):
        for y in range(height):
            if fileName[x,y] < minValue:
                minValue = fileName[x,y]
            if fileName[x,y] > maxValue:
                maxValue = fileName[x,y]
    
    #finds values for horizontal midpoint
    for x in range(width):
        horizontalMidpointArray.append(fileName[x, horizontalMidpoint])
    
    #finds values for vertical midpoint
    for y in range(height):
        verticalMidpointArray.append(fileName[verticalMidpoint, y])    
    
    return minValue, maxValue, horizontalMidpointArray, verticalMidpointArray

def plotTable(yAxisData):
    numPoints = len(yAxisData)
    xAxisData = []
    
    #increment by 1 across x-axis
    for i in range(numPoints):
        xAxisData.append(i+1)        

    matplotlib.pyplot.scatter(xAxisData, yAxisData)    
    pylab.show()

def blurring(image):
    blurred = ndimage.gaussian_filter(image, 5)
    # maxBright = -1
    # brightx = 0
    # brighty = 0
    # for brightx in blurred:
    #     for brighty in blurred:
    #         if blurred [brightx][brighty] > maxBright:
    #             maxBright = blurred[brightx][brighty]
    # print maxBright
    return blurred

def drawContour(image):
    print contour

    
if __name__ == '__main__':
    main()
