#  IMPORTANT TO NOTE! SEABORN CAN BE COMBINED WITH MATPLOTLIB TO CREATE PLOTS, FIGURES, TITLES, ETC. AND USE SEABORN FOR THE ACTUAL PLOT ITSELF; ALL OPTIONS ARE OPEN
import matplotlib
from matplotlib import pyplot
import seaborn
import numpy

# EXAMPLE DATASET:
tips = seaborn.load_dataset('tips')

# MATRIX PLOTS:
flights = seaborn.load_dataset('flights')
print( "INFO OF THE TIPS: \n")
tips.info()
print( "\n\n\n" )
print( "INFO OF THE FLIGHTS: \n" )
flights.info()
# HEAT MAPS (SHOWS RELATIVE HEIGHT OF SQUARE MATRIX), FOR VALUES INSIDE HEAT MAP, USE ANNOT(ATION), COLOUR SCALE CMAP:
seaborn.heatmap( tips.select_dtypes( include = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] ).corr(), annot = True )
pyplot.show()
# PIVOT TABLE IS IMPORTANT DETAIL HERE! FOR COLOURS, USE MATPLOTLIB COLOUR MAP LINKS, 
# FOR ADDING LINES BETWEEN THE BLOCKS, USE LINEWIDTH AND LINECOLOR ARGUMENTS:
seaborn.heatmap(flights.pivot_table(index = 'month', columns = 'year', values = 'passengers', aggfunc = 'sum'), linewidth = 0.5, linecolor = 'white', cmap = 'magma')
pyplot.show()
# CLUSTERMAP ALSO AVAILABLE, BUT NOT A CLEAR TYPE, THERE standard_scale IS AVAILABLE IF YOU WANT TO NORMALIZE YOUR DATA ( = 1):

# GRIDS PLOTS:
iris = seaborn.load_dataset('iris')
print( "\n\n\n" )
print( "INFO OF THE IRIS: \n")
iris.info()
# PAIRGRID GIVES MORE CUSTOMIZATION OPTIONS OF THE PAIRPLOT. USE MAP, MAP_DIAG, MAP_UPPER, MAP_LOWER:
seaborn.set_style('white')
seaborn.PairGrid(iris, hue = 'species').map_diag(seaborn.histplot, kde = False).map_upper(pyplot.scatter).map_lower(seaborn.kdeplot,color = 'green').add_legend()
pyplot.show()
#  FACETGRID GIVES POSSIBILITY TO AUTOMATICALLY CREATE SUBPLOTS
seaborn.set_style("darkgrid")
seaborn.FacetGrid(tips, col = 'time', row = 'sex').map(seaborn.histplot,'total_bill')
pyplot.show()
seaborn.set_style('whitegrid')
seaborn.FacetGrid(tips, col = 'time', row = 'sex').map(seaborn.kdeplot,'total_bill','tip')
pyplot.show()

# STYLES CAN BE SET WITH .set_style() WITH darkgrid, whitegrid, dark, white, ticks.
# REGRESSION PLOTS (FITTING):
seaborn.set_style('dark')
seaborn.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'time')
pyplot.show()
# SIMILAR TO FACETGRID, BUT AUTOMATED. USE ASPECT FOR ASPECT RATIO AND SIZE FOR SIZE:
seaborn.set_style('ticks')
seaborn.lmplot(x = 'total_bill', y = 'tip', data = tips, col = 'time', row = 'sex', height = 7, aspect = 0.5)
pyplot.show()
