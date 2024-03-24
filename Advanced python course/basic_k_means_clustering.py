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
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
# FOR CREATING ARTIFICIAL (CLUSTERED) DATA:
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

data = make_blobs(n_samples = 200, n_features = 2, centers = 4, cluster_std = 1.8)

cluster = KMeans(n_clusters = 4)
cluster.fit(data[0])

pyplot.figure(figsize = (10,6))
pyplot.subplot(1,2,1)
pyplot.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap = "magma")
pyplot.title("Original data")
pyplot.subplot(1,2,2)
pyplot.scatter(data[0][:,0], data[0][:,1], c = cluster.labels_, cmap = "magma")
pyplot.title("K Means Clustered")
pyplot.show()