# matplotlib.org HAS GOOD DOCUMENTATION

import matplotlib
from matplotlib import pyplot
import numpy

# AT THE END OF FIGURE STATE pyplot.show()

# CAN DO IT FUNCTIONALLY:

# LINEWIDTH CAN BE ABBREVIATED TO LW, LINESTYLE CAN BE ABBREVIATED TO LS, ALPHA DETERMINES THE TRANSPARANCY (0-1), 
# LABEL IS IMPORTANT FOR LEGEND, MARKER IS TO MARK WHERE DATAPOINTS ARE:
#  FUNCTIONAL: PYPLOT.PLOT( X-ELEMENTS, Y-ELEMENTS, LABEL, COLOR, LINEWIDTH, ALPHA (TRANSPARENCY), LINESTYLE, MARKER, MARKERSIZE, E.A)
pyplot.plot(numpy.linspace(0,900,65),numpy.linspace(-90,50,65)**4, label = 'DURK', color = 'y', linewidth = 15, 
alpha = 0.2, linestyle = '--', marker = 'o', markersize = 20)
pyplot.plot(numpy.linspace(0,900,65),numpy.linspace(-10,50,65)**9,label = 'DURK2', color = 'black', lw = 3, 
alpha = .8, ls = '-.', marker = 'x', markersize = 6)
axes = pyplot.gca()
axes.set_xlim([10,150])
axes.set_ylim([-1e9,1e9])
pyplot.xlabel("DURK")
pyplot.ylabel("DURKUDURK")
pyplot.title("DURKUDURKUDURK")
#  NOTE HERE THAT THE LOCATION OF THE LEGEND IS SPECIFIED
pyplot.legend( loc = 'upper left' )
pyplot.show()
# SAVING A FIGURE:
# pyplot.savefig("DURK")

#  OBJECT-ORIENTED METHOD FOR MAKING THE SAME FIGURE
#  CREATES A BLANK CANVAS
canvas = pyplot.figure()
#  CREATES AXES AS PERCENTAGE OF RANGE OF X AND Y (XMIN, YMIN, X-SCALE, Y-SCALE)
axes = canvas.add_axes([ .15, .15, .8, .8 ])
axes.plot( numpy.linspace(0,900,65), numpy.linspace(-90,50,65)**4, label = 'DURK', color = 'y', linewidth = 15, 
alpha = 0.2, linestyle = '--', marker = 'o', markersize = 20)
axes.plot(numpy.linspace(0,900,65),numpy.linspace(-10,50,65)**9,label = 'DURK2', color = 'black', lw = 3, 
alpha = .8, ls = '-.', marker = 'x', markersize = 6)
#  axes = pyplot.gca()
axes.set_xlim([10,150])
axes.set_ylim([-1e9,1e9])
#  NOTE, THIS IS DIFFERENT FROM FUNCTIONAL FORM ABOVE
axes.set_xlabel("DURK")
axes.set_ylabel("DURKUDURK")
axes.set_title("OBJECT-ORIENTED DURKUDURKUDURK")
axes.legend()
axes2 = canvas.add_axes([ .2, .7, .2, .2 ])
axes2.plot( numpy.linspace(0,900,65), numpy.linspace(-90,50,65)**4, label = 'DURK', color = 'r', linewidth = 2, 
alpha = 0.2, linestyle = '--', marker = 'o', markersize = 4)
axes2.plot(numpy.linspace(0,900,65),numpy.linspace(-10,50,65)**9,label = 'DURK2', color = 'lightblue', lw = 3, 
alpha = .8, ls = '-.', marker = 'x', markersize = 6)
axes2.set_xlim([10,150])
axes2.set_ylim([-1e9,1e9])
axes2.set_title("SUBDURKDURKUDURK")
pyplot.show()

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

#  OBJECT-ORIENTED WAY TO CREATE SUBPLOTS
#  NOTE THAT AXES ARE ARRAY HERE, SO ONE CAN INDEX IT
#  NOTE THE ADDITIONAL FIGSIZE PARAMETER TO TWEAK THE SIZE OF THE FIGURE
canvas, axes = pyplot.subplots( figsize = ( 8, 4 ), nrows = 2, ncols = 1 )
axes[0].plot(numpy.linspace(0,900,65),numpy.linspace(-90,50,65)**2)
axes[0].set_xlabel("DURK")
axes[0].set_ylabel("DURKUDURK")
axes[0].set_title("OBJECT-ORIENTED DURKUDURKUDURK")
axes[1].plot(numpy.linspace(0,900,65),numpy.linspace(-10,50,65)**4)
axes[1].set_xlabel("DURK")
axes[1].set_ylabel("DURKUDURK")
axes[1].set_title("OBJECT-ORIENTED DURKUDURKUDURK")
# TO CREATE AXES THAT ARE FURTHER APART:
pyplot.tight_layout()
pyplot.show()

# OR OBJECT-ORIENTED (CREATE pyplot.figure(figsize=(WIDTH IN INCHES, HEIGHT IN INCHES),dpi = NUMBER OF PIXELS PER SQUARE INCH) 
# AND ADD AXES WITH "ONE PLOT" = FIGURE.add_axes([MINIMUM X-AXIS BETWEEN 0 AND 1, 
# MINIMUM Y-AXIS BETWEEN 0 AND 1, WIDTH X-AXIS BETWEEN 0 AND 1, HEIGHT Y-AXIS BETWEEN 0 AND 1]). CAN ADD SECOND PLOT WITH DIFFERENT RATIOS. 
# THEN SET NAMES WITH .set_xlabel(NAME X-AXIS), .set_ylabel(NAME Y-AXIS) 
# AND PLOTTING TWO ARRAYS IN THIS SET OF AXIS .plot(ARRAY FOR X-AXIS, ARRAY FOR Y-AXIS)
# AND SET THE TITLE WITH .set_title(NAME OF PLOT).

# FOR OO SUBPLOTS, USE "FIGURE NAME, AXIS NAME" = pyplot.subplots((nrows = )NUMBER OF ROWS, (ncols = )NUMBER OF COLUMNS, 
# figsize=(WIDTH IN INCHES, HEIGHT IN INCHES),dpi = NUMBER OF PIXELS PER SQUARE INCH). 
# REST IS SIMILAR, THE AXIS-VARIABLE IS AN ARRAY CONTAINING THE AXES FOR EVERY PLOT. CAN ADD AXES/PLOTS WITH AXIS[INDEX].plot(X-ARRAY,Y-ARRAY).
