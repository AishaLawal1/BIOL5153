#! /usr/bin/env python3

#import modules

import argparse

#create an ArgumentParser object (like a box that holds an argument)

parser = argparse.ArgumentParser(description="This script creates a SLURM file for jobs on the AHPCC cluster")

#add positional (required) arguments

parser.add_argument("job_name",help="Name of the job", type=str)

#add optional arguments
#the default for the 'store_true' is  ..."False"
#if 'store_true', then assign 'True' wth -v or --verbose
parser.add_argument("-n","--num_nodes", help="Number of nodes to request",\
default = '1', type =int)

# The major difference between a positional and optional argument is the presence of dashes in the front of the arguments
parser.add_argument("-p","--num_processors", help="Number of processors to request",\
default = '24', type =int)

parser.add_argument("-w","--walltime", help="Length of the job",\
default = '72', type =int)

parser.add_argument("-q","--queue", help="Requested queue (comp01, comp06, comp72)",\
default = 'comp72', type=str)

#We have created the objects (using positional and optional) into the argparse box
#parse the actual arguments
#access argument values via `args` variable
args = parser.parse_args()




#! /usr/bin/env python3

# set your variables

job_name = '<Job-Name>'
queue = 'comp01'
walltime = 1
num_nodes = 1
num_processors = 24

#print bash header
print('#!/bin/bash')

print()

#print SBATCH commands

print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition', args.queue)
print('#SBATCH --nodes='+ str (args.num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str (args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o aolawal_%j.out')
print('#SBATCH -e aolawal_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=aolawal@uark.edu')

print()

#purge all modules