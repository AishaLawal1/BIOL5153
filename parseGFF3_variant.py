#! /usr/bin/env python3
#This is the class revision of the homework. Previous works were names 'parseGFF.py' and 'parseGFF2.py'
#import modules

import argparse
import csv
from Bio import SeqIO

#create an ArgumentParser object (like a box that holds an argument)

parser = argparse.ArgumentParser(description= "This script opens and reads a GFF file")

#add positional (required) arguments

parser.add_argument("gff",help="enter the gff", type=str)
parser.add_argument("fasta",help="enter the FASTA file", type=str)

args = parser.parse_args()

#open the gff file
with open(args.gff) as x:

	# create a csv reader object. we are using the csv module here
	reader = csv.reader(x, delimiter='\t')
	#when we use with, the object opens as a list

	#loop over all the lines in the file and remove line breaks
	# x is an object that has many lines. so we are looping over the lines
	for line in reader:
	
	#skip blank lines
    #this return true if the only character on the line is a newline character, usually for an empty line	
		
		if not line:
			continue 
		
	#else it's not a blank line
		else:

		#line = line.strip()
		#columns = line.split('\t')
#the split function breaks up the column in the  line, we can use the join function to put them back together			
#Name each columns in the dataset

			organisms = line[0]
			source = line[1]
			feature_type = line[2]
			start = int(line[3])
			end = int(line[4])
			length = line[5]
			strand = line[6]
			attributes = line[8]
		 
		#add the length to column 5
			line[5] = str(end - start + 1)
			line[5] = length
			new_line = '\t'.join(line)  
#to do the join, columns needs to be a string.hence we needed to convert it to string (that's why we used str)
		
		print(new_line)
		
	