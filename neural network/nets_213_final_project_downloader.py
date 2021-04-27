# -*- coding: utf-8 -*-
"""NETS 213 Final Project Downloader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lDRBwfl1wTFRWqmkkZ__qAsTrvXWKT3D
"""

#@title Register API Key
# registering your API key
!mkdir  ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

from google.colab import drive
drive.mount("/content/drive")

cd "/content/drive/MyDrive/NETS 213 Final Project/"

!pip install --upgrade --force-reinstall --no-deps kaggle==1.5.10
!kaggle -v

!kaggle datasets download -d ericpierce/austinhousingprices -p "/content/drive/MyDrive/NETS 213 Final Project/" --force
print("Dataset downloaded")

#Unzip
!unzip -qq austinhousingprices.zip

def checkDirSize(dirName):  
  import os
  dir = dirName
  dirFiles = os.listdir(dir)
  print("Dir Size {}".format(len(dirFiles)))
  return len(dirFiles)

checkTrainDirSize()