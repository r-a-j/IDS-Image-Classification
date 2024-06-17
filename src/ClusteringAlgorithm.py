# System Libraries
import os

# Third-Party Libraries
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

# Image Processing Libraries
from PIL import Image


class ClusteringAlgorithm:
    def __init__(self):
        pass

    @staticmethod
    def image_to_numpy_array(image):
        im = np.array(image)
        height = im.shape[0]
        width = im.shape[1]
        band_n = im.shape[2]
        numpy_arr = im.reshape(-1, band_n)
        return height, width, numpy_arr

    def k_means(self, pil_image, classes):
        height, width, x = self.image_to_numpy_array(pil_image)

        k_means = cluster.KMeans(classes)
        k_means.fit(x)

        x_classified = k_means.labels_
        result = x_classified.reshape(height, width)

        plt.figure(figsize=(12, 12))
        cmap = plt.get_cmap('jet', np.max(result) - np.min(result) + 1)
        plt.imshow(result, cmap=cmap)
        cax = plt.axes((0.92, 0.125, 0.02, 0.5))
        plt.colorbar(cax=cax)

        return self.get_plot()

    @staticmethod
    def get_plot():
        plt.tight_layout()
        home = os.getcwd()
        temp_folder = os.path.join(home, "data/temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        plot_path = os.path.join(temp_folder, 'plot.png')
        plt.savefig(plot_path)
        plt.close()
        return Image.open(plot_path)
