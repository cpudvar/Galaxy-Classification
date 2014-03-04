import f2n

myimage = f2n.fromfits("name.fits")

myimage.setzscale()
myimage.makepilimage("lin", negative = False)

myimage.tonet("file.png")
