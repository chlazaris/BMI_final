#!/bin/python

# Import what is necessary
import sys
import re

fname = sys.argv[1]

# Open the file and read it

################ FUNCTIONS #####################
'''
This is a function that reads a file line-by-line,
strips the new-line character after each line and
returns a list where each element is a line.
'''
def read_f_line(fname):
    with open(fname) as f:
        for line in f:
            return [line.rstrip() for line in f]
################################################

fcontent = read_f_line(fname)

for line in fcontent:
    x = re.split(r'\t+', line)
    first_chrom = x[0].split(":")
    f_chrom_name = first_chrom[0]
    first_bin = first_chrom[1]
    sec_chrom = x[1].split(":")
    sec_chrom_name = sec_chrom[0]
    sec_bin = sec_chrom[1]   

    print (f_chrom_name, first_bin, sec_chrom_name, sec_bin)
