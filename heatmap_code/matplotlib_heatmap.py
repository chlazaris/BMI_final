#start with

ipython --pylab

import numpy
column_labels = list('ABCD')
row_labels = list('WXYZ')
data = numpy.random.rand(4,4)


Making the heatmap is easy enough in matplotlib:



from matplotlib import pyplot as plt
heatmap = plt.pcolor(data)


And I even found a colormap arguments that look about right: heatmap = plt.pcolor(data, cmap=matplotlib.cm.Reds)