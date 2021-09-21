#Switching CPU operation instructions to AVX AVX2
import os
from sys import version
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Importing base tensorflow
import tensorflow as tf

#Importing tensorflow keras datasets, layers and models
from tensorflow.keras import datasets, layers, models
#Import pyplot so i can plot the results to a diagram
import matplotlib.pyplot as plt

#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)

##Dataloading and preprocessing
#Load and split dataset
(train_images,train_labels), (test_images,test_labels) = datasets.cifar10.load_data()
#Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

#Defining feature columns
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

