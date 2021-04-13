import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
nltk.download('punkt')
import numpy
import tflearn
from process_data import training, output
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
# things we need for Tensorflow
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import pandas as pd
import pickle
import random

from process_data import  allWords, convoLabels, data


# tensorflow.reset_default_graph()
# this line does not work

#convert input sentence to bag of words so the model can understand it. 
def convert_input_to_bow(s, wrds): 
    bow = [0 for _ in range(len(wrds))]
    s_wrds = nltk.word_tokenize(s)
    s_wrds = [stemmer.stem(wrd.lower()) for wrd in s_wrds]

    for x in s_wrds: 
        for i, j in enumerate(wrds): 
            if j == x: 
                bow[i] = 1
    
    return numpy.array(bow)


# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
# model = Sequential()
# model.add(Dense(128, input_shape=(len(training[0]),), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(len(output[0]), activation='softmax'))

# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# model.fit(np.array(training), np.array(output), epochs=1000, batch_size=5, verbose=1)

nerual_net = tflearn.input_data(shape=[None, len(training[0])])
# this create input data for the RNN 
nerual_net = tflearn.fully_connected(nerual_net, 128)
# first hidden layer with 12 neruon
nerual_net = tflearn.fully_connected(nerual_net, 64)
# second hidden layer with 12 neruon

nerual_net = tflearn.fully_connected(nerual_net, 32)

nerual_net = tflearn.fully_connected(nerual_net, len(output[0]), activation="softmax")
# output layer and declare activiation function for this NN. In this case is softmax
# the activiation function softmax will give a probaility to all output
nerual_net = tflearn.regression(nerual_net)

model = tflearn.DNN(nerual_net)
# this model untilize DNN(deep neural network) for natural langrage processing

# try:
for word in allWords: 
    print(word)
    
#     model.load("model.tflearn")
# except:
model.fit(training, output, n_epoch=500, batch_size=8)
# print(model.evaluate(training, output))
# #     # this is where model is trained
# #     # training and output both pass in
# #     # n_epoch is for how many its going to see the same data, in this case its 1000 time(we expect the more we show the same data, the better it is classifying )
# #     # we pass in 8 batch at a timeo
# p = convert_input_to_bow("Load blood pessure for patient", allWords)
# print(p)
# print(model.predict([p]))

model.save("model.tflearn")

