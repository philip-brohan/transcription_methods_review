Global observations count
=========================

The total number of observations, in ISPD3.2.9, over the period jan 1st 1851 to Dec 31st 2000, is 1,133,185,756.

Code to count them
------------------

Download all the observations for the period:

.. literalinclude:: ../../figures/global_observations_count/get_data.py

The data files have 1 observation per line, so it's fastest to count the lines

.. literalinclude:: ../../figures/global_observations_count/count_obs.py

Note, the unix utility 'wc' would do this, except that 'wc -l $SCRATCH/20CR/version_2c/observations/*/*.txt' wll fail, as there are too many files.

Counts up to the end of each year
---------------------------------

Output of the script above.

.. literalinclude:: ../../figures/global_observations_count/count.out

