# -*- coding: utf-8 -*-
"""Resize Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vY3iDUTs-WT2Ox6_z32ZfY4P-y229T8L
"""

import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from tqdm.notebook import tqdm
import numpy as np

from google.colab import drive
drive.mount("/content/drive")

cd "/content/drive/MyDrive/NETS 213 Final Project"

def batchResize(image_path, size, img_outDir):
  images = os.listdir(image_path)
  print("Creating dir..")
  if not os.path.isdir(img_outDir):
    os.makedirs(img_outDir)
  print("Adding images..")
  for img_f in tqdm(images):
    image = Image.open(os.path.join(image_path, img_f)).convert('RGB')
    image = image.resize(size)
    np.save(os.path.join(image_path, img_f), np.array(image))

batchResize('homeImages', (256, 256), 'resizedImages')