from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

# python 的用法-> tensor数据类型

img_path = "data/train/ants_image/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

# transforms该如何使用
tensor_trans = transforms.ToTensor()  # 调用工具箱创造自己的工具箱
tensor_img = tensor_trans(img)  # 调用自己的工具箱

writer.add_image("Tensor_img", tensor_img)

writer.close()
