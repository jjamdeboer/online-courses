#  AUTOENCODERS>>>

#  AUTOENCODERS ARE MOST OFTEN USED AS AN UNSUPERVISED TECHNIQUE, THEREFORE CLASSIC EVALUATION IS NOT HAPPENING
#  USE CASES ARE DIMENSIONALITY REDUCTION (LIKE PRINCIPAL COMPONENT ANALYSIS/PCA) AND NOISE REMOVAL
#  AN AUTOENCODER IS SUPPOSED TO REPRODUCE THE INPUT AT THE OUTPUT LAYER
#  THIS MEANS THAT THEIR RESPECTIVE SIZES OF THESE LAYERS ARE IDENTICAL, CONTRARY TO REGULAR NETWORKS
#  THE SHAPE OF AN AUTOENCODER IS ALWAYS A FUNNEL: ENCODING -> DECODING
#  FOR DIMENSIONALITY REDUCTION, ONE TRAINS THE FULL AUTOENCODER, BUT THEN ONLY USE THE ENCODER
#  FOR NOISE REDUCTION, ONE TRAINS AND USES THE FULL AUTOENCODER


# <<<

################################################################################
##### CODE FOR AUTOENCODER FOR DIMENSIONALITY REDUCTION
################################################################################

#  IMPORTS>>>

import os
#  MAKE TENSORFLOW REDUCE ITS EXAGARATING VERBOSITY
#  0 IS DEFAULT (NONE), 1 FOR INFO, 2 FOR WARNINGS AND 3 FOR EVEN SURPRESSING ERRORS
os.environ[ 'TF_CPP_MIN_LOG_LEVEL' ] = '1'
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler as MMS
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
#  STOCHASTIC GRADIENT DESCENT
from tensorflow.keras.optimizers import SGD


# <<<

#  DATA>>>

#  X IS THE TWO-DIMENSIONAL DATA, Y IS THE LABEL/CLUSTER THESE POINTS BELONG TO
x,label = make_blobs(
    n_samples = 300,
    n_features = 2,
    centers = 2,
    cluster_std = 1.0,
)
#  NOTE THAT THIS DIMENSION IS RANDOM, SO THE AUTENCODER IS SUPPOSED TO MOSTLY IGNORE THIS DIMENSION
z = pd.Series( np.random.normal( size = len( x ) ) )
data = pd.DataFrame( x )
data = pd.concat( [ data, z ], axis = 1 )
scaler = MMS()
data = scaler.fit_transform( data )


# <<<

#  MODEL>>>

encoder = Sequential([
    Dense( units = 2, activation ='relu', input_shape = [3] )
])
decoder = Sequential([
    Dense( units = 3, activation ='relu', input_shape = [2] )
])
#  THIS SYNTAX IS BENEFICIAL FOR SPLITTING UP THE ENCODER AND DECODER-PART
autoencoder = Sequential([ encoder, decoder ])
autoencoder.compile( optimizer = SGD( lr = 1.5 ), loss = 'mse' )


# <<<

#  TRAINING>>>

autoencoder.fit( data, data, epochs = 5 )


# <<<

#  VISUALIZING THE RESULTS>>>

data = pd.DataFrame( data, columns = [ 'x', 'y', 'z' ] )
reduced_data = encoder.predict( data )
reduced_data = pd.DataFrame( reduced_data, columns = [ 'x_reduced', 'y_reduced' ] )

canvas, axes = plt.subplots( figsize = ( 14, 8 ), nrows = 1, ncols = 2 ) 
axes[0].scatter( 
    data[ 'x' ],
    data[ 'y' ],
    c = label,
)
axes[1].scatter( 
    reduced_data[ 'x_reduced' ],
    reduced_data[ 'y_reduced' ],
    c = label,
)
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].set_title("Initial Clusters")
axes[1].set_xlabel("X")
axes[1].set_ylabel("Y")
axes[1].set_title("Predicted Clusters")
plt.tight_layout()
plt.show()


# <<<

