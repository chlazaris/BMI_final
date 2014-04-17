#!/bin/python

# Python script that accepts the output of gtools_hic 
# as input and produces the  Hi-C matrix

# Import what you will need
from __future__ import division
from math import ceil
import pandas as pd
import numpy as np
import itertools
from itertools import repeat
from itertools import izip as zip, count
import sys
import re
import os

##### INPUT AND OUTPUT ###############
# This file is the .reg.gz file 
input_file = sys.argv[1]
# The resulution
res = int(sys.argv[2])

# Get the intermediate file (fname) that will
# be used by the program to produce the final
# matrix (dat)
fname = input_file.rstrip("reg.gz") + (".txt")
os.system("""gtools_hic bin --bin-size %d %s > %s""" %(res, input_file, fname))

# This is the output file
# (.dat) containing the genome matrix
out_file = fname.rstrip("txt") + ("dat")

########### FUNCTIONS #################

# Function to read input file (gz)
'''
This is a function that reads a file line-by-line,
strips the new-line character after each line and
returns a list where each element is a line.
'''


def read_f_line(fname):
    with open(fname) as f:
       # for line in f:
         return [line.rstrip("\n") for line in f]

#######################################

# Use pandas to import the csv file
# with the chromosomes and their sizes
colnames = ['chrom', 'size']
data = pd.read_csv('hg19.genome.bed')
chrom_names = list(data.ix[:, 0])
chrom_sizes = list(data.ix[:, 1])

# Find the number of bins
bin_num = [int(ceil(chrom_size/res)) for chrom_size in chrom_sizes]
print bin_num

# Create the chromosome vector
chrom_vector = [list(itertools.repeat(chrom_name,bin_num)) for chrom_name,bin_num in zip(chrom_names,bin_num)]
# Flatten the list of lists into one list
chrom_vector = [item for sublist in chrom_vector for item in sublist]
chrom_vec_size = len(chrom_vector)

# Now initialize the genome matrix
# (all zeros)
genome_matrix = np.zeros(shape=(chrom_vec_size, chrom_vec_size), dtype=np.int)

# Get the first occurence of a chrom_name in chrom_vector
# (the corresponding indices)
chrom_index = [chrom_vector.index(chrom_name) for chrom_name in chrom_names]

############################################################################

# This file is the output
# of gtools_hic 
#fname = sys.argv[1]
# The resulution
#res = sys.argv[2]
# This is the output file
# (.csv) containing the genome matrix
#out_file = fname.rstrip("txt") + ("matrix.csv")

# Open the file and read it
# line by line
fcontent = read_f_line(fname)

for line in fcontent:
    x = re.split(r'\t+', line)
    first_chrom = x[0].split(":")
    f_chrom_name = first_chrom[0].strip("chr")
    first_bin = first_chrom[1]
    sec_chrom = x[1].split(":")
    sec_chrom_name = sec_chrom[0].strip("chr")
    sec_bin = sec_chrom[1]   

    #print (f_chrom_name, first_bin, sec_chrom_name, sec_bin)

    # Now add elements to the matrix
    # First find the coordinates i,j
    # where the entry will be put (correct bin)
    i = chrom_index[int(f_chrom_name)-1] + int(first_bin) - 1 
    j = chrom_index[int(sec_chrom_name)-1] + int(sec_bin) - 1

    # Now populate the matrix
    genome_matrix[i,j] += 1

    if i != j:
        genome_matrix[j,i] += 1
    else:
        pass 

# Now write the resulting matrix to a file
np.savetxt(out_file, genome_matrix, fmt="%d", delimiter=' ')
