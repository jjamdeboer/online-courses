#CLUSTERING CAN BE USED FOR: EXPLORATORY DATA ANALYSIS, SUMMARIES, OUTLIER DETECTION, FINDING DUPLICATES, PRE-PROCESSING
#CLUSTERING CAN BE DONE: PARTITION-BASED (RELATIVELY EFFICIENT, K-MEANS/K-MEDIAN), HIERARCHICALLY (NOT SO EFFICIENT, PRODUCES TREES, AGGLOMERATIVE/DIVISIVE CLUSTERING), DENSITY-BASED (NOT EFFICIENT, VERSATILE, DBSCAN)

#FOR K-MEANS/K-MEDIAN CLUSTERING, THE EVALUATION CAN BE DONE EXTERNALLY (IF LABELS ARE PRESENT) OR INTERNALLY (CALCULATING THE TOTAL DISTANCE OF ALL POINTS FROM THEIR RESPECTIVE CENTROIDS)
#ELBOW-METHOD OFTEN USED TO DETERMINE OPTIMAL NUMBER OF CLUSTERS

#IN HIERARCHICAL CLUSTERING, DIVISIVE IS TOP-DOWN (STARTING FROM ALL THE DATA WORKING DOWNWARDS), AGGLOMERATIVE STARTS WITH CATEGORIES THAT NEED TO BE CLUSTERED
#IN HIERARCHICAL CLUSTERING, DISTANCE BETWEEN CLUSTERS CAN BE SINGLE-LINKAGE (MINIMUM BETWEEN ALL THE POINTS OF THE TWO CLUSTERS), COMPLETE-LINKAGE (MAXIMUM), AVERAGE-LINKAGE (AVERAGE OF ALL DISTANCES), CENTROID-LINKAGE (DISTANCE BETWEEN CENTROIDS)
#ADVANTAGES: DOES NOT HAVE HYPERPARAMETERS, EASY TO IMPLEMENT/UNDERSTAND, DENDROGRAM IS EASY; DISADVANTAGES: ALL STEPS ARE IRREVERSIBLE, SLOW, SOMETIMES DIFFICULT TO IDENTIFY NUMBER OF CLUSTERS IN DENSE DENDROGRAM
#K-MEANS VERSUS HIERARCHICAL: EFFICIENT - SLOW, HYPERPARAMETER - NO HYPERPARAMETER, GIVES FIXED PARTITIONING: K, GIVES DIFFERENT NUMBER OF CLUSTERS BASED ON RESOLUTION, DEPENDS ON INITIALIZATION - INDEPENDENT OF INITIALIZATION

#FOR NON-SPHERICAL CLUSTERING TECHNIQUES, DENSITY-BASED MIGHT BE MORE FIT, SINCE THIS CAN DETECT ODD-SHAPED CLUSTERS AND IT CAN DETECT OUTLIERS
#DENSITY-BASED SPATIAL CLUSTERING OF APPLICATIONS WITH NOISE (DBSCAN) NEEDS AS HYPERPARAMETERS A RADIUS AND MINIMUM NUMBER OF NEIGHBOURS WITHIN THAT RADIUS
#POINTS THAT HAVE THE MINIMUM NUMBER OF NEIGHBOURS ARE CORE POINTS, THOSE THAT ARE CONNECTED VIA THE NEIGHBOURS FORM A CLUSTER; OTHER POINTS ARE CONSIDERED OUTLIERS
#THE NUMBER OF CLUSTERS IS NOT PRE-SPECIFIED AS IN K-MEANS/K-MEDIAN