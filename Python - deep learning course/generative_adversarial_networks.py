#  GENERATIVE ADVERSARIAL NETWORKS>>>

#  GENERATIVE ADVERSARIAL NETWORKS ARE NETWORKS THAT USES TWO NETWORKS TO COMPETE EACH OTHER
#  ONE NETWORK FORGES DATA, WHETHER THE OTHER ONE IS SUPPOSED TO (BINARY) IDENTIFY WHICH DATA IS FORGED AND WHICH DATA IS ORIGINAL
#  GENERATIVE ADVERSARIAL NETWORKS WERE INVENTED BY GOODFELLOW


# <<<

#  TRAINING>>>

#  PHASE 1 TRAINS THE DISCRIMINATOR (ON LABELED DATA THAT IS REAL AND IS FAKE)
#  PHASE 2 TRAINS THE GENERATOR ON FAKE IMAGES THE DISCRIMINATOR LABELS AS 'REAL', SO: THE GENERATOR TRAINS TO FOOL THE DISCRIMINATOR
#  THIS CYCLE REPEATS
#  THEREFORE, THE GENERATOR NEVER GETS TO SEE ANY OF THE ORIGINAL DATA, ONLY DATA IT PRODUCED ITSELF


# <<<

#  DIFFICULTIES>>>

#  RESOURCES: 
#      DEFINITELY NEED HIGH-PERFORMANCE GPU TO OPERATE DECENTLY
#  MODE COLLAPSE: 
#      IF ONLY VERY FEW IMAGES FOOL THE DISCRIMINATOR, THE GENERATOR MIGHT COLLAPSE TO ONLY PRODUCE THAT (SINGLE) IMAGE(S)
#      CAN BE SOLACED BY DEEP GENERATIVE ADVERSARIAL NETWORKS, AND MINI-BATCH DISCRIMINATION THAT PUNISHES SIMILAR GENERATED IMAGES
#  INSTABILITY:
#      DIFFICULT TO ASCERTAIN THE PERFORMANCE, SINCE WHAT MAY FOOL A COMPUTER MIGHT NOT FOOL A HUMAN BEING AND VICE VERSA
#      FURTHERMORE, SINCE THE TWO NETWORKS ARE COMPETING, THE PERFORMANCE MIGHT OSCILLATE WILDLY


# <<<

################################################################################
##### CODE FOR GENERATIVE ADVERSARIAL NETWORK ON MNIST
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
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.models import Sequential


# <<<

#  DATA>>>

( xtr, ytr ), ( xte, yte ) = mnist.load_data()
#  FILTER OUT SUBSET TO CLEARLY SEE RESULTS OF GENERATOR
sevens = xtr[ ytr == 7 ]


# <<<

#  MODEL>>>

discriminator = Sequential([
    
    Flatten( input_shape = [ 28, 28 ] ),
    Dense( 150, activation = 'relu' ),
    Dense( 100, activation = 'relu' ),
    Dense( 1, activation = 'sigmoid' ),


])
#  THE GENERATOR LOOKS A LOT LIKE A DECODER IS SHAPE!
INPUT_SHAPE = 100
generator = Sequential([
    
    Dense( 100, activation = 'relu', input_shape = [ INPUT_SHAPE ] ),
    Dense( 150, activation = 'relu' ),
    Dense( 28*28, activation = 'relu' ),
    Reshape([ 28, 28 ]),


])
discriminator.compile( loss = 'binary_crossentropy', optimizer = 'adam' )
#  THIS IS NECESSARY TO LET THE GAN COMPILE
discriminator.trainable = False
gan = Sequential([ generator, discriminator ])
gan.compile( loss = 'binary_crossentropy', optimizer = 'adam' )


# <<<

#  TRAINING>>>

BATCH_SIZE = 16
EPOCHS = 5
generator, discriminator = gan.layers
#  THIS IS NECESSARY TO CREATE SLICES FROM THE DATA, SINCE IT IS TOO LARGE TO LOAD IN MEMORY
data = tf.data.Dataset.from_tensor_slices( sevens ).shuffle( buffer_size = 1000 ).batch( BATCH_SIZE, drop_remainder = True )

#  MORE ELABORATE STRUCTURE, SINCE TWO PHASES NEED TO BE ACCOUNTED FOR
for epoch in range( EPOCHS ):
    
    print( f"Epoch { epoch + 1 }" )
    
    for i,j in enumerate( data ):
        
        if not i%100:
            print( f"Currently on batch { i } of { len( sevens ) // BATCH_SIZE }" )
        
        #####  DISCRIMINATOR PHASE
        #  CREATE ONE BATCH OF FAKE DATA
        noise = tf.random.normal( shape = [ BATCH_SIZE, INPUT_SHAPE ] )
        generated_images = generator( noise )
        #  CONCATENATE IT WITH REAL DATA
        real_and_generated_images = tf.concat( [ generated_images, tf.dtypes.cast( j, tf.float32 ) ], axis = 0 )
        labels_discriminator = tf.constant( [[ 0 ]] * BATCH_SIZE + [[ 1 ]] * BATCH_SIZE )
        discriminator.trainable = True
        discriminator.train_on_batch( real_and_generated_images, labels_discriminator )

        #####  GENERATOR PHASE
        discriminator.trainable = False
        noise = tf.random.normal( shape = [ BATCH_SIZE, INPUT_SHAPE ] )
        labels_generator = tf.constant( [[ 1.0 ]] * BATCH_SIZE )
        gan.train_on_batch( noise, labels_generator )


# <<<

#  VISUALIZING THE RESULTS>>>

#  HOPEFULLY, THE GENERATOR LEARNED TO CREATE FAKE NUMBERS FROM NOISE NOW
noise = tf.random.normal( shape = [ BATCH_SIZE, INPUT_SHAPE ] )
images = generator( noise )
for i in range( BATCH_SIZE ):
    #  NOTE THAT INDEED MODE COLLAPSE HAS TAKEN PLACE!
    plt.imshow( images[ i ] )
    plt.show()


# <<<

