"med" is a subregion of one of the exposure "CFHT/D4/cal-53535-i-797722_1"
starting at 0-indexed pixel (1563, 1907) of size 500x700.
This subregion was chosen to include some saturated pixels,
some masked pixels and plenty of stars, including a star partially cut off by the edge of the frame.

Warning: CFHT/D4/cal-53535-i-797722_1 has a WCS that the LSST stack cannot handle.
However, the WCS in med_img.fits is fine.

"medsub" is a subregion of med starting at 0-indexed pixel (40, 150) of size 145 x 200

medswarpcommands.sh is a shell script that generates the swarped versions of med_img.fits.
These are used in unit tests for lsst.afw.math.warpExposure.
As such they are intentionally have a large rotation and scale change
and some edge pixels.

medswarp1.head is used by medswarpcommands.sh to describe the desired WCS of the swarped images.
