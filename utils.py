import cv2
from glob import glob
import numpy as np
import requests
from tqdm import tqdm

class DataLoader():
    def __init__(self, dataset_path, img_res=(128, 128)):
        self.dataset_path = dataset_path
        self.img_res = img_res

    def load_data(self, batch_size=1, is_testing=False):
        path = glob('%s*' % (self.dataset_path))
        batch_images = np.random.choice(path, size=batch_size)

        imgs_hr = []
        imgs_lr = []
        for img_path in batch_images:
            # Get the slicing because Cv2 reads images in BGR
            img = self.imread(img_path)[:,:,::-1]

            # Downscales the original image by factor of 4
            h, w = self.img_res
            low_h, low_w = int(h / 4), int(w / 4)

            img_hr = cv2.resize(img, self.img_res)
            img_lr = cv2.resize(img, (low_h, low_w))

            # If training => do random flip
            if not is_testing and np.random.random() < 0.5:
                img_hr = np.fliplr(img_hr)
                img_lr = np.fliplr(img_lr)

            imgs_hr.append(img_hr)
            imgs_lr.append(img_lr)

        imgs_hr = np.array(imgs_hr) / 127.5 - 1.
        imgs_lr = np.array(imgs_lr) / 127.5 - 1.

        return imgs_hr, imgs_lr

    # reads the image
    def imread(self, path):
        return cv2.imread(path).astype(np.float)	


def DataDownloader(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 8192

        with open(destination, "wb") as f:
            for chunk in tqdm(response.iter_content(CHUNK_SIZE)):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    
    session.mount('https://', adapter)

    response = session.get(URL, params = { 'id' : id }, stream = True, verify=False)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)
