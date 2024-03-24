import matplotlib
from matplotlib import pyplot
import seaborn
import numpy

# EXAMPLE DATASET:
tips = seaborn.load_dataset('tips')

print("INFO OF EXAMPLE DATASET: \n")
tips.info()

# MAKING HISTOGRAM, KDE IS THE ESTIMATED LINE ON TOP OF THE HISTOGRAM, BINS IS NUMBER OF BINS:
durk = seaborn.distplot(tips['total_bill'], bins = 1000)
pyplot.show()
seaborn.distplot(tips['tip'], kde = False)
pyplot.show()
seaborn.kdeplot(tips['tip'])
pyplot.show()
# COMPARING TWO HISTOGRAM INPUT X-AXIS, Y-AXIS, DATASET, KIND (SCATTER, HEX, REG (REGRESSION), KDE (KERNEL DENSITY ESTIMATION)):
seaborn.jointplot('total_bill','tip',data=tips, kind = 'kde')
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
seaborn.factorplot(x = 'day', y = 'tip',hue = 'sex', data = tips, split = True, kind = 'violin')
pyplot.show()