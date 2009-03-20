"med" is a subregion of one of the exposure "CFHT/D4/cal-53535-i-797722_1"
starting at 0-indexed pixel (1563, 1901) of size 500x700.
This subregion was chosen to include some saturated pixels,
some masked pixels and plenty of stars, including a star partially cut off by the edge of the frame.

medswarpcommands.sh is a shell script that generates the swarped versions of med_img.fits.
These are used in unit tests for lsst.afw.math.warpExposure.
As such they are intentionally have a large rotation and scale change
and some edge pixels.

medswarp1.head is used by medswarpcommands.sh to describe the desired WCS of the swarped images.
