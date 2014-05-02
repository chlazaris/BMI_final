#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -M cl3011@nyumc.org
#$ -M cl3011@nyu.edu
#$ -m abe

module load python/2.6	

# Give the resolution
RES=$1

echo 'Start creating heatmaps...'
for FILE in *.$RES.dat
do
	echo "Creating heatmap for $FILE"
	python matplotlib_heatmap.py $FILE
	echo "Heatmap ready for $FILE"
done
