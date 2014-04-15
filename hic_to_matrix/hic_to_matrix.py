#!/bin/python

# Python script that accepts the output of gtools_hic 
# as input and produces the  Hi-C matrix

# Import what you will need
from __future__ import division
from math import ceil
import pandas as pd
import numpy as np
from itertools import repeat
from itertools import izip as zip, count

########### FUNCTIONS #################

# Function to find bins
'''
This function accepts a list with
the chromosome sizes as input and
returns another with the corresponding
number of bins
'''


def bin_calc(x):
    return [int(ceil(item/res)) for item in x]

#######################################

# Define resolution
res = 1000000

# Use pandas to import the csv file
# with the chromosomes and their sizes
colnames = ['chrom', 'size']
data = pd.read_csv('hg19_chr_sizes.csv')
chrom_names = list(data.ix[:, 0])
chrom_sizes = list(data.ix[:, 1])

# Find the number of bins
bin_num = bin_calc(chrom_sizes)

# Create the chromosome vector
chrom_vector = [list(itertools.repeat(chrom_names,bin_num)) for chrom_names,bin_num in zip(chrom_names,bin_num)]
# Flatten the list of lists into one list
chrom_vector = [item for sublist in chrom_vector for item in sublist]
chrom_vec_size = len(chrom_vector)

# Now initialize the genome matrix
# (all zeros)
genome_matrix = np.zeros(shape=(chrom_vec_size, chrom_vec_size))

# Get the first occurence of a chrom_name in chrom_vector
# (the corresponding indices)
chrom_index = [chrom_vector.index(chrom_name) for chrom_name in chrom_names]

