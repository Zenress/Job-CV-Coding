#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Main Machine learning libraries
import tensorflow as tf
from tensorflow import keras

#Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() #Split into testing and training
 
class_names = ['T-shirt/top', 'Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle Boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential ([
  keras.layers.Flatten(input_shape=(28,28)), #Input layer (1)
  keras.layers.Dense(128, activation='relu'), #Hidden layer (2)
  keras.layers.Dense(10, activation='softmax') #Output layer (3)
])