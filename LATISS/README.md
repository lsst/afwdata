The following files were produced by Merlin Fisher-Levine (merlin.fisherlevine@gmail.com):
./postISRCCD/postISRCCD_2020021700249-EMPTY~ronchi90lpmm-det000.fits.fz
./postISRCCD/postISRCCD_2020021800027-KPNO_406_828nm~EMPTY-det000.fits.fz
./postISRCCD/postISRCCD_2020021800073-KPNO_406_828nm~EMPTY-det000.fits.fz
./postISRCCD/postISRCCD_2020021800224-EMPTY~EMPTY-det000.fits.fz
./postISRCCD/postISRCCD_2020031500119-EMPTY~ronchi90lpmm-det000.fits.fz

These are on-sky images from LATISS (Rubin Observatory's Auxiliary Telescope slitless spectrograph).
They have been run though some nominal ISR: assembly, bias, dark, defect, overscan subtraction with median-per-row.
Their primary usage is in unit tests for quickFrameMeasurement, but may be useful in some other applications.
They have been compressed with fpack -g2.

To add more files, it is necessary to uncompress the postISRCCDs put by the butler (which don't have .fits.fz suffix, but are nonetheless actually compressed), then recompress, as compressing postISRCCD files will result in no extra compression but also no error message.

Below is the script which made these files
--------
import os
import shutil

filenames = ['/path/to/file1.fits', '/path/to/file2.fits']
outDir = '/some/output/path'

for filename in filenames:
    outnameFz = os.path.join(outDir, os.path.basename(filename)) + '.fz'
    shutil.copy(filename, outnameFz)
    os.system(f'funpack {outnameFz}')
    os.remove(outnameFz)
    outname = outnameFz[:-3]
    os.system(f'fpack -g2 {outname}')
    os.remove(outname)
