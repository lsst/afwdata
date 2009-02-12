#!/bin/sh
swarp med_img.fits -IMAGEOUT_NAME medswarp1.fits -SUBTRACT_BACK N -GAIN_DEFAULT 1.0 -RESAMPLING_TYPE BILINEAR
mv medswarp1.fits medswarp1bilinear.fits
swarp med_img.fits -IMAGEOUT_NAME medswarp1.fits -SUBTRACT_BACK N -GAIN_DEFAULT 1.0 -RESAMPLING_TYPE LANCZOS4
mv medswarp1.fits medswarp1lanczos4.fits
