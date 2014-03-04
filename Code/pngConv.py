import f2n

myimage = f2n.fromfits("name.fits")

myimage.setzscale()
myimage.makepilimage("log", negative = False)

myimage.tonet("file.png")
