#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^

import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
  root="PyTorchLearning/PyTorchDatasets",
  train=True,
  download=True,
  transform=ToTensor(),
  target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)