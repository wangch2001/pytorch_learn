from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
img_path = "data/train/bees_image/16838648_415acd9e3f.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)
print(type(img_PIL))
print(img_array.shape)

writer.add_image("test", img_array, 2, dataformats="HWC")

for i in range(100):
    writer.add_scalar("y=x", i, i)

writer.close()
