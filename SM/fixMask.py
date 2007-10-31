import pyfits
import numarray as num
import sys

# turn all the mask bits into 1
MaskedImageMsk = sys.argv[1]
ptr  = pyfits.open(MaskedImageMsk, mode='update')
ptr[0].data = num.where(ptr[0].data > 0, 1, 0).astype(num.UInt8)
ptr[0].header.update('MP_BAD', 0)
ptr[0].header.update('MP_SAT', 1)
ptr[0].header.update('MP_INTRP', 2)
ptr[0].header.update('MP_CR', 3)
ptr[0].header.update('MP_EDGE', 4)
ptr.flush()
