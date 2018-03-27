import os
import skimage
import numpy as np

from skimage import data


def load_data(data_dir):
    dirs = [d for d in os.listdir(data_dir)
            if os.path.isdir(os.path.join(data_dir, d))]
    labels = []
    images = []
    for d in dirs:
        label_dir = os.path.join(data_dir, d)
        file_names = [os.path.join(label_dir, f)
                      for f in os.listdir(label_dir)
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return np.asarray(images), np.asarray(labels)


def main():
    ROOT_PATH = '/Nitin/BelgiumTSDataSet/'
    training_data_dir = os.path.join(ROOT_PATH, 'Training')
    testing_data_directory = os.path.join(ROOT_PATH, 'Testing')
    images, labels = load_data(training_data_dir)
    print(images.ndim)
    print(images.size)
    print(images[0])


if __name__ == "__main__":
    main()


