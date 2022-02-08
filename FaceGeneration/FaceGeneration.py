from audioop import bias
from email import generator
from torchvision.datasets import ImageFolder
import torchvision.transforms as T
import torch.nn as nn
import torch

image_size = 64
stats = (0.5,0.5,0.5),(0.5,0.5,0.5)
FOLDER_DIR = "C:/Users/shan0382/Documents/Full FaceGenerationDataset/"

dataset = ImageFolder(FOLDER_DIR, transform = T.Compose([
                      T.Resize(image_size),
                      T.CenterCrop(image_size),
                      T.ToTensor(),
                      T.Normalize(*stats)]))




"""discriminator = nn.Sequential(
  #Initial dim: 3 X 64 X 64
  nn.Conv2d(3, 64, kernel_size = 4, stride = 2, padding = 1, bias = False),
  nn.BatchNorm2d(64),
  nn.LeakyReLU(0.2, inplace=True),
  
  #Dim: 64 x 32 x 32
  nn.Conv2d(64, 128, kernel_size = 4, stride = 2, padding = 1, bias = False),
  nn.BatchNorm2d(128),
  nn.LeakyReLU(0.2, inplace = True),
  
  #Dim: 128 x 16 x 16
  nn.Conv2d(128, 256, kernel_size = 4, stride = 2, padding = 1, bias = False),
  nn.BatchNorm2d(256),
  nn.LeakyReLU(0.2,inplace = True),
  
  #Dim: 256 x 8 x 8
  nn.Conv2d(256, 512, kernel_size = 4, stride = 2, padding = 2, bias = False),
  nn.BatchNorm2d(512),
  nn.LeakyReLU(0.2, inplace = True),
  
  #Dim: 512 x 4 x 4
  nn.Conv2d(512, 1, kernel_size = 4, stride = 1, padding = 0, bias = False),
  
  #Dim: 1 x 1 x 1
  nn.Flatten(),
  nn.Sigmoid()
)

latent_size = 128

generator = nn.Sequential(
  #Initial Dim: latent_size x 1 x 1
  nn.ConvTranspose2d(latent_size,512,kernel_size=4,stride=1,padding=0,bias= False),
  nn.BatchNorm2d(512),
  nn.ReLU(True),
  
  #Dim: 512 x 4 x 4
  nn.ConvTranspose2d(512,256,kernel_size=4,stride=2,padding=1,bias=False),
  nn.BatchNorm2d(256),
  nn.ReLU(True),
  
  #Dim: 256 x 8 x 8
  nn.ConvTranspose2d(256,128,kernel_size=4,stride=2,padding=1,bias=False),
  nn.BatchNorm2d(128),
  nn.ReLU(True),
  
  #Dim: 128 x 16 x 16
  nn.ConvTranspose2d(128,64,kernel_size=4,stride=2,padding=1,bias=False),
  nn.BatchNorm2d(64),
  nn.ReLU(True),
  
  #Dim: 64 x 32 x 32
  nn.ConvTranspose2d(64,3,kernel_size=4,stride=2,padding=1,bias=False),
  nn.Tanh()
)

xb = torch.randn(batch_size)
"""