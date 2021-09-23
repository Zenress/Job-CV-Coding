#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^

from keras.datasets import imdb
from keras.preprocessing import sequence
import tensorflow as tf
import numpy as np

VOCAB_SIZE = 88584

MAXLEN = 250
BATCH_SIZE = 64

(train_data, train_labels),(test_data,test_label) = imdb.load_data(num_words=VOCAB_SIZE)

train_data = sequence.pad_sequences(train_data, MAXLEN) #Preprocessing the data so that each review is 250 characters long
test_data = sequence.pad_sequences(test_data, MAXLEN) #Preprocessing the data so that each review is 250 characters long


model = tf.keras.Sequential([
  tf.keras.layers.Embedding(VOCAB_SIZE, 32),
  tf.keras.layers.LSTM(32),
  tf.keras.layers.Dense(1,activation='sigmoid')
])

model.summary()

model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=['acc'])

history = model.fit(train_data, train_labels, epochs=10, validation_split=0.2)

model.save("languageProcessing")