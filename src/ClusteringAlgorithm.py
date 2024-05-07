from PIL import Image
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt
import os

class ClusteringAlgorithm:

    def image_to_numpy_array(image):
        im = np.array(image)
        height = im.shape[0]
        width = im.shape[1]
        band_n = im.shape[2]
        numpy_arr = im.reshape(-1, band_n)
        return height, width, numpy_arr
    
    def k_means(self, image, classes):
        
        height, width, X = ClusteringAlgorithm.image_to_numpy_array(image)
        
        k_means = cluster.KMeans(classes)
        k_means.fit(X)
        
        X_classified = k_means.labels_
        result = X_classified.reshape(height, width)
        
        data_folder = os.path.join(os.getcwd(), "IDS-Image-Classification/data/temp")
        
        plt.figure(figsize=(12,12))
        cmap = plt.get_cmap('jet', np.max(result) - np.min(result) + 1)
        
        plt.imshow(result, cmap=cmap)
        
        cax = plt.axes([0.92, 0.125, 0.02, 0.5])
        plt.colorbar(cax=cax)
        
        plot_path = os.path.join(data_folder, 'plot.png')
        plt.savefig(plot_path)
        plt.close()
        
        plot_image = Image.open(plot_path)
        return plot_image