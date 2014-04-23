
import pandas
import matplotlib as mpl
from matplotlib import pyplot

data = pandas.read_table('Hind3_NcoI_Ming_total_boxplot_final_input.txt', header=None)
data.columns=['chrom','corr','sample']

output = pandas.DataFrame.boxplot(data, column='corr', by='sample')

fig = output.get_figure()
fig.savefig('boxplot.pdf')