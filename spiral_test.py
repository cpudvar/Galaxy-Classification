from astropy.io import fits
import numpy
import scipy
import matplotlib

def main():
    #read in FITS file, find midpoint
    
    #header data unit
    hdulist = fits.open('rosat_pspc_rdf2_3_bk2.fits')
    print hdulist.info()
    
    imageData = hdulist[0].data
    
    
    minValue, maxValue = findPixelRange(imageData)
    print "Min value: " , minValue , "\nMax value: " , maxValue
    
    hdulist.close()
    
def findPixelRange(fileName):
    minValue=9999
    maxValue=0
    
    for x in range(512):
        for y in range(512):
            if fileName[x,y] < minValue:
                minValue = file[x,y]
            if fileName[x,y] > maxValue:
                maxValue = file[x,y]
                
    return minValue, maxValue
    
def plotHorizontal(midpoint, image, height, width, fileName):
    for x in range(width):
        print x, fileName[midpoint-1, x]
        
        pass
        #write x, value to .csv
        
def graphValue(fileName):
    #plot 
    pass
    
if __name__ == '__main__':
    main()