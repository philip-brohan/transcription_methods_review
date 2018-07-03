#!/usr/bin/env python

# Plot the observations in ISPD3.2.9 that are active in 20CR
#  for a given time.

import IRData.twcr as twcr
import datetime
import numpy
import pandas

import Meteorographica as mg
import iris
import os

import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import cartopy
import cartopy.crs as ccrs

# Get the datetime to plot from commandline arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--year", help="Year",
                    type=int,required=True)
parser.add_argument("--month", help="Integer month",
                    type=int,required=True)
parser.add_argument("--day", help="Day of month",
                    type=int,required=True)
parser.add_argument("--hour", help="Hour of day (0 to 23)",
                    type=int,required=True)
parser.add_argument("--minute", help="Minute of hour (0 to 59)",
                    type=int,required=True)
parser.add_argument("--radius", help="Marker size (degrees)",
                    type=float,default=0.75)
parser.add_argument("--opdir", help="Directory for output files",
                    default="%s/images/transcription_figures/ispd" % \
                                           os.getenv('SCRATCH'),
                    type=str,required=False)
args = parser.parse_args()
if not os.path.isdir(args.opdir):
    os.makedirs(args.opdir)

dte=datetime.datetime(args.year,args.month,args.day,
                      args.hour,args.minute)


# Define the figure (page size, background color, resolution, ...
aspect=16/9.0
fig=Figure(figsize=(10.8*aspect,10.8),  # Width, Height (inches)
           dpi=100,
           facecolor=(0.88,0.88,0.88,1),
           edgecolor=None,
           linewidth=0.0,
           frameon=False,                # Don't draw a frame
           subplotpars=None,
           tight_layout=None)
# Attach a canvas
canvas=FigureCanvas(fig)

# All mg plots use Rotated Pole, in this case just use the standard
#  pole location.
projection=ccrs.RotatedPole(pole_longitude=180.0, pole_latitude=90.0)

# Define an axes to contain the plot. In this case our axes covers
#  the whole figure
ax = fig.add_axes([0,0,1,1],projection=projection)
ax.set_axis_off() # Don't want surrounding x and y axis
# Set the axes background colour
ax.background_patch.set_facecolor((0.88,0.88,0.88,1))

# Lat and lon range (in rotated-pole coordinates) for plot
extent=[-180.0,180.0,-90.0,90.0]
ax.set_extent(extent, crs=projection)
# Lat:Lon aspect does not match the plot aspect, ignore this and
#  fill the figure with the plot.
matplotlib.rc('image',aspect='auto')

# Draw a lat:lon grid
mg.background.add_grid(ax,
                       sep_major=5,
                       sep_minor=2.5,
                       color=(0,0.3,0,0.2))


# Add the land
land_img=ax.background_img(name='GreyT', resolution='low')

# Load the observations within 6 hours
obs=twcr.load_observations(dte-datetime.timedelta(hours=12),
                           dte+datetime.timedelta(hours=12),version='2c')
# Time difference in s
dtm=pandas.to_datetime(obs.UID.str.slice(0,10),format="%Y%m%d%H")
dts=numpy.divide(dte-dtm,numpy.timedelta64(1, 's'))
# weight the obs by distance from current time
weight=numpy.abs(dts)/(3600.0*6)
obs['weight']=weight
obs=obs[weight<1]
obs['weight']=1-obs['weight']

# Plot the observations
mg.observations.plot(ax,obs,radius=args.radius,
                            facecolor='red')

# Add a label showing the date
mg.utils.plot_label(ax,
              ('%04d-%02d-%02d:%02d' % 
               (args.year,args.month,args.day,args.hour)),
              facecolor=fig.get_facecolor(),
              x_fraction=0.99,
              y_fraction=0.98,
              horizontalalignment='right',
              verticalalignment='top',
              fontsize=14)

# Render the figure as a png
fig.savefig('%s/obs_%04d%02d%02d%02d%02d.png' % 
               (args.opdir,args.year,args.month,args.day,
                           args.hour,args.minute))
