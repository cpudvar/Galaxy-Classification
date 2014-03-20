from astropy.io import fits
import numpy
import scipy
import matplotlib
from scipy import ndimage
from scipy import misc

def main():
    #read in FITS file, find midpoint
    
    #from location of python script
    imageFileLocation = "images/"
    
    #header data unit
    hdulist = fits.open(imageFileLocation+"658nmos.fits")
    #print hdulist.info()
    
    imageData = hdulist[0].data
    
    # TODO: make sure this works for all images
    width, height = getDimensions(hdulist["PRIMARY"])

    brightest = blurring(imageData)
    
    print "Width: ", width 
    print "Height: ",  height   
    minValue, maxValue = findPixelRange(imageData)
    print "Min value: " , minValue , "\nMax value: " , maxValue
    print "brightest: ", brightest
    hdulist.close()
    
def getDimensions(data):    
    dimensions = data.shape
    
    return dimensions[0], dimensions[1]
    
def findPixelRange(fileName):
    minValue=9999
    maxValue=0

    for x in range(512):
        for y in range(512):
            if fileName[x,y] < minValue:
                minValue = fileName[x,y]
            if fileName[x,y] > maxValue:
                maxValue = fileName[x,y]
                
    return minValue, maxValue
    
def plotHorizontal(midpoint, image, height, width, fileName):
    for x in range(width):
        print x, fileName[midpoint-1, x]
        
        pass
        #write x, value to .csv
        
def graphValue(fileName):
    #plot 
    pass

def blurring(hdulist):
    blurred = ndimage.gaussian_filter(hdulist, 5)
    return blurred 


    
if __name__ == '__main__':
    main()