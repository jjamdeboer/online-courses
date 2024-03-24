#MODULE FOLIUM CAN BE USED FOR GEOSPATIAL DATA
import matplotlib
import matplotlib.pyplot as pyplot
import pandas
import folium

#TILES ARE STYLES, AS: 'Mapbox Bright', 'Stamen Terrain', 'Stamen Toner', 'OpenStreetMap', 'Mapbox Control Room'
durk = folium.Map(location = (0,0), tiles='Stamen Toner', zoom_start = 4)
#MARKERS, CIRCLES AND CIRCLEMARKERS CAN BE ADDED TO THE MAP
folium.Marker((-10,-10), popup='<i>Mt. Hood Meadows</i>', tooltip='YES', fill=False).add_to(durk)
folium.Circle((10,10), popup='<i>Mt. Hood Meadows</i>', tooltip='MURK', fill=False, color='yellow',radius=1e6).add_to(durk)
folium.CircleMarker((-10,10), popup='<i>Mt. Hood Meadows</i>', tooltip='DURK', fill=True, color='crimson', fill_color= 'green', radius=20).add_to(durk)

#ALSO CHLOROPLETH MAPS ARE POSSIBLE, IN WHICH MAPS ARE SHADED

durk.save(outfile='map.html')
