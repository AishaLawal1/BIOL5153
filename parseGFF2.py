#! /usr/bin/env python3

#import modules

import argparse

#create an ArgumentParser object (like a box that holds an argument)

parser = argparse.ArgumentParser(description= "This script opens and reads a GFF file")

#add positional (required) arguments

parser.add_argument("gff",help="enter the gff", type=str)
parser.add_argument("fasta",help="enter the FASTA file", type=str)

args = parser.parse_args()

#open the gff file
with open(args.gff) as x:

#loop over all the lines in the file and remove line breaks

	for line in x:
		line = line.rstrip('\n')
		y = line
		for output in y:
			output = line.rstrip()

#separate each lines into columns using 			
			z = output.split('\t')
			print(z)
			
		
