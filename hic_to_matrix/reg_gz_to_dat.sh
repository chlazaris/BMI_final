#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -M cl3011@nyumc.org
#$ -M cl3011@nyu.edu
#$ -m abe

# This is a script that converts the reg.gz
# files to the corresponding genome matrices
# The reg.gz files contain information on the
# interacting chromosomes. The script accepts
# only one argument which is the bin size 
# in bp.

BINSIZE = $1

# Start processing the files
echo "Converting .reg.gz to .dat"
for FILE in *.reg.gz
do
	echo "Now converting $FILE"
        cat $FILE | gunzip |\
        gtools_hic bin -v --bin-size $BINSIZE -g hg19.genome.bed --matrix > ${FILE%.reg.gz}.$BINSIZE.dat
	echo "$FILE converted to reg.gz!"
done
echo "Process complete!"




