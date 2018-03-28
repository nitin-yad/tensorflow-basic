import matplotlib.pyplot as plt
from tf.traffic_data_analysis.LoadData import load_training_data
from tf.traffic_data_analysis.DataShow import plot_few
from skimage import transform


def main():
    images, labels = load_training_data()
    scaled_images = [transform.resize(image, (28, 28)) for image in images]
    plot_few(scaled_images)

if __name__ == "__main__":
    main()
