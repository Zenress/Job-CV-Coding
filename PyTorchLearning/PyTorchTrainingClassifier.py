import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

def run():
    
    print('loop')

if __name__ == '__main__':
    torch.multiprocessing.freeze_support()
    run()

    

    #To fix certificate problems
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    transform = transforms.Compose(
      [transforms.ToTensor(),
      transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))]
    )

    batch_size = 4

    trainset = torchvision.datasets.CIFAR10(root="PyTorchLearning/PyTorchDatasets",     train=True, download=True, transform=transform)

    trainloader = torch.utils.data.DataLoader(trainset,batch_size=batch_size,shuffle=True,num_workers=2)

    testset = torchvision.datasets.CIFAR10(root="PyTorchLearning/PyTorchDatasets",   train=False, download=True, transform=transform)

    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers= 2)

    classes = ('plane','car','bird','cat','deer','dog','frog','horse','ship','truck')


    #Functions to show an image

    def imshow(img):
      img = img / 2 + 0.5 #Unnormalize
      npimg = img.numpy()
      plt.imshow(np.transpose(npimg, (1,2,0)))
      plt.show()

    #Get some random training images
    dataiter = iter(trainloader)
    images, labels = dataiter.next()

    #Show images
    imshow(torchvision.utils.make_grid(images))
    #Print labels
    print(' '.join('%5s' % classes[labels[j]] for j in range(batch_size)))

    #Project dropped due to too many issues. Not worth the energy