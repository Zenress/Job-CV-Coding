import tensorflow as tf
tf.__version__
import keras
keras.__version__

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())