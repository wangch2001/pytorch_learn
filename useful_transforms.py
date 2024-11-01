from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")
img = Image.open("images/image.png")
print(img)

# ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("ToTensor", img_tensor)
print(img_tensor.shape)

# Normalize
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
writer.add_image("Normalize", img_norm, 3)

# Resize
print(img.size)
trans_resize = transforms.Resize((512, 512))  # 设置自己工具箱
# img_PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)  # 调整图片大小
# img_resize PIL -> totensor -> img_resize tensor
img_resize = trans_totensor(img_resize)  # 将图片转为tensor数据类型
writer.add_image("Resize", img_resize, 0)
print(img_resize)

# Compose - resize -2
trans_resize2 = transforms.Resize(512)
trans_compose = transforms.Compose([trans_resize2, trans_totensor])  # 前一个的输出作为后一个的输入
img_resize2 = trans_compose(img)
writer.add_image("Compose", img_resize2, 1)

# RandomCrop
trans_random = transforms.RandomCrop((500, 500))
trans_compose2 = transforms.Compose([trans_random, trans_totensor])
for i in range(10):
    img_crop = trans_compose2(img)
    writer.add_image("RandomCrop", img_crop, i)

writer.close()
