import os
from PIL import Image
from torch.utils.data import Dataset
import numpy as np

class RNetDataset(Dataset):
    def __init__(self, root_dir, val_dir, transform=None):
        self.root_dir = root_dir
        self.val_dir = val_dir
        self.transform = transform
        self.images = os.listdir(self.root_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.images[index])
        mask_path = os.path.join(self.val_dir, self.images[index])
        try:
          image = np.array(Image.open(img_path).convert("RGB"))
        except:
          pass
        try:
          mask = np.array(Image.open(mask_path).convert("L"), dtype=np.float32)
          mask[mask == 255.0] = 1.0
        except:
          pass

        try:
          if self.transform is not None:
              augmentations = self.transform(image=image, mask=mask)
              image = augmentations["image"]
              mask = augmentations["mask"]

          return image, mask
        except:
          pass