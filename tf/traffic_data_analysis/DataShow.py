import matplotlib.pyplot as plt
from tf.traffic_data_analysis.LoadData import load_training_data


def plot_few(images):
    # images, labels = load_training_data()
    traffic_signs = [300, 2250, 3650, 4000]

    for i in range(len(traffic_signs)):
        plt.subplot(1, 4, i+1)
        plt.axis('off')
        plt.imshow(images[traffic_signs[i]])
        plt.subplots_adjust(wspace=0.5)
    plt.show()


def main():
    images, labels = load_training_data()
    traffic_signs = [300, 2250, 3650, 4000]

    for i in range(len(traffic_signs)):
        plt.subplot(1, 4, i+1)
        plt.axis('off')
        plt.imshow(images[traffic_signs[i]])
        plt.subplots_adjust(wspace=0.5)
    plt.show()


if __name__ == "__main__":
    main()
