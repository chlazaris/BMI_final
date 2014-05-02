#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -M cl3011@nyumc.org
#$ -m abe

# load python on the cluster
# module load python/2.6

# This is a bash script that calls hic_to_matrix.py
# to convert reg.gz files to the corresponding genome matrices.
# The reg.gz files contain information on the
# interacting chromosomes. The script accepts
# only one argument which is the bin size 
# in bp.

BINSIZE=$1 # Give the resolution in bp (eg 1024000)

# Start processing the files
echo "Converting .reg.gz to .dat"
for FILE in *.reg.gz
do
	echo "Now converting $FILE"
	# unzip the input file and pass
	# it to the hic_to_matrix to create
	# the matrix (hic_to_matrix accepts
	# standard input as input and the name
	# of the output as well as the binsize
	# as arguments).
    cat $FILE | gunzip | python hic_to_matrix.py ${FILE%.reg.gz}.dat ${BINSIZE}    
	echo "$FILE converted to matrix ${FILE%.reg.gz}.dat!"
done
echo "Process complete!"




