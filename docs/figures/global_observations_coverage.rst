Global observations coverage video
==================================

.. raw:: html

    <center>
    <table><tr><td><center>
    <iframe src="https://player.vimeo.com/video/278299089?title=0&byline=0&portrait=0" width="795" height="448" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></center></td></tr>
    <tr><td><center>Pressure observations available to science</center></td></tr>
    </table>
    </center>

A sample of the observations available for reconstructing past climate. These are pressure observations in the International Surface Pressure Databank (version 3.2.9).



Each observation is shown on-screen for 6-hours either side of the time of observation, and the video shows every observation available, sampling one month every 5 years over the period 1851-2000. The idea is to give an indication of the observations coverage and how it changes with time: In times and places with a fixed red dot we have a continuous series of observations with good diurnal sampling (at least 4 times a day); flashing red dots indicate poor diurnal sampling (usually only once or twice a day), and in too many places there are no observations at all.

The video runs at 12 hours to the second, so to show the full 163 years covered by this dataset would take nearly three days. Instead it shows a sample: all the data for one month, and then a 5-year step to the next month shown. Even so it's probably best to view selected periods rather than watching from start to end.


Code to make the figure
-----------------------

Download the data required:

.. literalinclude:: ../../figures/global_observations_coverage/get_data.py

Script to make an individual frame - takes year, month, day, hour, and minute as command-line options:

.. literalinclude:: ../../figures/global_observations_coverage/plot_obs_fortime.py

To make the video, it is necessary to run the script above hundreds of times - giving an image for every 30-minute period in the sampled months. The best way to do this is system dependent - the script below does it on the Met Office SPICE cluster - it will need modification to run on any other system. (Could do this on a single PC, but it will take many hours).

.. literalinclude:: ../../figures/global_observations_coverage/make_frames.py

To turn the thousands of images into a movie, use `ffmpeg <http://www.ffmpeg.org>`_

.. code-block:: shell

    ffmpeg -r 24 -pattern_type glob -i ispd/\*.png \
           -c:v libx264 -threads 16 -preset slow -tune animation \
           -profile:v high -level 4.2 -pix_fmt yuv420p -crf 25 \
           -c:a copy ispd.mp4
