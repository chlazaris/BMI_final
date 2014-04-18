#!/bin/python

# Python script that accepts the
# output of gtools_hic as input and produces the  Hi-C matrix

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

############# INPUT AND OUTPUT ##################
# This is the output file
# (.dat) containing the genome matrix
out_file = sys.argv[1]

# The resolution
res = int(sys.argv[2])
#################################################

# Use pandas to import the csv file
# with the chromosomes and their sizes
data = pd.read_csv('hg19.genome.bed', sep='\t', header=None)
chrom_names = list(data.ix[:, 0])
chrom_sizes = list(data.ix[:, 2])

# Find the number of bins for each chromosome
bin_num = [int(ceil(chrom_size/res)) for chrom_size in chrom_sizes]

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
# chrom_index = [chrom_vector.index(chrom_name) for chrom_name in chrom_names]

############################################################################

# Read the input (the .reg.gz after
# processed with gunzip) line-by-line
for line in sys.stdin:
    line.rstrip("\n")
    line = re.split(r' ',line)
    first_chrom = line[0].split("\t")
    first_chrom = first_chrom[1]
    first_bin = int(int(line[3])/res)
    sec_chrom = line[4]
    sec_bin = int(int(line[7])/res)
    #print(first_chrom, first_bin, sec_chrom, sec_bin)

    # Check if both chromosomes are in the
    # chromosome vector generated from the .bed file
    if first_chrom in chrom_names and sec_chrom in chrom_names:
        # Now add elements to the matrix
        # First find the coordinates i,j
        # where the entry will be put (correct bin)
        i = chrom_vector.index(first_chrom) + int(first_bin)
        j = chrom_vector.index(sec_chrom) + int(sec_bin)
        # Now populate the matrix
        genome_matrix[i, j] += 1

        if i != j:
            genome_matrix[j, i] += 1
        else:
            pass
    else:
        pass

# Now write the resulting matrix to a file
np.savetxt(out_file, genome_matrix, fmt="%d", delimiter=' ')
