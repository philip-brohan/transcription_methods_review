#!/usr/bin/env python

# Want the obs video to run forward within a year, but present
#  the years in reverse order (2000->1850). So change the file
#  names to get the images in the desired order.

import os

dir="%s/images/transcription_figures/ispd" % os.getenv('SCRATCH')
images = os.listdir(dir)
for image in images:
    year=int(image[4:8])
    newyear=2100-year
    newname="%s%04d%s" % (image[0:4],newyear,image[8:20])
    os.rename("%s/%s" % (dir,image),
              "%s/%s" % (dir,newname))

# Run this script again to reverse the effect.
