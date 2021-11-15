"""#Loading a pretrained resnet18 model from torchvision
import torch, torchvision
model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1,3,64,64)
labels = torch.rand(1,1000)

prediction = model(data) #Forward pass

loss = (prediction - labels).sum()
loss.backward() #Backward pass

optim = torch.optim.SGD(model.parameters(),lr=1e-2, momentum=0.9)
optim.step() #Gradient descent"""

#Differentiation in Autograd
import torch

a = torch.tensor([2.,3.], requires_grad=True)
b = torch.tensor([6.,4.], requires_grad=True)

Q = 3*a**3 - b**2

external_grad = torch.tensor([1.,1.])
Q.backward(gradient=external_grad)

print(9*a**2 == a.grad)
print(-2*b == b.grad)