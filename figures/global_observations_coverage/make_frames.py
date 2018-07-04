#!/usr/bin/env python

# Make all the individual frames for a movie
#  run the jobs on SPICE.

import os
import sys
import time
import subprocess
import datetime

max_jobs_in_queue=500
# Where to put the output files
opdir="%s/slurm_output" % os.getenv('SCRATCH')
if not os.path.isdir(opdir):
    os.makedirs(opdir)

# Plotted size of observations might vary with date
def obs_size(dte):
    return 0.75

# Timestep might vary with date as well
# Also need to put in some big skips, to keep
#   total length somewhere reasonable.
def next_timestep(dte):
    old=dte
    new=dte+datetime.timedelta(minutes=30)
    if(old.month!=new.month):
        new=datetime.datetime(new.year+5,
                     new.month,new.day,
                     new.hour,new.minute)
    return new

start_day=datetime.datetime(1851, 1, 1,13)
end_day  =datetime.datetime(2000,12,31,11)

# Function to check if the job is already done for this timepoint
def is_done(dte):
    op_file_name=("%s/images/transcription_figures/ispd/" +
                  "obs_%04d%02d%02d%02d%02d.png") % (
                            os.getenv('SCRATCH'),
                            dte.year,dte.month,dte.day,
                            dte.hour,dte.minute)
    if os.path.isfile(op_file_name):
        return True
    return False

current_day=start_day
while current_day<end_day:
    queued_jobs=subprocess.check_output('squeue --user hadpb',
                                         shell=True).count('\n')
    max_new_jobs=max_jobs_in_queue-queued_jobs
    while max_new_jobs>0 and current_day<=end_day:
        if is_done(current_day):
            current_day=next_timestep(current_day)
            continue
        f=open("multirun.slm","w+")
        f.write('#!/bin/ksh -l\n')
        f.write('#SBATCH --output=%s/TR_obs_frame_%04d%02d%02d%02d.out\n' %
                   (opdir,
                    current_day.year,current_day.month,
                    current_day.day,current_day.hour))
        f.write('#SBATCH --qos=normal\n')
        f.write('#SBATCH --ntasks=4\n')
        f.write('#SBATCH --ntasks-per-core=1\n')
        f.write('#SBATCH --mem=40000\n')
        f.write('#SBATCH --time=10\n')
        for i in (0,1,2,3):
            while is_done(current_day):
                current_day=next_timestep(current_day)
                if current_day>=end_day: break
            cmd=("./plot_obs_fortime.py --year=%d --month=%d" +
                " --day=%d --hour=%d --minute=%d & \n") % (
                   current_day.year,current_day.month,
                   current_day.day,current_day.hour,
                   current_day.minute)
            f.write(cmd)
            current_day=next_timestep(current_day)
        f.write('wait')
        f.close()
        rc=subprocess.call('sbatch multirun.slm',shell=True)
        os.unlink('multirun.slm')
        #sys.exit(0)
        max_new_jobs=max_new_jobs-1
    time.sleep(60)
