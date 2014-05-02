#!/bin/python 

# import necessary modules
import pandas
import matplotlib as mpl
from matplotlib import pyplot
import sys

# Get input file as argument
input_file = sys.argv[1]

data = pandas.read_table(input_file, header=None)
data.columns=['chrom','Spearman correlation','sample']

# sample = ['HindIII_1_2_flt','NcoI_1_2_flt','HindIII_NcoI_1_flt','HindIII_NcoI_2_flt',
# 'HindIII_1_2_cor','NcoI_1_2_cor','HindIII_NcoI_1_cor','HindIII_NcoI_2_cor']

output = pandas.DataFrame.boxplot(data, column='Spearman correlation', by='sample', rot=45, fontsize=6, grid=False)

fig = output.get_figure()
out_file = input_file.split("_")[0] + "_" + input_file.split("_")[1] + ".pdf"
fig.savefig(out_file)