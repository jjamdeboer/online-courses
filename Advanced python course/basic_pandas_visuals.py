import numpy
import pandas
import matplotlib
from matplotlib import pyplot
# BUT IF YOU IMPORT SEABORN, PLOTS LOOK NICER!
import seaborn

df1 = pandas.read_csv('df1',index_col = 0)
df2 = pandas.read_csv('df2')

df1['A'].hist()
pyplot.show()
df2.loc[4,:].hist()
pyplot.show()
# KIND CAN BE 'AREA' OR 'BOX' OR 'HIST' OR 'BAR' OR 'LINE' OR 'SCATTER' OR 'HEXBIN' (USE GRIDSIZE THEREIN TO CHANGE THE 'BIN' SIZE):
df1[['B','C']].plot(kind = 'kde')
pyplot.show()
df2.plot(kind = 'bar', stacked = True)
pyplot.show()
df1.plot(kind = 'line',x = df1.index,y = ['B','C'])
pyplot.show()
# FOR COLOR USE 'c', FOR SIZE USE 's':
df1.plot(kind = 'scatter', x = 'A', y = 'D',c = "A",cmap = 'magma', s = df1["D"]*100)
pyplot.show()
df1.plot(kind = 'hexbin', x = 'A', y = 'D',cmap = 'magma', gridsize = 25)
pyplot.show()