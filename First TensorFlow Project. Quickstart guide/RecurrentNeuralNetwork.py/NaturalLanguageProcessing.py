#Switching CPU operation instructions to AVX AVX2
import os
from tensorflow.python.ops.array_ops import sequence_mask
from tensorflow.python.ops.gen_batch_ops import batch
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^

