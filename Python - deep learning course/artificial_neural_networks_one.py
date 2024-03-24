# PERCEPTRON SIMPLEST NEURAL NETWORK: TWO INPUTS, A PROCESSOR AND THEN AN OUTPUT 
# THIS IS THE 'FEED-FORWARD'-MODEL (STREAM IS IN ONE DIRECTION)
# THE PERCEPTRON DOES FOUR THINGS:
    # RECEIVE INPUTS
    # WEIGH INPUTS (OFTEN MULTIPLIED BY NUMBER BETWEEN -1 AND 1)
    # SUM INPUTS
    # GENERATE OUTPUT
# TO TRAIN IT USE THESE STEPS:
    # PROVIDE PERCEPTRON WITH INPUTS OF WHICH THERE IS A KNOWN ANSWER
    # PREDICT OUTCOME WITH PERCEPTRON
    # COMPUTE THE ERROR
    # ADJUST WEIGHTS ACCORDING TO ERROR
    # REPEAT
# NEURAL NETWORK IS COMBINATION OF MANY PERCEPTRONS. THERE CAN BE 'HIDDEN' LAYERS BETWEEN THE INPUT AND OUTPUT. 
# DEEP LEARNING REFERS TO THE FACT THAT THERE CAN BE MANY HIDDEN LAYERS (P.E. A NETWORK WITH 152 LAYERS)

# TENSORFLOW IS MOST POPULAR DEEP LEARNING LIBRARIES, CREATED BY GOOGLE
# IT CREATES DATA FLOW GRAPHS, WHERE THE GRAPHS ARE REALLY GRAPH-REPRESENTATIONS OF THE LAYERED NETWORK
# THE FLOW OF THE DATA (CALLED TENSORS IN THIS CONTEXT) THROUGH THESE GRAPHS IS THUS TENSORFLOW 

import tensorflow
import numpy
from tensorflow.examples.tutorials.mnist import input_data
from matplotlib import pyplot

# # MAKE CONSTANTS OR PLACEHOLDERS FOR CONSTANTS WITH TENSORFLOW:
# print(tensorflow.constant("DURK!!!"))
# print(tensorflow.placeholder(tensorflow.string))
# # FOR MATRICES:
# a = numpy.array([[5.0,78.0],[3.0,16.9]])
# b = numpy.array([[18.9],[20.0]])
# print(numpy.dot(a,b))
# xx = tensorflow.constant(a)
# yy = tensorflow.constant(b)

# # CREATE A SESSION WITH WHICH YOU CAN PERFORM OPERATIONS:
# durk = tensorflow.Session()

# # PERFORM OPERATIONS:
# print(durk.run(tensorflow.constant("DURK!!!") + tensorflow.constant("DURK!!!")))
# x = tensorflow.placeholder(tensorflow.int32)
# y = tensorflow.placeholder(tensorflow.int32)
# print(durk.run(tensorflow.add(x,y),feed_dict={x:3000,y:9090}))
# print(durk.run(tensorflow.multiply(x,y),feed_dict={x:3000,y:9090}))
# print(durk.run(tensorflow.subtract(x,y),feed_dict={x:3000,y:9090}))
# # FOR MATRICES:
# print(durk.run(tensorflow.matmul(xx,yy)))

# # WORKING WITH MNIST DATA SET:
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# # TAKING ONE RANDOM ARRAY FROM THE DATASET AND SHOW WHAT THE ORIGINAL SHAPE (28 BY 28) LOOKED LIKE:
# pyplot.imshow(mnist.train.images[429].reshape(28,28),cmap = 'Greys')
# pyplot.show()

# learn_rate = 0.001
# training_epochs = 15
# batch_size = 100
# # HOW MANY OUTCOMES THE OUTPUT CAN HAVE (0-9):
# n_classes = 10 
# n_samples = mnist.train.num_examples
# # NUMBER OF INPUTS (CAN BE RESHAPED TO MAKE 28 BY 28 MATRIX THAT LOOKS LIKE NUMBER):
# n_input = 784
# # GIVEN, TWO HIDDEN LAYERS OF PERCEPTRONS, HOW MANY PERCEPTRONS PER LAYER:
# n_hidden_1 = 256
# n_hidden_2 = 256
# # THERE IS ALSO A COST FUNCTION, THAT DEFINES HOW WELL THE ALGORITHM PERFORMED:
# def multilayered_perceptron(x,weight,bias):
#     # X PLACEHOLDER INPUT DATA, WEIGHTS DICTIONAIRY OF WEIGHTS, BIASES DICTIONAIRY OF BIAS VALUES
#     # MULTIPLY INPUT BY WEIGHTS AND ADD BIAS TO IT (SO THAT ZEROES GET OFFSET, 
#     # SO THAT WEIGHTS DON'T GET ALTERED TREMENDOUSLY AFTER LEARNING)
#     # FIRST HIDDEN LAYER WITH RELU-ACTIVATION:
#     layer_1 = tensorflow.add(tensorflow.matmul(x, weight['w1']), bias['b1'])
#     layer_1 = tensorflow.nn.relu(layer_1)
#     # SECOND HIDDEN LAYER WITH RELU-ACTIVATION:
#     layer_2 = tensorflow.add(tensorflow.matmul(layer_1, weight['w2']), bias['b2'])
#     layer_2 = tensorflow.nn.relu(layer_2)
#     # OUTPUT LAYER:
#     layer_out = tensorflow.add(tensorflow.matmul(layer_2, weight['wout']), bias['bout'])

#     return layer_out

# weights = {
#     # CREATE A MATRIX OF 784 x 256 WITH RANDOM NUMBERS:
#     'w1': tensorflow.Variable(tensorflow.random_normal([n_input,n_hidden_1])),
#     # CREATE A MATRIX OF 256 x 256 OF RANDOM NUMBERS (OUTPUT OF FIRST LAYER IS 256 FIELDS):
#     'w2': tensorflow.Variable(tensorflow.random_normal([n_hidden_1,n_hidden_2])),
#     # CREATE A MATRIX OF 256 x 10 OF RANDOM NUMBERS (OUTPUT OF SECOND LAYER IS 256 FIELDS):
#     'wout': tensorflow.Variable(tensorflow.random_normal([n_hidden_2,n_classes])),
# }

# biases = {
#     # CREATE A MATRIX OF 784 x 256 WITH RANDOM NUMBERS:
#     'b1': tensorflow.Variable(tensorflow.random_normal([n_hidden_1])),
#     # CREATE A MATRIX OF 256 x 256 OF RANDOM NUMBERS (OUTPUT OF FIRST LAYER IS 256 FIELDS):
#     'b2': tensorflow.Variable(tensorflow.random_normal([n_hidden_2])),
#     # CREATE A MATRIX OF 256 x 10 OF RANDOM NUMBERS (OUTPUT OF SECOND LAYER IS 256 FIELDS):
#     'bout': tensorflow.Variable(tensorflow.random_normal([n_classes])),
# }

# # DEFINE INPUT VARIABLE:
# input_variable = tensorflow.placeholder(dtype = 'float', shape = [None, n_input])
# # DEFINE OUTPUT VARIABLE:
# output_variable = tensorflow.placeholder(dtype = 'float', shape = [None, n_classes])
# # NOW TAKE THE FUNCTION AND PUT IT PLACEHOLDER VALUES INTO IT:
# prediction = multilayered_perceptron(input_variable, weights, biases)
# # DEFINE COST FUNCTION USING TENSORFLOW'S BUILT-IN LIBRARY:
# cost = tensorflow.reduce_mean(tensorflow.nn.softmax_cross_entropy_with_logits(labels = prediction, logits = output_variable))

# FROM HERE ON, THE CODE MALFUNCTIONS:
# optimizer = tensorflow.train.AdamOptimizer(learning_rate = learn_rate).minimize(cost)
# # CREATING A SAMPLE FROM THE DATA SET 
# # THIS IS A TUPLE OF ORIGINAL ARRAY AND WHAT THE RIGHT ANSWER WAS IN FORM OF [0 0 0 1 0 0 0 0 0 0]:
# sample = mnist.train.next_batch(batch_size)
# # CREATE A NEW SESSION:
# durkudurk = tensorflow.InteractiveSession()
# initialize_variables = tensorflow.initialize_all_variables()
# durkudurk.run(initialize_variables)
# # NOW TRAIN THE MODEL:
# for epoch in range(training_epochs):

#     average_costs = 0.0

#     for i in range(int(n_samples/batch_size)):
#         batch_x, batch_y = mnist.train.next_batch(batch_size)
#         _,c = durkudurk.run([optimizer, cost], feed_dict = {input_variable: batch_x, output_variable: batch_y})
#         average_costs += c/(int(n_samples/batch_size))
#         print(f'EPOCH: {i} AND AVERAGE COSTS: {average_costs}')
    
# THE SYNTAX OF TENSORFLOW IS CUMBERSOME. TO MAKE IT MORE SKLEARN-LIKE, PEOPLE DEVELOPED SKFLOW
# THIS IS NOW OFFICIALLY PART OF TENSORFLOW UNDER CONTRIBUTIONS (CONTRIB)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X = iris['data']
y = iris['target']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

featured_columns = [tensorflow.contrib.layers.real_valued_column("", dimension=4)]
classifier = tensorflow.contrib.learn.DNNClassifier(feature_columns = featured_columns, hidden_units=[10, 20, 10],n_classes=3,)
classifier.fit(X_train, y_train, steps=2000)
accuracy_score = classifier.evaluate(X_test, y_test)["accuracy"]
iris_predictions = list(classifier.predict(X_test))
print(f'ACCURACY: {accuracy_score}')
print(classification_report(y_test,  iris_predictions))
print(confusion_matrix(y_test,  iris_predictions))

# CODE:
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    
# import tensorflow as tf
# x = tf.placeholder(tf.float32, [None, 784])
    
# W = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))
    
# y = tf.nn.softmax(tf.matmul(x, W) + b)
    
# y_ = tf.placeholder(tf.float32, [None, 10])
    
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    
# train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    
# sess = tf.InteractiveSession()
    
# tf.global_variables_initializer().run()
    
# for _ in range(1000):
#     batch_xs, batch_ys = mnist.train.next_batch(100)
#     sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    
# correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    
# print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

# #Imports
# import tensorflow as tf
# import numpy as np
# from sklearn.datasets import load_iris
# from sklearn.cross_validation import train_test_split
# from sklearn.metrics import classification_report, confusion_matrix
    
# # Data sets
# iris = load_iris()
# X =np.float32(iris['data']) 
# y = iris['target']
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
    
# # Specify that all features have real-value data
# feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]
    
# # Build 3 layer DNN with 10, 20, 10 units respectively.
# classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
#                                             hidden_units=[10, 20, 10],
#                                             n_classes=3,
#                                             model_dir="./output")
    
# # Fit model.
# classifier.fit(X_train, y_train, steps=2000)
    
# # Evaluate accuracy.
# accuracy_score = classifier.evaluate(X_test, y_test)["accuracy"]
# print('Accuracy: {0:f}'.format(accuracy_score))
    
# #Evaluate with classification report and confusion matrix
# iris_predictions = list(classifier.predict(X_test))
# print(classification_report(y_test,  iris_predictions))
# print('\n')
# print(confusion_matrix(y_test,  iris_predictions))
# print('\n')
