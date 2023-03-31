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

print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition',queue)
print('#SBATCH --nodes='+ str (num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=32')
print('#SBATCH --time=' + str(walltime) + ':00:00')
print('#SBATCH -o aolawal_%j.out')
print('#SBATCH -e aolawal_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=aolawal@uark.edu')

print()

#purge all modules

print('purge modules') 

