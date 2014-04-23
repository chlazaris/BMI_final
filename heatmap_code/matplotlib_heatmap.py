#!/bin/python

import matplotlib
matplotlib.use('Agg') # very important. It wan't try to graph it
from matplotlib import pyplot as plt
import numpy as np
import sys

# The scripts takes one
# argument which is the input matrix
input_file = sys.argv[1]

# Load the data from a saved matrix
data = np.loadtxt(input_file, delimiter=' ')

# Extract the parts of the name that will 
# be used to name the plot
input_f_parts = input_file.split('.')
heatmap_title_part1 = [input_f_parts[0] + input_f_parts[1] + input_f_parts[2]]

# Extract the resolution
# and get it in kb
res=int(input_f_parts[5])
res_kb=int(res/1000)

heatmap_title = '.'.join(heatmap_title_part1) + ' ' + ('(%dkb)' %res_kb)

fig = plt.figure()
heatmap = plt.pcolor(data, cmap=matplotlib.cm.Reds)
fig.set_size_inches(5,5)
fig.suptitle(heatmap_title)
heatmap.axes.get_xaxis().set_ticks([])
heatmap.axes.get_yaxis().set_ticks([])
plt.xlabel("%dkb genome bins" %res_kb)
plt.ylabel("%dkb genome bins" %res_kb)

# Set up the name of the output file
out_file = input_file.strip('dat')
fig.savefig(out_file + 'heatmap.tif',dpi=72)
