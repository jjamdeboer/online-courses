# CLUSTERING SIMILAR DATA
# FIRST CHOOSE NUMBER K
# THEN ASSIGN EACH DATA POINT TO A CLUSTER
# THEN, FOR EACH CLUSTER CALCULATE CENTROID AND ASSIGN EACH POINT TO CLUSTER FOR WHICH CENTROID IS CLOSEST
# STOP THIS ALGORITHM IF THERE IS NO CHANGE IN CLUSTER COMPOSITION

# NO EASY WAY TO DETERMINE K BEFOREHAND, SOMETIMES VISUAL 'ELBOW'-METHOD OF SSE (SUM OF SQUARED ERRORS) OF THE CLUSTERS IS USED:
# EUCLIDEAN DISTANCE BETWEEN POINTS AND CENTROID SHOULD ALWAYS DECREASE, BUT MIGHT HAVE SOME SORT OF TRANSITION OR ELBOW, THAT'S THE RIGHT K-VALUE

import numpy
import pandas
import matplotlib
from matplotlib import pyplot
import seaborn
import sklearn
# FOR CREATING ARTIFICIAL (CLUSTERED) DATA:
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

data = make_blobs( n_samples = 200, n_features = 2, centers = 4, cluster_std = 1.8 )

cluster = KMeans(n_clusters = 4)
cluster.fit(data[0])

#  OOP-WAY
canvas, axes = pyplot.subplots( 1, 2, sharey = True, figsize = ( 10, 6 ) )
axes[0].set_title("Original data")
#  THIS IS HOW YOU WOULD ADD A LEGEND:
#  THIS CREATES AN ARRAY WITH EVENLY-SPACED RGB-VALUES FOR THE PALETTE CHOSEN, VERY NEAT!
colors = pyplot.cm.magma( numpy.linspace( 0, 1, 4 ) )
for i in range( 4 ):
    axes[0].scatter( data[0][data[1]==i][:,0], data[0][data[1]==i][:,1], color = colors[ i ], label = f'Cluster {i}' )
#  THIS IS WITHOUT THE LEGEND, BUT WITH THE RIGHT PALETTE AUTOMATICALLY
#  NOTE THAT C IS NOT THE SAME AT ALL AS COLOR, IT TAKES AN ARRAY FOR THE COLOR MAPPING
#  axes[0].scatter( data[0][:,0], data[0][:,1], c = data[1], cmap = "magma" )
axes[1].set_title("K Means Clustered")
axes[1].scatter(data[0][:,0], data[0][:,1], c = cluster.labels_, cmap = "magma")
axes[0].legend( loc = 'best' )
pyplot.tight_layout()
pyplot.show()

#  FUNCTIONAL-WAY
pyplot.figure(figsize = (10,6))
pyplot.subplot(1,2,1)
pyplot.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap = "magma")
pyplot.title("Original data")
pyplot.subplot(1,2,2)
pyplot.scatter(data[0][:,0], data[0][:,1], c = cluster.labels_, cmap = "magma")
pyplot.title("K Means Clustered")
pyplot.tight_layout()
pyplot.show()
