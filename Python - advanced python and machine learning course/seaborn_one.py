#  IMPORTANT TO NOTE! SEABORN CAN BE COMBINED WITH MATPLOTLIB TO CREATE PLOTS, FIGURES, TITLES, ETC. AND USE SEABORN FOR THE ACTUAL PLOT ITSELF; ALL OPTIONS ARE OPEN
import matplotlib
from matplotlib import pyplot
import seaborn
import numpy

# EXAMPLE DATASET:
tips = seaborn.load_dataset('tips')

print( "INFO OF EXAMPLE DATASET: \n" )
tips.info()

# MAKING HISTOGRAM, KDE IS THE ESTIMATED LINE ON TOP OF THE HISTOGRAM, BINS IS NUMBER OF BINS:
durk = seaborn.displot(tips['total_bill'], bins = 100)
pyplot.show()
seaborn.displot(tips['tip'], kde = False)
pyplot.show()
seaborn.kdeplot(tips['tip'])
pyplot.show()
# COMPARING TWO HISTOGRAM INPUT X-AXIS, Y-AXIS, DATASET, KIND (SCATTER, HEX, REG (REGRESSION), KDE (KERNEL DENSITY ESTIMATION)):
seaborn.jointplot(x = 'total_bill',y = 'tip',data = tips, kind = 'hex')
pyplot.show()
# SCATTERPLOT
seaborn.scatterplot(x = 'total_bill',y = 'tip',data = tips, hue = 'sex', style = 'time', size = 'size')
pyplot.show()
# COMPARING ALL COLUMNS IN YOUR DATA FRAME (HUE GIVES THE POSSIBILITY OF ADDING NON-NUMERICAL DATA, SUCH AS (BINARY) CATEGORIES):
seaborn.pairplot(tips,hue = 'sex')
pyplot.show()

# CATEGORICAL PLOTS 
# BARPLOT (STANDARD ESTIMATOR IS MEAN):
seaborn.barplot(x = 'sex',y = 'total_bill',data = tips,estimator = numpy.std)
pyplot.show()
# COUNTPLOT:
seaborn.countplot(x = 'smoker',data = tips)
pyplot.show()
# BOXPLOT (X CATEGORICAL, Y NUMERICAL), SWARMPLOT SIMILAR, BUT SHOWS DATA POINTS, NOT BOXES:
seaborn.boxplot(x = 'day', y = 'tip',hue = 'sex', data = tips)
seaborn.swarmplot(x = 'day', y = 'tip',hue = 'sex', data = tips)
pyplot.show()
# VIOLINPLOT SIMILAR, BUT SHOWING DISTRIBUTION (CAN SPLIT THE VIOLIN TO BE MORE EFFICIENT), ALSO STRIPPLOT SIMILAR CREATE A JITTER TO BE CLEARER:
seaborn.violinplot(x = 'day', y = 'tip',hue = 'sex', data = tips, split = True)
seaborn.stripplot(x = 'day', y = 'tip',hue = 'sex', data = tips,jitter = True)
pyplot.show()
# MOST GENERAL METHOD IS FACTORPLOT, WHICH YOU CAN SPECIFY TO BE ONE OF THE ABOVE PLOTS:
seaborn.catplot(x = 'day', y = 'tip',hue = 'sex', data = tips, split = True, kind = 'violin')
pyplot.show()
