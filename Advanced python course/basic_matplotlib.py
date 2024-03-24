# matplotlib.org HAS GOOD DOCUMENTATION

import matplotlib
from matplotlib import pyplot
import numpy

# AT THE END OF FIGURE STATE pyplot.show()

# CAN DO IT FUNCTIONALLY:

# LINEWIDTH CAN BE ABBREVIATED TO LW, LINESTYLE CAN BE ABBREVIATED TO LS, ALPHA DETERMINES THE TRANSPARANCY, 
# LABEL IS IMPORTANT FOR LEGEND, MARKER IS TO MARK WHERE DATAPOINTS ARE:
pyplot.plot(numpy.linspace(0,900,65),numpy.linspace(-90,50,65)**4, label = 'DURK', color = 'y', linewidth = 15, 
alpha = 0.2, linestyle = '--', marker = 'o', markersize = 20)
pyplot.plot(numpy.linspace(0,900,65),numpy.linspace(-10,50,65)**9,label = 'DURK2', color = 'black', lw = 3, 
alpha = 2, ls = '-.', marker = 'x', markersize = 6)
axes = pyplot.gca()
axes.set_xlim([10,150])
axes.set_ylim([-1e9,1e9])
pyplot.xlabel("DURK")
pyplot.ylabel("DURKUDURK")
pyplot.title("DURKUDURKUDURK")
pyplot.legend()
pyplot.show()
# SAVING A FIGURE:
# pyplot.savefig("DURK")

# INSIDE SUBPLOT, THE ARGUMENTS ARE: NUMBER OF COLUMNS, NUMBER OF ROWS, THE PLOT YOU ARE REFERRING TO
pyplot.subplot(1,2,1)
pyplot.plot(numpy.linspace(0,900,65),numpy.linspace(-90,50,65)**2)
pyplot.xlabel("DURK")
pyplot.ylabel("DURKUDURK")
pyplot.title("DURKUDURKUDURK")
pyplot.subplot(1,2,2)
pyplot.plot(numpy.linspace(0,900,65),numpy.linspace(-10,50,65)**4)
pyplot.xlabel("DURK")
pyplot.ylabel("DURKUDURK")
pyplot.title("DURKUDURKUDURK")
# TO CREATE AXES THAT ARE FURTHER APART:
pyplot.tight_layout()
pyplot.show()
# SAVING A FIGURE:
# pyplot.savefig("DURK")

# OR OBJECT-ORIENTED (CREATE pyplot.figure(figsize=(WIDTH IN INCHES, HEIGHT IN INCHES),dpi = NUMBER OF PIXELS PER SQUARE INCH) 
# AND ADD AXES WITH "ONE PLOT" = FIGURE.add_axes([MINIMUM X-AXIS BETWEEN 0 AND 1, 
# MINIMUM Y-AXIS BETWEEN 0 AND 1, WIDTH X-AXIS BETWEEN 0 AND 1, HEIGHT Y-AXIS BETWEEN 0 AND 1]). CAN ADD SECOND PLOT WITH DIFFERENT RATIOS. 
# THEN SET NAMES WITH .set_xlabel(NAME X-AXIS), .set_ylabel(NAME Y-AXIS) 
# AND PLOTTING TWO ARRAYS IN THIS SET OF AXIS .plot(ARRAY FOR X-AXIS, ARRAY FOR Y-AXIS)
# AND SET THE TITLE WITH .set_title(NAME OF PLOT).

# FOR OO SUBPLOTS, USE "FIGURE NAME, AXIS NAME" = pyplot.subplots((nrows = )NUMBER OF ROWS, (ncols = )NUMBER OF COLUMNS, 
# figsize=(WIDTH IN INCHES, HEIGHT IN INCHES),dpi = NUMBER OF PIXELS PER SQUARE INCH). 
# REST IS SIMILAR, THE AXIS-VARIABLE IS AN ARRAY CONTAINING THE AXES FOR EVERY PLOT. CAN ADD AXES/PLOTS WITH AXIS[INDEX].plot(X-ARRAY,Y-ARRAY).