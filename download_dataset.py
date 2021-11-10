# Load packages
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import os
import pandas as pd
import shutil


train_data_url = 'https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Data.zip'
train_labels_url = 'https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part3_GroundTruth.csv'

valid_data_url = 'https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Data.zip'
valid_labels_url = 'https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part3_GroundTruth.csv'

test_data_url = 'https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Data.zip'
test_labels_url = 'https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part3_GroundTruth.csv'

classes = ['melanoma', 'nevus', 'seborrheic_keratosis']

zip_urls = [train_data_url, valid_data_url, test_data_url]
csv_urls = [train_labels_url, valid_labels_url, test_labels_url]

# Download images

for url in zip_urls:
    with urlopen(url) as resp:
        print('Downloading {} ...'.format(url.split('/')[-1]))
        with ZipFile(BytesIO(resp.read())) as zip_file:
            zip_file.extractall('./download/')
        print('Done!')

# Create new directories

os.mkdir('data')
new_dirs = ['data/train', 'data/valid', 'data/test']

for path in new_dirs:
    os.mkdir(path)
    for i in range(len(classes)):
        os.mkdir(path + '/' + classes[i])


def transform(s):
    """
    Transforms 'Training' into 'train', 'Validation' into 'valid', and 'Test' into 'test'
    """
    if len(s) > 4:
        return s.lower()[:5]
    else:
        return s.lower()


# Load labels into dataframes

ground_truth = {}
for url in csv_urls:
    ground_truth[transform(url.split('_')[1])] = pd.read_csv(url)


def get_new_path(x):
    """
    Uses ground truth label to generate new location
    """
    img_id = x['image_id']
    m = x['melanoma']
    s = x['seborrheic_keratosis']
    n = 1.0 - (m + s)
    one_hot_label = [m, n, s]
    label = classes[one_hot_label.index(max(one_hot_label))]
    return label + '/' + img_id + '.jpg'


for url in zip_urls:

    old_dir = 'download/' + url.split('/')[-1][:-4]
    new_dir = 'data/' + transform(url.split('_')[1])

    df = ground_truth[transform(url.split('_')[1])]
    df['old_path'] = df.apply(lambda x: x['image_id'] + '.jpg', axis=1)
    df['new_path'] = df.apply(get_new_path, axis=1)

    print('Moving files to ' + new_dir)
    for _, row in df.iterrows():
        old_path = row['old_path']
        new_path = row['new_path']
        shutil.move(old_dir + '/' + old_path, new_dir + '/' + new_path)
    print('Done!')
