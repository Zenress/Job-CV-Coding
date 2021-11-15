#Switching CPU operation instructions to AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Adding progression logging
import logging
logging.getLogger().setLevel(logging.INFO)
#Standard imports ^

import torch
import numpy as np

#Directly from data
#Tensors can be created directly from data. The data type is automatically inferred
data = [[1,2],[3,4]]
x_data = torch.tensor(data)

#From a NumPy array
#Tensors can be created from a numpy array (and vice versa)
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

#From another tensor
#The new tensor retains the properties(shape, datatype) of the argument tensor, unless explicitly overridden
x_ones = torch.ones_like(x_data) #Retains the properties of x_data
print(f"Ones Tensor \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) #Overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

#With Random or Constant values:
#Shape is a tuple of tensor dimensions. In the functions below, it determines the dimensionality of the output tensor
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor}")
print(f"Ones Tensor: \n {ones_tensor}")
print(f"Zeros Tensor: \n {zeros_tensor}")

#Attributes of a Tensor
#Tensor attributes describe their shape, datatype and the device on which they are stored
tensor = torch.rand(3,4)

print(f"Shape of Tensor: {tensor.shape}")
print(f"Datatype of Tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

if torch.cuda.is_available():
  tensor = tensor.to("cuda")

#Standard numpy-like indexing and slicing
tensor2 = torch.ones(4,4)
print("First row: ", tensor2[0])
print("First column: ", tensor2[:,0])
print("Last column: ", tensor2[...,-1])
tensor2[:,1] = 0
print(tensor2)

#Joining tensors. You can use torch.cat to concatenate a sequence of tensors along a given dimension
t1 = torch.cat([tensor2,tensor2,tensor2], dim=1)
print(t1)

#Arithmetic operations
#This computes the matrix multiplication between two tensors. y1, y2, y3 will have the same value
y1 = tensor2 @ tensor2.T
y2 = tensor2.matmul(tensor2.T)

y3 = torch.rand_like(tensor2)
torch.matmul(tensor2,tensor2.T, out=y3)

#This computes the element-wise product. z1, z2, z3 will have the same value
z1 = tensor2 * tensor2
z2 = tensor2.mul(tensor2)

z3 = torch.rand_like(tensor2)
torch.mul(tensor2,tensor2,out=z3)

#Single Element tensors. If you have a one-element tensor, for example by aggregating all values
#Of a tensor into one value, you can convert it to a Python numerical value using item()
agg = tensor2.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

#In-palce operations. Operations that store the result into the operand are called in-place.
#They are denoted by a _ suffix. For example: x.copy_(y), x.t_(), will change x
print(tensor2, "\n")
tensor2.add_(5)
print(tensor2)

#Bridge with Numpy
#Tensors on the CPU and NumPy arrays can share their underlying memory locations,
# and changing one will change the other

#Tensor to NumPy array
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

#A change in the tensor reflects in the NumPy array
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

#NumPy array to tensor
n = np.ones(5)
t = torch.from_numpy(n)

#Changes in the NumPy array reflects in the tensor
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")