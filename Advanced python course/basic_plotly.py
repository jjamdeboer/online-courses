import pandas
import numpy
from plotly.offline import download_plotlyjs, plot, iplot, init_notebook_mode
import matplotlib
from matplotlib import pyplot
import cufflinks

cufflinks.go_offline()
init_notebook_mode(connected = True)

df = pandas.DataFrame(numpy.random.randn(400,4),columns = ['DURK','DURKUDURK', 'MURK', 'MURKUMURK'])
df_two = pandas.DataFrame({'DURKUDURKUDURK':['A', 'B', 'C'], 'MURKUMURKUMURK':[344444,1,345]})

# # FOR REGULAR PLOT, USE 'plot':
# df.plot()
# pyplot.show()
# # FOR INTERACTIVE PLOT, USE 'iplot':
# df.iplot()
# pyplot.show()

import plotly
import plotly.graph_objs as go

# plotly.offline.plot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": go.Layout(title="hello world")
# })

# plotly.offline.plot({
#     "data": [go.Histogram(x=df['DURK'])],
#     "layout": go.Layout(title="hello world")
# })

# ETC. ETC.

# CAN ALSO BE USED FOR GEOGRAPHICAL VISUALIZATION:

import plotly.plotly

# data = dict(type = 'choropleth',locations = ['AZ', 'NY', 'CA'],locationmode = 'USA-states', colorscale = 'Portland',text = \
# ['text 1', 'text 2', 'text 3'], z = [1.0,2.0,.30], colorbar = {'title': 'TITLE COLORBAR'})
# layout = dict(geo = {'scope':'usa'})

# plotly.offline.plot({
#     "data": [go.Choropleth(data)],
#     "layout": go.Layout(layout)
# })

df_usa = pandas.read_csv('2011_US_AGRI_Exports')

# TYPE OF PLOT, LOCATIONS OF THE MAP, Z ARE THE VALUES SHOWN, COLORBAR IS SHOWN NEXT TO MAP, MARKER GIVES SPACING BETWEEN STATES:
# data = dict(type = 'choropleth',locations = df_usa['code'],locationmode = 'USA-states', colorscale = 'YIOrRd',text = \
# df_usa['state'], z = df_usa['total exports'], colorbar = {'title': 'Millions USD'}, marker = {'line' : {'color' : 'rgb(255,255,255)','width':2}})
# layout = dict(title = 'Export USA',geo = {'scope':'usa','showlakes': True})

# plotly.offline.plot({
#     "data": [go.Choropleth(data)],
#     "layout": go.Layout(layout)
# })

df_world = pandas.read_csv('2014_World_GDP')

# print(df_world.head())
data = dict(type = 'choropleth',locations = df_world['CODE'],locationmode = 'World', colorscale = 'YIOrRd',text = \
df_world['COUNTRY'], z = df_world['GDP (BILLIONS)'], colorbar = {'title': 'Billions USD'}, marker = {'line' : {'color' : 'rgb(255,255,255)','width':2}})
layout = dict(title = 'GDP World',geo = {'scope':'world','showlakes': True})

plotly.offline.plot({
    "data": [go.Choropleth(data)],
    "layout": go.Layout(layout)
})