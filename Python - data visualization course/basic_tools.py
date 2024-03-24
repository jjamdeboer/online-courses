#DARKHORSE ANALYTICS COMPANY THAT, WITH COOPERATION OF UNIVERSITY OF ALBERTA, DID A LOT OF RESEARCH ON VISUALIZATION; LESS IS MORE
#MATPLOTLIB MOST USED, MADE BY JOHN HUNTER BASED ON MATLAB, SO THE SCRIPTING ENVIRONMENT, PYPLOT, IS SIMILAR TO MATLAB
#MATPLOTLIB CONSISTS OF THREE LAYERS:
#- BACKEND LAYER (CANVAS): HAS THREE BUILT-IN CLASSES: FigureCanvas (AREA FOR FIGURE), Renderer (CREATES FIGURE ON CANVAS BY MEANS OF ARTIST), Event (HANDLES EVENTS IN THE CANVAS)
#- ARTIST LAYER (ARTIST): ALL PLOTS ARE ARTIST INSTANCES; TWO ARTIST OBJECTS: PRIMITIVE (LINE, RECTANGLE, TEXT) AND COMPOSITE (AXES, FIGURE)
#- SCRIPTING LAYER (PYPLOT): LIGHTER CODING THAN DIRECTLY MAKING ARTIST INSTANCES, BUT THIS CAN BE DONE, IN PRINCIPLE
import matplotlib
import matplotlib.pyplot as pyplot
import pandas

#BASIC FIGURE CREATION: A PYPLOT-OBJECT CAN HAVE SEVERAL ATTRIBUTES ADDED TO IT
#pyplot.plot(5,6,'o')
#pyplot.ylabel('Y')
#pyplot.xlabel('DURK')
#pyplot.title('DURK AND Y')
#pyplot.show()

#WITH SEABORN, WHICH HAS BUILT-IN MATPLOTLIB FEATURE, USE DATAFRAME.plot(kind = 'hist'/'line'/'area'/'bar'/'barh'/'pie'/'scatter'/...)
#THE .sort_values(keys = 'COLUMN NAME', ascending = True/False) GIVES MAXIMUM/MINIMUM VALUES ACORDING TO A SPECIFIED COLUMN
immigrants = pandas.read_excel('Canada.xlsx', sheet_name = 'Canada by Citizenship', skiprows = range(20), skipfooter = 2)
immigrants.set_index('OdName', inplace=True, drop = True)
for i in immigrants.columns:
    immigrants.rename(columns = {i: str(i)}, inplace = True)
immigrants = pandas.concat([immigrants, immigrants.loc[:,'1980':'2013'].sum(axis = 1)], axis = 1).rename(columns = {0: 'Total'})
print(immigrants.columns)
#print(immigrants['Total'].head())
#print(immigrants.head())
#OPTIONAL DIFFERENT STYLE FOR PLOTTING, A BIT CLEANER THAN DEFAULT STYLE
matplotlib.style.use('ggplot')
#immigrants['Total'].plot(kind = 'line')
#immigrants.loc[['Afghanistan','Algeria'], '1980':'2013'].transpose().plot(kind = 'box')
immigrants.loc[['Afghanistan','Algeria'], '1980':'2013'].transpose().plot(kind = 'area', stacked = False)
#FOOLING AROUND WITH SCATTER, NO FUN:
#immigrants.loc[:, '1980':'2013'].sum(axis = 0).to_frame().reset_index().astype('float').plot(kind = 'scatter', x = 'index', y = 0)
#PIE CHART + MOVING LEGEND AROUND:
#immigrants.groupby('AreaName',axis = 0).sum()['Total'].plot(kind = 'pie')
#.legend(loc='upper center', bbox_to_anchor=(0.5, 0),fancybox=True, shadow=True, ncol=3)
#pyplot.ylabel('Y')
#pyplot.xlabel('DURK')
#pyplot.title('DURK AND Y')
pyplot.show()

#MATPLOTLIB DOES NOT HAVE A BUILT-IN FEATURE FOR WAFFLE CHARTS (TILES PROPORTIONAL TO PROPORTION) OR WORD CLOUDS
