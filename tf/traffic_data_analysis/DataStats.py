import os
import matplotlib.pyplot as plt
from tf.traffic_data_analysis.LoadData import load_training_data


images, labels = load_training_data()

print(images.ndim)
print(images.size)
print(images.flags)
print(images.itemsize)
print(images.nbytes)

plt.hist(labels, 62)
plt.show()
