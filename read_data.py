from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        """
        构造函数

        参数:
        root_dir (str): 根目录路径
        label_dir (str): 标签目录路径

        该函数用于初始化对象的根目录和标签目录路径，并计算其组合路径
        """
        self.root_dir = root_dir  # 设置根目录路径
        self.label_dir = label_dir  # 设置标签目录路径
        self.path = os.path.join(self.root_dir, self.label_dir)  # 计算根目录和标签目录的组合路径
        self.img_path = os.listdir(self.path) # 获取组合路径下的所有文件名

    def __getitem__(self, idx):
        """
        重写[]操作，以便在给定索引时能够获取到相应的图像和标签。

        参数:
        - idx (int): 图像索引。

        返回:
        - img: 打开的图像对象。
        - label: 图像的标签目录。
        """
        # 根据索引获取图像文件名
        img_name = self.img_path[idx]

        # 构建图像的完整路径
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)

        # 打开图像
        img = Image.open(img_item_path)

        # 获取标签目录
        label = self.label_dir

        # 返回图像和标签
        return img, label

    def __len__(self):
        return len(self.img_path)


root_dir = "dataset/train"
ants_label_dir = "ants"
bees_label_dir = "bees"
ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir, bees_label_dir)
train_dataset = ants_dataset + bees_dataset

img, data = train_dataset[123]
img.show()
print(data)


# print(ants_dataset.__len__())
# print(bees_dataset.__len__())





