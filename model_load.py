import torch
import torchvision

# 方式1-》保存方式1，加载模型
from torch import nn
from model_save import *

model = torch.load("vgg16_method1.pth")
#print(model)

# 方式2，加载模型
# vgg16 = torchvision.models.vgg16(pretrained=False)  #加载模型结构
# vgg16.load_state_dict(torch.load("vgg16_method2.pth"))
model = torch.load("vgg16_method2.pth")  #仅加载模型参数
# print(model)

# class Tudui(nn.Module):
#     def __init__(self):
#         super(Tudui, self).__init__()
#         self.conv1 = nn.Conv2d(3, 64, kernel_size=3)
#
#     def forward(self, x):
#         x = self.conv1(x)
#         return x

model = torch.load('tudui_method1.pth')
print(model)