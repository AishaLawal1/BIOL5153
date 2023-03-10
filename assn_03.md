---
title: "BIOL5153_Assignment3"
author: "Aishat Lawal"
date: "2023-03-10"
output: html_document
---
To change into the "Desktop" directory where 'mt_genomes' is a sub-subdirectory of "watermelon_files" directory on local machine. 
``` {r}
  cd ~/Desktop
```

Answer_1: 

To upload "mt_genomes" directory from local machine to the AHPCC cluster in /storage/aolawal called mt_genomes

``` {r}
 rsync -avz watermelon_files/mt_genomes/ aolawal@hpc-portal2.hpc.uark.edu:/storage/aolawal/mt_genomes
```

Answer_2: 

To upload "unknown.fa" file containing the unknown sequence from local machine

```{r}
 scp unknown.fa aolawal@hpc-portal2.hpc.uark.edu:/storage/aolawal/mt_genomes/unknown.fa
```

To ssh into the AHPCC cluster 

```{r}
 ssh aolawal@hpc-portal2.hpc.uark.edu
```

To changed into the "storage" working directory on the HPC, where the uploaded mt_genomes directory now sits.

```{r}
 cd /storage/aolawal/mt_genomes
```

Answer_3: 

Nano was used to create a slurm script named "blast.slurm", essentially to purge the modules, load a blast module (BLASTN 2.13.0+) and concatenate all the genomes in mt_genomes directory into a single file called ‘genomes.fas'. 

Also, to create a blast database of all the genomes and the unknown sequence (unknown.fa) was searched  against the created database to generate a new output file named "unknown.vs.genomes.blastn". 

```{r}
#!/bin/bash
#SBATCH --job-name=blast-mt_genomes
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=1
#SBATCH --time=0:02:00
#SBATCH -o blast-mt_genomes_%j.out
#SBATCH -e blast-mt_genomes_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=aolawal@uark.edu

 export OMP_NUM_THREADS=32

 module purge
 module load blast/2.13.0+bin

 cd $SLURM_SUBMIT_DIR

 cat *.fasta > genomes.fas
 makeblastdb -in genomes.fas -dbtype nucl
 blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn
```

To submit slurm job on HPC and check the progress of the job

```{r}
 sbatch blast.slurm 

 squeue -u aolawal
```

Answer_4: 

To synchronize the remote mt_genomes, which contains the new output file (unknown.vs.genomes.blastn) and the local version of mt_genomes

```{r}
 rsync -av aolawal@hpc-portal.uark.edu:/storage/aolawal/mt_genomes ~/Desktop/watermelon_files           
```

Answer_5

i. The run time for the slurm job was 3 seconds (as shown in the email notification)

ii. The closest match in the database was Cucurbita genome


**The output file can be viewed on HPC via this path : /storage/aolawal/mt_genomes**



