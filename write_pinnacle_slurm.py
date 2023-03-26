#! /usr/bin/env python3
jobname="#SBATCH --job-name=pinnacle_slurm"
queue="#SBATCH --partition comp01"
number_of_nodes="#SBATCH --nodes=1"
number_of_processors="#SBATCH --tasks-per-node=1"
walltime="#SBATCH --time=0:02:00"

print(jobname)
print(queue)
print(number_of_nodes)
print(number_of_processors)
print(walltime)
