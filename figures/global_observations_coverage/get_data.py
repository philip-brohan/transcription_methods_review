# Retrieve ISPD3.2.9 observations from NERSC

import datetime
import IRData.twcr as twcr

for year in range(1851,2001):
    dte=datetime.datetime(year,1,1)
    twcr.fetch_observations(dte,version='2c')
