################################################################################
########## CODE
################################################################################

########## IMPORTS>>>

import os
#  MAKE TENSORFLOW REDUCE ITS EXAGARATING VERBOSITY
#  0 IS DEFAULT (NONE), 1 FOR INFO, 2 FOR WARNINGS AND 3 FOR EVEN SURPRESSING ERRORS
os.environ[ 'TF_CPP_MIN_LOG_LEVEL' ] = '1'  
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import MinMaxScaler as MMS
from sklearn.metrics import mean_absolute_error as mae, mean_squared_error as mse
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# <<<

########## DATA>>>

df = pd.read_csv( 'kc_house_data.csv' )
#  NOTE THAT EXPANSION OF THE DATE INTO NUMERICAL COLUMNS CAN BE ACHIEVED AS SUCH
df[[ 'month', 'year']] = df[[ 'date' ]].apply( lambda x: x.values[ 0 ].split( '/' )[ 0::2 ], axis = 1, result_type = 'expand' )
df[ 'renovated' ] = ( df[ 'yr_renovated' ] != 0 ).astype( int )
df[ 'basement' ] = ( df[ 'sqft_basement' ] != 0 ).astype( int )
#  print( df[[ 'renovated', 'yr_renovated', 'basement', 'sqft_basement' ]].head() )
#  REMOVE NON-NUMERICAL AND/OR UNINTERESTING COLUMNS
df.drop( [ 'id', 'date', 'zipcode', 'yr_renovated', 'sqft_basement' ], axis = 1, inplace = True )
df.info()


# <<<

########## ENGINEERING>>>

#  DEFINE A SCALER THAT CAN BE FIT ON THE FEATURES
scaler = MMS()
#  NOTE THAT FEATURES AND TARGET CAN BE DEFINED AS SUCH AND THAT THE FEATURES NEED TO BE A NUMPY ARRAY RATHER THAN A DATAFRAME
x = df.drop( 'price', axis = 1 ).values
y = df[ 'price' ]
#  NOTE THAT KERAS NEEDS NUMPY-ARRAYS, SO X NEEDS TO BE CONVERTED, Y IS IN THE RIGHT FORMAT ALREADY
#  FURTHERMORE, X NEEDS TO BE TRANSFORMED, SINCE OTHERWISE VANISHING/EXPLODING GRADIENTS MAY OCCUR
x = scaler.fit_transform( x )
xtr, xte, ytr, yte = tts( x, y, test_size = .3 )


# <<<
 
########## MODEL>>>

#  BUILDING A MODEL CAN BE DONE IN TWO WAYS: DEFINING A SEQUENTIAL MODEL WITH FULLY-CONNECTED/DENSE LAYERS AND A RELU-ACTIVATION:
model = Sequential([ 
    #  LAYER 1
    Dense( 19, activation = 'relu' ),
    #  THIS IS THE FRACTION OF NEURONS THAT GETS SWITCHED OFF RANDOMLY AFTER ONE EPOCH
    #  HELPS AGAINST OVERFITTING AND INCREASES THE TRAINING SPEED
    Dropout( .3 ),
    #  LAYER 2, ETC.
    Dense( 30, activation = 'relu' ),
    Dropout( .3 ),
    Dense( 30, activation = 'relu' ),
    Dropout( .3 ),
    Dense( 30, activation = 'relu' ),
    Dropout( .3 ),
    Dense( 10, activation = 'relu' ),
    Dropout( .3 ),
    #  NOTE THAT THE ACTIVATION FOR CLASSIFICATION PROBLEMS SHOULD BE 'sigmoid' FOR THE LAST LAYERS
    #  FOR MULTICLASS CLASSIFICATION IT SHOULD BE 'softmax'
    Dense( 1 ),
])
#  THE LOSS FOR MULTI-CLASSIFICATION IS 'categorical_crossentropy', FOR BINARY CLASSIFICATION 'binary_crossentropy'
model.compile( optimizer = 'adam', loss = 'mse' )
#  OTHER METHOD IS MORE OOP:
#  model = Sequential()
#  model.add( Dense( 4, activation = 'relu' ) )
#  model.add( Dense( 3, activation = 'sigmoid' ) )
#  model.add( Dense( 3, activation = 'relu' ) )
#  model.add( Dense( 1 ) )
#  model.compile( optimizer = 'adam', loss = 'mse' )


# <<<

########## FITTING>>>

#  DEFINE A MANNER OF STOPPING EARLY ONCE THE VALIDATION ERROR STARTS INCREASING ONCE AGAIN
stopper = EarlyStopping( 
    monitor = 'val_loss', 
    mode = 'min', 
    patience = 50, 
    verbose = 0 
)
#  EPOCHS IS THE NUMBER OF TIMES THE NETWORK GOES THROUGH THE WHOLE DATA SET
#  VALIDATION IS VALIDATING THE TRAINING DOESN'T GO OFF IN THE MIDDLE AND BATCH SIZE IS MAKING IT FASTER FOR LARGER SETS
model.fit( 
    xtr, 
    ytr, 
    epochs = 800, 
    verbose = 0, 
    validation_data = ( xte, yte ), 
    #  BATCH SIZES ARE OFTEN POWER OF 2
    batch_size = 128,
    #  THIS MAKES SURE THAT TRAINING STOPS ONCE THE VALIDATION ERROR STARTS INCREASING AGAIN AFTER 50/PATIENCE ROUNDS
    callbacks = [ stopper ]
)
#  VISUALIZING THE LOSS OVER TIME, NOTE THAT THE VALIDATION DATA IS NOW SHOWN AS WELL
#  NOTE THAT THE NUMBER OF EPOCHS WAS INDEED INFLUENCED BY THE CALLBACK
pd.DataFrame( model.history.history ).plot()
plt.show()
#  NOTE THAT THIS GIVE MSE
print( 'MSE: ', model.evaluate( xte, yte, verbose = 0 ) )
y_predict = pd.Series( model.predict( xte ).flatten() )
#  VISUALIZING THE PREDICTION:
durk = pd.concat([ y_predict, yte.reset_index( drop = True ) ], axis = 1 )
durk.columns = [ 'prediction', 'original' ]
sns.lmplot( y = 'prediction', x = 'original', data = durk )
plt.show()
#  FOR OTHER METRICS, ONE CAN ALSO USE:
print( 
    'MSE: ', a := mse( y_predict, yte ),
    '\n',
    'RMSE: ', np.sqrt( a ),
    '\n',
    'MAE: ', mae( y_predict, yte ),
)


# <<<

