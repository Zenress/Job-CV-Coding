#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
keras = tf.keras

import tensorflow_datasets as tfds
tfds.disable_progress_bar()

#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^
#Split the data manually into 80% training, 10% testing and 10% validation
(raw_train, raw_validation, raw_test), metadata = tfds.load(
'cats_vs_dogs',
split=[
  tfds.Split.TRAIN.subsplit(tfds.percent[:80]),
  tfds.Split.TRAIN.subsplit(tfds.percent[80:90]),
  tfds.Split.TRAIN.subsplit(tfds.percent[90:])],
with_info=True,
as_supervised=True,
)

get_label_name = metadata.features['label'].int2str #Creates a function object that we can use to get labels

IMG_SIZE = 160 #All images will be resized to 160x160

def format_example(image,label):
  """
  Returns an image that is reshaped to IMG_SIZE
  """
  image = tf.cast(image,tf.float32)
  image = (image/127.5) - 1
  image = tf.image.resize(image, (IMG_SIZE,IMG_SIZE))
  return image, label

train = raw_train.map(format_example)
validation = raw_validation.map(format_example)
test = raw_test.map(format_example)

BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000

train_batches = train.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
validation_batches = validation.batch(BATCH_SIZE)
test_batches = test.batch(BATCH_SIZE)

IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

#Using one of the inbuilt models from googles tensorflow
#MobileNetV2 is trained on 1.4 million images and has 1000 different classes
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')

for image, _ in train_batches.take(1):
  pass

feature_batch = base_model(image)
print(feature_batch.shape)