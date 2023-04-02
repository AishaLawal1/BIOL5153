#! /usr/bin/env python3

#import modules
import argparse

#create an ArgumentParser object (like a box that holds an argument)
parser = argparse.ArgumentParser(description="This script returns the slurm script for HPC")

#add positional (required) arguments
parser.add_argument("job_name", help="First, enter the jobname  you wish to enter")
parser.add_argument("queue", help="Next, enter the queue name")
parser.add_argument("nodes",help="Then, enter number of nodes", type=int)
parser.add_argument("num_processors",help="Now, enter the number of processor", type=int)
parser.add_argument("walltime",help="Finally, enter walltime", type=int)

args = parser.parse_args()

print('#SBATCH --job-name=' + args.job_name,'\n#SBATCH --partition' + args.queue,'\n#SBATCH --nodes=' + str(args.nodes)\
,'\n#SBATCH --qos comp','\n#SBATCH --tasks-per-node=' + str(args.num_processors),\
'\n#SBATCH --time=' + str(args.walltime) + ':00:00',\
'\n#SBATCH  -o aolawal_%j.out','\n#SBATCH -e aolawal_%j.err','\n#SBATCH --mail-type=ALL')

