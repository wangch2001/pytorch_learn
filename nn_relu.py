import torch
import torchvision
from torch import nn
from torch.nn import ReLU, Module, Sigmoid
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./dataset_CIFAR10", train=False, transform=torchvision.transforms.ToTensor(),
                                     download=False)

dataloader = DataLoader(dataset, batch_size=64)

class Tudui(Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.relu1 = ReLU()
        self.sigmoid1 = Sigmoid()

    def forward(self, input):
        output = self.sigmoid1(input)
        return output

tudui = Tudui()
step = 0

writer = SummaryWriter("logs")

for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, step)
    output = tudui(imgs)
    writer.add_images("output", output, step)
    step += 1

writer.close()
