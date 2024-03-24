# REDUCING DIMENSIONALITY OF THE DATASET IN ORDER TO EXPLAIN MOST OF THE VARIANCE
# OFTEN THE PRINCIPAL COMPONENT IS THE LINEAR REGRESSION HYPERPLANE AND THE PLANE PERPENDICULAR TO THAT PLANE
# THE ALGORITHM IS VERY SENSITIVE TO SCALING OF THE VARIABLES, SO USUALLY ALL THE FEATURES ARE SET TO STANDARD NORMAL DISTRIBUTION
# THE GOALS IS OFTEN CLEARER VISUALIZATION OF THE DATASET

# FOR SCALING USE: 
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit("dataframe")
# scaled_data = scaler.transform("dataframe")

# FOR PRINCIPAL COMPONENT ANALYSIS:
# from sklearn.decomposition import PCA
# pca = PCA(n_components = "number of components you want to keep")
# pca.fit(scaled_data)
# pca_two = pca.transform(scaled_data)