################################################################################
########## HISTORY
################################################################################

#  NEURAL NETWORKS ARE BASED ON PERCEPTRONS, HISTORICALLY:
#      PERCEPTRONS ALREADY EXIST SINCE THE '50'S
#      BECAME LESS INTERESTING AFTER MINSKY PUBLISHED 'PERCEPTRON' IN 69: 
#          ARGUED THAT THE GENERAL COMPUTATIONAL POWER WAS INSUFFICIENT
#          STARTED THE AI-WINTER THAT LASTED UNTIL SOMEWHERE '90'S
#      REVIVAL AFTER BACKPROPAGATION TOOK OFF (INVENTED AND REINVENTED SEVERAL TIMES THROUGH '80'S AND '90'S)
#      LATER LU AND HANIN PROVED THAT ANY CONVEX CONTINUOUS FUNCTION CAN BE REPRESENTED BY A NEURAL NETWORK (UNIVERSAL APPROXIMATION THEOREM)


################################################################################
########## FUNCTIONALITY
################################################################################

#  NEURONS HAVE INPUT (DENDRITES) AND OUTPUT (AXONS), NEXT TO A CORE (NUCLEUS)
#  THE PERCEPTRON MIMICS THIS BEHAVIOUR, BY HAVING INPUT-FLOWS, CALCULATIONS AND THEN OUTPUT 
#      SINGLE PERCEPTRONS ARE INSUFFICIENT FOR DESIRED BEHAVIOUR, SO MULTIPLE LAYERS ARE NECESSARY
#      THEREFORE, OUPUT POSSIBLY BEHAVES AS INPUTS TO THE NEXT LAYERS OF PERCEPTRONS
#      FIRST LAYERS IS INPUT LAYER, LAST LAYER OUTPUT LAYER -- ALL THE INBETWEEN LAYERS ARE THE HIDDEN LAYERS
#      THE WIDTH IS HOW MANY PERCEPTRONS THERE ARE IN A LAYER, THE DEPTH HOW MANY LAYERS THERE ARE
#      THE HIDDEN LAYERS ARE THE MOST DIFFICULT TO INTERPRET
#      THE DEFINITION OF 'DEEP' IS IN FACT MORE THAN TWO HIDDEN LAYERS
#      SINGLE CLASSES AND REGRESSION CAN EASILY BE DONE WITH A SINGLY OUPUT NEURON; MUTLIPLE CLASSES WITH MULTIPLE OUTPUT NEURONS
#      MULTIPLE OUTPUT NEURONS CAN EITHER BE EXCLUSIVELY:
#          RESULTS INTO PROBABILITIES THAT ADD UP TO 1 VIA SOFTMAX (e^X/SUM(e^X))
#          HIGHEST SOFTMAX PROBABILITY WILL BE SELECTED
#      OR NON-EXCLUSIVELY:
#          HAVING A CUTOFF TO CLASSIFY AS CERTAIN CATEGORY
#      THE CALCULATIONS CAN BE VIEWED AS APPLYING WEIGHTS AND BIAS TO INPUT AND APPLYING A FUNCTION TO PRODUCE OUTPUT


################################################################################
########## ACTIVATION
################################################################################

#  ACTIVATION FUNCTIONS TAKE THE INPUT, APPLY WEIGHTS AND BIASES AND AN ACTIVATION FUNCTION TO MAKE IT NONLINEAR; KNOWN ONES ARE:
#      STEP FUNCTION (BETWEEN 0 AND 1 FOR CERTAIN THRESHOLD); IMPRACTICAL, SINCE IT DOES NOT REFLECT CHANGES IN INPUT WELL
#      SIGMOID/LOGISTIC FUNCTION; UNPOPULAR, SINCE RELU IS COMPUTATIONALLY EASIER
#      HYPERBOLIC SINE, COSINE AND TANGENT; NOT VERY POPULAR, SHAPED VERY MUCH LIKE THE SIGMOID
#      RECTIFIED LINEAR UNIT (RELU); ZERO UNTIL CERTAIN THRESHOLD AND THEN LINEAR: max( 0, z ); MOST POPULAR SINCE IT COMPUTATIONALLY CHEAP + ROBUST TO VANISHING GRADIENTS


################################################################################
########## BACKPROPAGATION
################################################################################

#  AFTER OUTPUT IS CREATED, THE EVALUATION IS DONE WITH A COST/LOST/ERROR FUNCTION:
#      THE COST FUNCTION IDEALLY CONVERTS OUTPUT INTO SINGLE VALUE, SO THAT IT CAN BE COMPARED USING A NORM
#      OFTEN THE COST FUNCTION USES L2-DISTANCE FROM THE DESIRED VALUE FOR REGRESSION AND CROSS-ENTROPY FOR CLASSIFICATION
#      COST FUNCTION ARE OFTEN MINIMIZED USING (STOCHASTIC) GRADIENT DESCENT:
#          STEP SIZE IS LEARNING RATE
#          LEARNING RATE CAN BE MADE A FUNCTION OF THE DERIVATE OF THE WEIGTHS, SO THAT LEARNING IS ADAPTIVE -- BEST VERSION IS ADAM
#      THE UPDATE OF THE WEIGHTS AND BIASES IS DONE WITH BACKPROPAGATION, USING THE DERIVATIVES OF THE COST FUNCTION


################################################################################
########## KERAS
################################################################################

#  TENSORFLOW IS DEEP LEARNING LIBRARY THAT IS NOT NECESSARILY PYTHON-SPECIFC; DEVELOPED BY GOOGLE
#  KERAS IS A PYTHON LIBRARY, THAT CAN USE VARIOUS DEEP LEARNING LIBRARIES UNDERNEATH, AMONGST WHICH TENSORFLOW, THEANO AND CNTK
#  KERAS IS SUPERIOR IN TERMS OF SIMPLICITY, SO THAT IT BECAME THE DEFAULT API FOR TENSORFLOW 2.0


################################################################################
########## CODE
################################################################################

########## IMPORTS>>>

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import MinMaxScaler as MMS
from sklearn.metrics import mean_absolute_error as mae, mean_squared_error as mse
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
 
 
# <<<

########## DATA>>>

#  DATA HAS A PRICE AND TWO FEATURES, SO A VERY SIMPLISTIC SET
df = pd.read_csv( 'fake_reg.csv' )
df.info()


# <<<

########## ENGINEERING>>>

#  DEFINE A SCALER THAT CAN BE FIT ON THE FEATURES
scaler = MMS()
#  NOTE THAT FEATURES AND TARGET CAN BE DEFINED AS SUCH
x = df.drop( 'price', axis = 1 )
y = df[ 'price' ]
#  NOTE THAT KERAS NEEDS NUMPY-ARRAYS, SO X NEEDS TO BE CONVERTED, Y IS IN THE RIGHT FORMAT ALREADY
#  FURTHERMORE, X NEEDS TO BE TRANSFORMED, SINCE OTHERWISE VANISHING/EXPLODING GRADIENTS MAY OCCUR
x = scaler.fit_transform( x.values )
print( type( x ), '\n', x )
xtr, xte, ytr, yte = tts( x, y, test_size = .3 )


# <<<
 
########## MODEL>>>

#  BUILDING A MODEL CAN BE DONE IN TWO WAYS: DEFINING A SEQUENTIAL MODEL WITH FULLY-CONNECTED/DENSE LAYERS AND A RELU-ACTIVATION:
model = Sequential([ 
    #  LAYER 1
    Dense( 4, activation = 'relu' ),
    #  LAYER 2, ETC.
    Dense( 3, activation = 'relu' ),
    Dense( 3, activation = 'relu' ),
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

#  EPOCHS IS THE NUMBER OF TIMES THE NETWORK GOES THROUGH THE WHOLE DATA SET
model.fit( xtr, ytr, epochs = 250, verbose = 0 )
#  VISUALIZING THE LOSS OVER TIME
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

