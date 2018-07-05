
import datetime
import IRData.twcr as twcr

dte=datetime.datetime(1953,2,1)
twcr.fetch('prmsl',dte,version='2c')
twcr.fetch_observations(dte,version='2c')
