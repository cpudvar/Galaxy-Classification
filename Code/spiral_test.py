import os
import sys
from astropy.io import fits
import f2n
import numpy
import scipy
import pylab
import matplotlib
from scipy import ndimage
from astropy.io import fits
from optparse import OptionParser
import matplotlib.pyplot as plt

def get_options():
    #Gets options from command line
    usage = """
    Read in a FITS file for identification. 

    spiral_test.py [image_name] [opts] 
    """ 
    parser = OptionParser(usage=usage)
    parser.add_option("-c", default=False, action='store_true',
                  help="Prints out image with contour lines",
                  dest="contour")
    parser.add_option("-l","--location", 
                  default=os.path.abspath(os.path.join(os.pardir, 'images')),
                  help="Select new location for images")

    global opts,imageName
    (opts, args) = parser.parse_args()
    if len(args) != 1:
        print ("Using default image")
        imageName = "m101_050511_12i60m_L.fits"
    else:
        imageName = args[1]

    return

def main():
    get_options()
    
    imageFileLocation = os.path.join(opts.location,imageName)

    # for testing, save image data as .png for viewing
    #convert(imageName)    
        
    imageFileLocation = opts.location
    
    #print imageFileLocation #from location of python script  
    convert(imageFileLocation)
    
    # header data unit    
    hdulist = fits.open(imageFileLocation)
    imageData = hdulist[0].data
    #print hdulist.info()
    
    dimensions = getDimensions(hdulist["PRIMARY"])  
    
    minValue, maxValue, horizontalMidpointArray, verticalMidpointArray = findPixelRange(imageData, dimensions)
    
    # display range of pixel values for given image
    print "Min value: " , minValue , "\nMax value: " , maxValue
    
    plotTable(horizontalMidpointArray)
    plotTable(verticalMidpointArray)
    
    blurredImage = blur(imageData)
    contourImage = drawContour(blurredImage)
    
    #if (opts.contour):
        #drawContour(os.path.join(imageFileLocation, imageName))
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

def blur(imageData):
    #also take parameter for sigma?
    img = ndimage.gaussian_filter(imageData, sigma=7, order=0)
    plt.imshow(img, interpolation='nearest')
    plt.show() 
    
    return img
    
def drawContour(img):
    contour_image = plt.contour(img, 5)
    plt.clabel(contour_image, inline=1, fontsize=10)
    plt.show()
    
    return contour_image

def convert(image):
    
    myimage = f2n.fromfits(image)
    
    myimage.setzscale()
    myimage.makepilimage("log", negative = False)
    
    myimage.tonet((imageName+".png"))
    
if __name__ == '__main__':
    main()
