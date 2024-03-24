################################################################################
#####  THEORY
################################################################################

#  GENERAL>>>

#  CONVOLUTIONAL NEURAL NETWORKS ARE MAINLY USEFUL FOR IMAGE DATA
#  FAMOUS EXAMPLES ARE: LeNet-5, AlexNet, GoogLeNet, ResNet, A.M.O
#  IMAGE FILTER == IMAGE KERNEL, WHERE LATTER REFERS MAINLY TO MATHEMATICS, FIRST TO APPLICATIONS
#  PROCESS OF PASSING A KERNEL OVER AN IMAGE IS CALLED A CONVOLUTION
#  IMAGES IN THIS CONTEXT SHOULD BE DECONSTRUCTED IN SEPARATE COLORS (RGB, FOR EXAMPLE), SO THAT AN ENCOMPASSING COLOR TENSOR OCCURS


# <<<

#  FAMOUS IMAGE DATA SETS>>>

#  MNIST CONTAINS GREYSCALE HANDWRITTEN 28X28 IMAGES OF DIGITS
#  CIFAR-10 CONTAINS COLORED 32X32 IMAGES OF TEN DIFFERENT OBJECTS: AIRPLANE, CAT, BIRD, CAR, DEER, DOG, FROG, HORSE, SHIP AND TRUCK


# <<<

#  CONVOLUTION IN IMAGE CONTEXT>>>

#  SUMMING THE HADAMARD-PRODUCT (ELEMENT-WISE PRODUCT) OF KERNEL WITH THE IMAGE PIXELS 
#  REPLACING THE CENTER PIXEL IN THE KERNEL WITH THIS SUM
#  DOES RESULT IN THE EDGE LAYER BEING IGNORED, SO A DUMMY EDGE (PADDING) CAN BE INTRODUCED TO COUNTER THIS EFFECT


# <<<

#  CONVOLUTIONAL NEURAL NETWORKS>>>

#  ARTIFICIAL NEURAL NETWORKS NEED:
#      FLATTENED IMAGES (SO LOSE 2D INFORMATION)
#      EXECESSIVE AMOUNT OF PARAMETERS, SINCE THEY ARE FULLY CONNECTED
#      CENTERED/BALANCED IMAGES
#  CONVOLUTIONAL NEURAL NETWORKS DON'T NEED: 
#      FLATTENED IMAGES (SO WOULD MAINTAIN 2D INFORMATION)
#      EXECESSIVE AMOUNT OF PARAMETERS, SINCE THEY ARE SPARSELY CONNECTED
#      CENTERED/BALANCED IMAGES, BUT CAN HANDLE DEFORMED IMAGES


# <<<

#  ARCHITECTURE>>>

#  IN CONVOLUTIONAL NEURAL NETWORKS NOT ALL NEURONS ARE CONNECTED TO NEXT LAYER
#  INSTEAD, A LOCAL KERNEL IS MAPPED UNTO A NEURON IN THE FOLLOWING LAYER, 
#  THEN A STRIDE IS APPLIED AND THE NEXT KERNEL IS APPLIED TO ANOTHER NEURON IN THE FOLLOWING LAYER, 
#  THUS CREATING A REAL KERNEL-LAYER, THAT CONSISTS OF LOCAL MAPPINGS, IN THE END
#  THESE SPARSELY CONNECTED NEURONS THEN END UP BECOMING THE KERNELS
#  MOST OFTEN, CONVOLUTIONAL LAYERS ARE THEN FED INTO OTHER CONVOLUTIONAL LAYERS, DISCOVERING INTRICATE PATTERS
#  AFTER CONVOLUTIONAL LAYERS, POOLING/DOWNSAMPLING/SUBSAMPLING LAYERS COME
#  THESE ARE CONVOLUTIONAL LAYERS THAT DOWNSIZE THE PREVIOUS CONVOLUTIONAL LAYER DUE TO A LARGER KERNEL-SIZE AND STRIDE
#  OFTEN AVERAGE/MAX-KERNELS ARE USED IN THIS CASE (TAKING THE MAX-VALUE IN A KERNEL AS THE NEW VALUE)
#  NOTE THAT EVEN A RELATIVELY SMALL KERNEL OF 2X2 WITH A STRIDE OF 2, ALREADY REMOVES 75% OF THE DATA
#  ANOTHER TECHNIQUE OF REDUCING SIZE IS TO USE DROPOUT LAYERS


# <<<

################################################################################
#####  CODE
################################################################################

#  IMPORTS>>>

import os
#  MAKE TENSORFLOW REDUCE ITS EXAGARATING VERBOSITY
#  0 IS DEFAULT (NONE), 1 FOR INFO, 2 FOR WARNINGS AND 3 FOR EVEN SURPRESSING ERRORS
os.environ[ 'TF_CPP_MIN_LOG_LEVEL' ] = '1'  
import pandas as pd
import numpy as np
#  FOR READING IN FILES FROM ONES OWN COMPUTER
#  from matplotlib.image import imread
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split as tts
#  FOR READING IN AND MANIPULATING IMAGE FILES
from tensorflow.keras.preprocessing.image import ImageDataGenerator as IDG
#  FOR CREATING ONE-HOT ENCODING
#  from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, LeakyReLU
from tensorflow.keras.callbacks import EarlyStopping


# <<<

#  DATA ENGINEERING>>>

#  THIS DATA IS ON BLOOD CELLS OF MALARIA PATIENTS FROM NIH

#  NOTE THAT THE IMAGES WILL HAVE DIFFERENT DIMENSIONS, SO THE IMAGES NEED TO BE RESCALED FOR THE NETWORK!
#  A GIVEN FOR NOW IS THE IDEAL SIZE, IT IS DEMONSTRATED THAT THIS IS THE AVERAGE SIZE FOR ALL IMAGES
#  NOTE THE 3 HERE, THAT INDICATES 3 DIFFERENT COLOUR CHANNELS
BATCH = 16
average_shape = ( 130, 130, 3 )

#  ANOTHER THING TO DO IS TO MANIPULATE THE INPUT, SO THAT THE MODEL BECOMES MORE ROBUST TO SCALED/CROPPED/ROTATED IMAGES
#  THIS IS SPECIFICALLY AIMED AT DATA AUGMENTATION
image_data = IDG( 
        
    #  DEGREES OVER WHICH IMAGES CAN BE RANDOMLY ROTATED OVER
    rotation_range = 20,
    #  BOTH FOR WIDTH AND HEIGHT, SOME IMAGES WILL BE AUTOMATICALLY SCALED WITH A RANDOM NUMBER 0-0.1
    width_shift_range = .1,
    height_shift_range = .1,
    #  RESCALING THE IMAGE TO DESIRED SCALE
    rescale = 1/255,
    #  ONE CAN ALSO CUT AWAY PARTS OF THE IMAGE
    shear_range = .1,
    #  OR ZOOM IN
    zoom_range = .1,
    #  IN THIS CASE IT WON'T HURT TO RANDOMLY FLIP SOME IMAGES
    horizontal_flip = True,
    #  AND FILL UP MISSING VALUES AFTER TRANSFORMING IMAGES; PADDING WITH 0 IS ANOTHER OPTION
    fill_mode = 'nearest',


)

#  NOTE THAT THE FILES ALREADY WERE ORGANIZED IN THE MANNER TENSORFLOW LIKES
#  PER IMAGE, A DESIRED TARGET SIZE NEEDS TO BE SPECIFIED WHICH IS EQUAL IN EVERY IMAGE
train = image_data.flow_from_directory( 
    
    './cell_images/train/', 
    #  NOTE THAT THE SIZE IS THE FIRST TWO ENTRIES IN THE AVERAGE IMAGE (COLOUR IS NOT RELEVANT HERE)
    target_size = average_shape[ :-1 ], 
    color_mode = 'rgb',
    class_mode = 'binary',
    #  TAKE A POWER OF 2 HERE
    batch_size = BATCH,
    #  THIS ONE IS ALSO IMPORTANT, SINCE ONE DOESN'T WANT TO SHUFFLE TEST DATA COMPARED TO LABELS!
    #  shuffle = False,
    
    
)
test = image_data.flow_from_directory( 
     
    './cell_images/test/',
    target_size = average_shape[ :-1 ], 
    color_mode = 'rgb',
    class_mode = 'binary',
    batch_size = BATCH,
    #  THIS ONE IS ALSO IMPORTANT, SINCE ONE DOESN'T WANT TO SHUFFLE TEST DATA COMPARED TO LABELS!
    shuffle = False,
    
    
)


# <<<

#  MODEL>>>

cnn = Sequential([

    #  THE NUMBER OF FILTERS IS A BIT ARBITRARY, AS IS THE KERNEL SIZE, THE SHAPE IS THE DEFINED SHAPE EARLIER ON (IMPORTANT!!)
    Conv2D( 
        filters = 64, 
        kernel_size = ( 3, 3 ), 
        input_shape = average_shape, 
        activation = 'relu',
        #  activation = LeakyReLU( alpha = 0.5 ),
        kernel_initializer = 'glorot_uniform', 
        bias_initializer = 'glorot_uniform' 
    ),
    #  DEFAULT IS 2X2
    MaxPool2D( pool_size = ( 2, 2 ) ),
    #  ADDITIONAL LAYERS, IF SO DESIRED; DOES HAVE PROBLEM OF VANISHING GRADIENTS
    #  Conv2D( filters = 64, kernel_size = ( 3, 3 ), input_shape = average_shape, activation = 'relu' ),
    #  MaxPool2D( pool_size = ( 2, 2 ) ),
    #  Conv2D( filters = 64, kernel_size = ( 3, 3 ), input_shape = average_shape, activation = 'relu' ),
    #  MaxPool2D( pool_size = ( 2, 2 ) ),
    #  THIS FLATTENING IS SPECICALLY FOR THE DENSE LAYERS
    Flatten(),
    Dense( 
        128, 
        #  activation = 'relu',
        activation = LeakyReLU( alpha = 0.3 ),
        kernel_initializer = 'glorot_uniform', 
        bias_initializer = 'glorot_uniform',
    ),
    #  SWITCHING OFF HALF THE NEURONS IN EVERY BATCH
    Dropout( .5 ),
    Dense( 
        1, 
        activation = 'sigmoid',
        kernel_initializer = 'glorot_uniform', 
        use_bias = False,
        #  bias_initializer = 'glorot_uniform',
    ),


])

#  import tensorflow as tf
cnn.compile( 
    
    #  optimizer = tf.keras.optimizers.Adam( learning_rate = 1e-3 ),
    #  loss = tf.keras.losses.BinaryCrossentropy(),
    #  metrics = [ tf.keras.metrics.BinaryAccuracy(), tf.keras.metrics.FalseNegatives() ]
    loss = 'binary_crossentropy', 
    optimizer = 'adam', 
    #  NOTE THAT ONE CAN ADD ADDITIONAL METRICS HERE THAT WILL BE TRACKED DURING TRAINING
    metrics = [ 'accuracy' ]

    
)

#  NOTE THAT ONE CAN MONITOR EVERYTHING THAT'S EITHER THE LOSS FUNCTION OR THE METRICS SPECIFIED IN COMPILING THE MODEL
early_stopper = EarlyStopping( monitor = 'val_loss', patience = 2 )

model = cnn.fit(
    
    train,
    epochs = 20,
    validation_data = test,
    callbacks = [ early_stopper ],
    #  THIS ALLOWS TO SEE HOW QUICKLY IT IS TRAINING
    verbose = 1,
   

)

print( 'ACTUAL WEIGHTS IN THE FINAL LAYER:\n', cnn.layers[ 5 ].get_weights()[ 0 ] )
cnn.save( 'malaria.h5' )


# <<<

#  VISUALIZING RESULTS>>>

results = pd.DataFrame( cnn.history.history )

#  VISUALIZING THE RESULTS
canvas, axes = plt.subplots( figsize = ( 14, 8 ), nrows = 1, ncols = 2 ) 
#  LOSSES LINE PLOT:
axes[0].plot( 
    results.index,
    results[ 'val_loss' ],
    label = 'Validation Loss',
    linewidth = 5,
    c = 'yellow',
)
axes[0].plot( 
    results.index,
    results[ 'loss' ],
    label = 'Training Loss',
    linewidth = 5,
    c = 'darkgreen',
)
axes[0].legend()
axes[0].set_xlabel("Epochs")
axes[0].set_ylabel("Validation and Training Loss")
axes[0].set_title("Validation and Training Loss over Epochs")
#  ACCURACY LINE PLOT:
axes[1].plot( 
    results.index,
    results[ 'val_accuracy' ],
    label = 'Validation Accuracy',
    linewidth = 5,
    c = 'yellow',
)
axes[1].plot( 
    results.index,
    results[ 'accuracy' ],
    label = 'Training Accuracy',
    linewidth = 5,
    c = 'darkgreen',
)
axes[1].legend()
axes[1].set_xlabel("Epochs")
axes[1].set_ylabel("Validation and Training Accuracy")
axes[1].set_title("Validation and Training Accuracy over Epochs")
# TO CREATE AXES THAT ARE FURTHER APART:
plt.tight_layout()
plt.show()


# <<<

#  EVALUATION>>>

print( '\n' )
print( cnn.evaluate( test, verbose = 0 ) )
print( '\n' )
#  NOTE THAT THE BOOLEAN OUTPUT IS GENERATED HERE EXPLICITLY, SINCE THE LAST LAYER IS A SIGMOID
#  CAN BE CHANGED EASILY TO HIGHER/LOWER VALUE IF TYPE I/II ERROR MATTERS MORE (WHICH MIGHT BE VERY WELL THE CASE HERE)
predictions = cnn.predict( test ) > .5
print( classification_report( test.classes, predictions ) )
print( '\n' )
print( confusion_matrix(  test.classes, predictions ) )


# <<<

