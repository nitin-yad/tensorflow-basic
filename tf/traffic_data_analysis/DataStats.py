import os
from tf.traffic_data_analysis.LoadData import load_data


ROOT_PATH = '/Nitin/BelgiumTSDataSet/'
training_data_dir = os.path.join(ROOT_PATH, 'Training')

images, labels = load_data(training_data_dir)


print(images.ndim)
print(images.size)
print(images.flags)
print(images.itemsize)
print(images.nbytes)

