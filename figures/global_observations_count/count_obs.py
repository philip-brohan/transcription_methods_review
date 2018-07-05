#!/usr/bin/env python

# Count the total number of observations, 1851-2000
#  Fastest way is to count the lines in the text files

import os
import sys

# How many lines in a file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

total=0
for year in range(1851,2001):
    ydir=("%s/20CR/version_2c/observations/%04d" %
                            (os.getenv('SCRATCH'),year))
    files=os.listdir(ydir)
    for file in files:
        total=total+file_len("%s/%s" % (ydir,file))
    print "%04d %11d" % (year,total)
    sys.stdout.flush()
print total

    
