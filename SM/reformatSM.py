import numarray as num
import pyfits
import sys

MaskedImage = sys.argv[1]
MaskedImageImg = MaskedImage+'_img.fits'
MaskedImageMsk = MaskedImage+'_msk.fits'
MaskedImageVar = MaskedImage+'_var.fits'

# need to turn img into float
ptr  = pyfits.open(MaskedImageImg, mode='update')
ptr[0].data = ptr[0].data.astype(num.Float32)
ptr.flush()

# need to turn mask into 8bit
ptr  = pyfits.open(MaskedImageMsk, mode='update')
ptr[0].data = num.where(ptr[0].data > 0, 1, 0).astype(num.UInt8)
ptr.flush()

# if len(sys.argv) > 2:
# redo the variance also.  its input as noise, turn into variance
ptr  = pyfits.open(MaskedImageVar, mode='update')
ptr[0].data *= ptr[0].data
ptr.flush()
