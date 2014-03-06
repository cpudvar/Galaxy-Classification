from astropy.io import fits
import numpy
import scipy
import matplotlib
import pylab
import os

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
    width, height = getDimensions(hdulist["PRIMARY"])
    
    print "Width: ", width 
    print "Height: ",  height   
    
    minValue, maxValue, pixelValues = findPixelRange(imageData)
    print "Min value: " , minValue , "\nMax value: " , maxValue
    
    plotTable(pixelValues)
    
    hdulist.close()
    
def getDimensions(data):    
    dimensions = data.shape
    
    return dimensions[0], dimensions[1]

def plotTable(yData):
    numPoints = len(yData)
    xData = []
    
    for i in range(numPoints):
        xData.append(i+1)
        
    
    entries = len(xData)
    
    for i in range(entries):
        print xData[i], yData[i]
        
    matplotlib.pyplot.scatter(xData, yData)
    
    pylab.show()
    
def findPixelRange(fileName):
    minValue=9999
    maxValue=0
    pixelValues = []
    
    y = 800

    #dont hardcode dimensions of image
    """
    for x in range(1600):
        for y in range(1600):
            if fileName[x,y] < minValue:
                minValue = fileName[x,y]
            if fileName[x,y] > maxValue:
                maxValue = fileName[x,y]
    """
    for x in range(1600):
        pixelValues.append(fileName[x,y])
                
    return minValue, maxValue, pixelValues
    
def plotHorizontal(midpoint, image, height, width, fileName):
    for x in range(width):
        print x, fileName[midpoint-1, x]
        
        pass
        #write x, value to .csv
        
    
if __name__ == '__main__':
    main()