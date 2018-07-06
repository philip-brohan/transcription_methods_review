Uncertainty and observations
============================

.. figure:: ../../figures/uncertainty_and_observations/pressure_uncertainty.png
   :width: 700px
   :align: center
   :figwidth: 700px

   Observations coverage and reconstructed weather (MSLP) uncertainty.

   Mean-sea-level pressure (mslp) as reconstructed by 20CR version 2c for 1953-02-01:06 (blue contours), and the pressure observations assimilated to make the reconstruction. A seperate contour plot is shown for each of the 56 ensemble members comprising 20CR2c - where these all agree we have confidence in the reconstruction, where the contours diverge the reconstruction is very uncertain.

The red dots mark the observations asimilated at the selected time-point (1953-02-01:06) - 6-hours worth of observations. The blue contours form a spaghetti-contour plot - 56 contour plots (one for each 20CR ensemble member) all plotted on top of one another. Where the ensemble spread is small all 56 contour plots are almost the same - this produces the clean contours in the northern extratropics. Where the ensemble spread is large the contours can be in quite different places in the different ensemble plots - producing the messy effect visible in the south-east Pacific. The overall effect is to show both the reconstructed pressure field and its uncertainty. 

Code to make the figure
-----------------------

Download the data required:

.. literalinclude:: ../../figures/uncertainty_and_observations/get_data.py

Script to make the figure:

.. literalinclude:: ../../figures/uncertainty_and_observations/plot_pressure_uncertainty.py

