#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow_probability as tfp
import tensorflow as tf