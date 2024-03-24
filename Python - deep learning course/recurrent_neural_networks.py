#  PRINCIPLES>>>

#  CONVOLUTIONAL NEURAL NETWORKS ARE MORE EFFECTIVE FOR IMAGE DATA
#  SIMILARLY, RECURSIVE NEURAL NETWORKS ARE MORE EFFECTIVE FOR SEQUENTIAL DATA:
#      SEQUENTIAL DATA INCLUDES TIME SERIES, WORD SENTENCES OR AUDIO DATA
#  MAIN IDEA IS TO USE OUTPUT OF A NEURON AS NEW INPUT FOR ITSELF, SO THAT HISTORY IS EXPLICITLY (RE)USED DURING TRAINING:
#      NEURONS THAT (RE)USE THE OUTPUT OF PREVIOUS STEP(S) ARE CALLED MEMORY CELLS
#      BASIC MEMORY CELLS ONLY REMEMBER PREVIOUS STEP, MORE ADVANCED ALSO REMEMBER EARLIER STEPS (WITH LESS IMPORTANCE, E.G.)
#  SPECIAL CELLS ARE THE LONG-SHORT-TERM-MEMORY-CELLS (LSTM), THAT BOTH MAINTAIN LONG- AND SHORT-TERM MEMORY:
#      THESE CELLS HAVE INPUT, OUTPUT, FORGET AND UPDATE GATES
#      THESE GATES ESSENTIALLY BEHAVE AS SIGMOID FUNCTIONS (BLOCKING SOME INPUT, WHEREAS ACCEPTING SOME OTHERS)
#      INPUTS ARE DATA, SHORT- AND LONG-TERM MEMORY
#      OUTPUTS ARE DATA, AN UPDATED SHORT- AND LONG-TERM MEMORY
#      NEW LONG-TERM MEMORY: 
#          SIGMOID( OLD SHORT-TERM, DATA ) * OLD LONG-TERM + SIGMOID( OLD SHORT-TERM, DATA ) * TANH( OLD SHORT-TERM, DATA )
#      NEW SHORT-TERM MEMORY:
#          TANH( NEW LONG-TERM ) * SIGMOID( OLD SHORT-TERM, DATA )
#      VARIATION OF THIS IS PEEPHOLES, WHICH ADDS OLD/NEW LONG-TERM MEMORY TO ALL THREE SIGMOIDS 
#      ANOTHER VARIATION IS THE GATED RECURRENT UNIT (GRU), WHICH IS QUITE POPULAR, BUT MORE INTRICATE


# <<<

#  ARCHITECTURES>>>

#  SEQUENCE-SEQUENCE/MANY-TO-MANY: LEN(INPUT) ~ LEN(OUTPUT)
#  SEQUENCE-VECTOR/MANY-TO-ONE: LEN(INPUT) >> LEN(OUTPUT)
#  VECTOR-SEQUENCE/ONE-TO-MANY: LEN(INPUT) << LEN(OUTPUT)
#  FOR TRAINING, NOTE THAT EVERY FEATURE/TRAINING POINT IS A SEQUENCE/VECTOR AND EVERY TARGET IS AGAIN A SEQUENCE/VECTOR
#  THE TARGET DEPENDS, NATURALLY, ON THE ARCHITECTURE
#  NOTE THAT THE SIZE OF THE SEQUENCE IS MOSTLY A MATTER OF TASTE, AS LONG AS IT CAN CAPTURE TRENDS (CAN BE UP FOR EXPERIMENTS)
#  FOR TRAINING, ONE COMPARES TO TEST DATA, FOR PREDICTING, ONE RETRAINS ON ALL DATA (INCLUDING TEST) AND HOPE FOR THE BEST


# <<<

#  EXPLODING/VANISHING GRADIENTS>>>

#  GRADIENTS ARE USED TO CALCULATE WEIGHTS AND BIASES
#  FOR DEEPER NETWORKS, GRADIENTS MAY NUMERICALLY DIVERGE (EXPLODING/VANISHING)
#  NATURALLY, THIS ALSO HAPPENS WITH RECURSIVE NEURAL NETWORKS, SINCE THESE TEND TO BE DEEP DUE TO SELF-FEEDING
#  AGAINST VANISHING GRADIENTS:
#      USING ACTIVATION FUNCTIONS THAT BEHAVE WELL, WHICH IS ONE REASON FOR THE POPULARITY OF THE RECTIFIED LINEAR UNIT (RELU)
#      THIS IS UNLIKE A SIGMOID FUNCTION, WHICH DOES INDEED VANISH VERY QUICKLY, ESPECIALLY WHEN USED IN MULTIPLE LAYERS
#      ANOTHER SOLUTION IS BATCH-NORMALIZATION, OR SPECIFIC INITIALIZATION OF THE LAYERS (LIKE XAVIER INITIALIZATION)
#  AGAINST EXPLODING GRADIENTS:
#      GRADIENT CLIPPING CAN BE USED AGAINST DIVERGING GRADIENTS, WHERE THE GRADIENTS ARE CUT OFF AFTER THRESHOLDS


# <<<

################################################################################
##### CODE FOR LSTM OF A SINE WAVE
################################################################################

#  IMPORTS>>>

import os
#  MAKE TENSORFLOW REDUCE ITS EXAGARATING VERBOSITY
#  0 IS DEFAULT (NONE), 1 FOR INFO, 2 FOR WARNINGS AND 3 FOR EVEN SURPRESSING ERRORS
os.environ[ 'TF_CPP_MIN_LOG_LEVEL' ] = '1'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler as MMS
#  THIS TO CREATE BATCHES IN THE TRAINING SET
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator as TG
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM
from tensorflow.keras.callbacks import EarlyStopping


# <<<

#  DATA>>>

scaler = MMS()
#  GO FROM 0-50 IN 501 STEPS
#  EVERYTHING NEEDS TO BE SCALED, SINCE OUTPUT IS USED AS INPUT AGAIN IN THE NEW ROUND
#  RESHAPING IS NECESSARY, TO CREATE A MATRIX (RATHER THAN A VECTOR), WHICH THE SCALER DUMBLY NEEDS
#  sine = pd.DataFrame( scaler.fit_transform( np.sin( x := np.linspace( 0, 50, 501 ) ).reshape( -1, 1 ) ), index = list( range( 501 ) ), columns = [ 'sine' ] )
sine = scaler.fit_transform( np.sin( x := np.linspace( 0, 50, 501 ) ).reshape( -1, 1 ) )
#  print( sine[ 50 ] )
#  quit()

# <<<

#  ENGINEERING>>>

#  INDICATES WHICH PART OF THE SEQUENCE IS GOING TO BE USED FOR TESTING
TEST = .1
split_index = int( len( sine ) * ( 1 - TEST ) )
train = sine[ :split_index ]
test = sine[ split_index: ]
#  train = sine.iloc[ :split_index ]
#  test = sine.iloc[ split_index: ]


# <<<

#  LEARNING>>>

#  DATA TO TRAIN ON, DATA THAT OUTPUTS NEED TO BE TAKEN FROM, LENGTH OF THE TRAINING SEQUENCE, NUMBER OF SEQUENCE SAMPLES PER BATCH
#  NOTE THAT FOR THESE SETTINGS, THE OUTPUT IS ONE, SO ARCHITECTURE IS SEQUENCE-VECTOR/MANY-TO-ONE
LENGTH_OF_INPUT_SEQUENCE = 50
NUMBER_OF_FEATURES = 1
generator = TG( data = train, targets = train, length = LENGTH_OF_INPUT_SEQUENCE, batch_size = 3, )
#  CREATING THE MODEL
rnn = Sequential([
#  input_shape = ( LENGTH_OF_INPUT_SEQUENCE, NUMBER_OF_FEATURES )
    SimpleRNN( units = LENGTH_OF_INPUT_SEQUENCE, ) ,
    #  LSTM( units = LENGTH_OF_INPUT_SEQUENCE, ) ,
    Dense( 1 ),
    #  SimpleRNN,
    #  LSTM,
    #  Dense,
])
rnn.compile( optimizer = 'adam', loss = 'mse', )
#  early_stopper = EarlyStopping( monitor = 'val_loss', patience = 3 )
#  NOTE THAT RECURSIVE NEURAL NETWORKS TEND TO BE VERY SLOW
rnn.fit( generator, epochs = 6, verbose = 1 )


# <<<

#  RESULTS>>>

predicted_sequence = []
sequence = train[ -LENGTH_OF_INPUT_SEQUENCE: ].reshape(( 1, LENGTH_OF_INPUT_SEQUENCE, NUMBER_OF_FEATURES ))
for i in range( len( test ) ):
    new_point = rnn.predict( sequence )[0]
    predicted_sequence.append( new_point )
    sequence = np.append( sequence[ :, 1:, : ], [[ new_point ]], axis = 1 )
test = pd.DataFrame( data = test, index = np.arange( split_index, len( sine ) ), columns = ['sine'] )
train = pd.DataFrame( data = train, index = np.arange( 0, split_index ), columns = ['sine'] )
test[ 'predictions' ] =  np.array( predicted_sequence ).reshape( len( test ) )
results = pd.DataFrame( rnn.history.history )
#  FOR REASONS UNKNOWN, THIS YIELDS AN EMPTY SET
print( rnn.history.history )
print( results )


# <<<

#  VISUALIZING THE RESULTS>>>

canvas, axes = plt.subplots( figsize = ( 14, 8 ), nrows = 1, ncols = 2 )
#  LOSSES LINE PLOT:
axes[0].plot(
    train.index,
    'sine',
    data = train,
    label = 'Original Sine Train',
    linewidth = 5,
    c = 'brown',
)
axes[0].plot(
    test.index,
    'sine',
    data = test,
    label = 'Original Sine Test',
    linewidth = 2,
    linestyle = '--',
    c = 'yellow',
)
axes[0].plot(
    test.index,
    'predictions',
    data = test,
    label = 'Predictions',
    linewidth = 2,
    linestyle = '--',
    c = 'orange',
)
axes[0].legend()
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Output")
axes[0].set_title("Output and Predictions over Time")
#  axes[1].plot(
#      results,
#      linewidth = 5,
#      c = 'black',
#  )
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Root Mean Squared Error")
axes[1].set_title("Root Mean Squared Error over Time")
plt.tight_layout()
plt.show()


# <<<

