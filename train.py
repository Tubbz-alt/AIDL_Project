import os
import zipfile
import argparse
from tqdm import tqdm
#
from model import SRGAN
from utils import DataDownloader
#
# Preparation for training
def prep(train_folder, num_images, download=True):
    # Download CelebA dataset from Google Drive And prepare the folders.
    # DO NOT CHANGE FILE_ID !!!
    if download:
        file_id = '1DdATVAyvoH9dhLiQfJH89xE1nW-8k23m'
        destination = 'img_align_celeba.zip'
        DataDownloader(file_id, destination)    

    # if the folder does not exist, create
    if not os.path.exists(train_folder):
        os.makedirs(train_folder)

    # iterate over zip file to remove subdirectories and extract data
    with zipfile.ZipFile('img_align_celeba.zip') as zip:
        zinfo = zip.infolist()
        for f in tqdm(range(num_images), ncols=80):
            if zinfo[f].filename[-1] != '/':
                zinfo[f].filename = os.path.basename(zinfo[f].filename.split('/')[1])
                zip.extract(zinfo[f], train_folder)        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AIDL SRGAN Train')
    parser.add_argument('--train_folder', default='./data/train/', help='dataset folder')
    parser.add_argument('--epochs', default=500, type=int, help='number of epochs')
    parser.add_argument('--batch_size', default=12, type=int, help='Batch size')
    parser.add_argument('--sample_interval', default=10, type=int, help='Sample Save Interval')
    opt = parser.parse_args()

    # Call 'prep' method to download dataset and create folders
    # if the automatic download of the dataset fails, download it manually from
    # https://drive.google.com/file/d/1DdATVAyvoH9dhLiQfJH89xE1nW-8k23m
    # and put in the same folder of this script and set the download = False
    num_img = opt.epochs * opt.batch_size
    prep(opt.train_folder, num_img, download=False)

    # Call 'train' Method
    gan = SRGAN()
    gan.train(epochs=opt.epochs, 
              batch_size=opt.batch_size, 
              train_folder=opt.train_folder,
              sample_interval=opt.sample_interval)
