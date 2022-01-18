#Switching CPU operation instructions to AVX AVX2
from locale import normalize
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^

import numpy as np

import typing
from typing import Tuple

import tensorflow as tf
import tensorflow_text as tf_text
import pathlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

use_builtins = True

path_to_zip = tf.keras.utils.get_file(
    'spa-eng.zip', origin='http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip',
    extract=True)

path_to_file = pathlib.Path(path_to_zip).parent/"spa-eng/spa.txt"

def load_data(path):
  text = path.read_text(encoding="utf-8")
  lines = text.splitlines()
  pairs = [line.split("\t") for line in lines]
  inp = [inp for targ, inp in pairs]
  targ = [targ for targ, inp in pairs]
  return targ, inp

targ, inp = load_data(path_to_file)

#Creating a tf.data dataset
BUFFER_SIZE = len(inp)
BATCH_SIZE = 64

dataset = tf.data.Dataset.from_tensor_slices((inp,targ)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE)

for example_input_batch, example_target_batch in dataset.take(1):
  
  break

#Text preprocessing
example_text = tf.constant("¿Todavía está en casa?")

#Unicode Normalization
def tf_lower_and_split_punct(text):
  #Split accented characters
  text = tf_text.normalize_utf8(text, "NFKD")
  text = tf.strings.lower(text)
  #Keep space, a to z and select punctuation.
  text = tf.strings.regex_replace(text, "[^ a-z.?!,¿]","")
  #Add spaces around punctuation
  text = tf.strings.regex_replace(text, "[.?!,¿]", r" \0 ")
  #Strip whitespace.
  text = tf.strings.strip(text)

  text = tf.strings.join(['[START]', text, "[END]"], separator=' ')
  return text

#Text Vectorization
max_vocab_size = 5000

input_text_processor = tf.keras.layers.TextVectorization(
    standardize = tf_lower_and_split_punct,
    max_tokens = max_vocab_size)

input_text_processor.adapt(inp)

output_text_processor = tf.keras.layers.TextVectorization(
    standardize=tf_lower_and_split_punct,
    max_tokens=max_vocab_size)

output_text_processor.adapt(targ)
example_tokens = input_text_processor(example_input_batch)

input_vocab = np.array(input_text_processor.get_vocabulary())
tokens = input_vocab[example_tokens[0].numpy()]

plt.subplot(1,2,1)
plt.pcolormesh(example_tokens)
plt.title("Token IDs")

plt.subplot(1,2,2)
plt.pcolormesh(example_tokens != 0)
plt.title("Mask")
plt.show()

## Encoder / Decoder model


class ShapeChecker():
  def __init__(self):
    #Keep a cache of every axis-name seen
    self.shapes = {}

  def __call__(self,tensor,names,broadcast = False):
    if not tf.executing_eagerly():
      return
    
    if isinstance(names,str):
      names = (names,)

    shape = tf.shape(tensor)
    rank = tf.rank(tensor)

    if rank is not len(names):
      raise ValueError(f"Rank mismatch: \n"
                       f"     found {rank}: {shape.numpy()}\n"
                       f"     expected {len(names)}: {names}\n")

    for i, name in enumerate(names):
      if isinstance(name,int):
        old_dim = name
      else:
        old_dim = self.shapes.get(name, None)
      new_dim = shape[i]

      if (broadcast and new_dim == 1):
        continue

      if old_dim is None:
        #If the axis name is new, add its length to the cache
        self.shapes[name] = new_dim
        continue

      if new_dim is not old_dim:
        raise ValueError(f"Shape mistmatch for dimension: '{name}'\n"
                         f"    found: {new_dim}\n"
                         f"    expected: {old_dim}\n")