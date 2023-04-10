#! /usr/bin/env python3

#import modules

import argparse

#create an ArgumentParser object (like a box that holds an argument)

parser = argparse.ArgumentParser(description="This script opens and reads a GFF* file)

#add positional (required) arguments

parser.add_argument("file_name",help="enter the file name", type=str)
parser.add_argument("FASTA_file",help="enter the FASTA file", type=str)

args = parser.parse_args()

file = covid.gff
open (file)

for value in file:
print(value)