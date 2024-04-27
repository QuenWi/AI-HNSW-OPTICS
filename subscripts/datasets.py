import random
import numpy as np
from sklearn.datasets import make_blobs, make_moons, make_circles, make_classification, load_iris
from matplotlib import pyplot as plt

def dataset():
    matrix = [[0 for x in range(2)] for y in range(150)]
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            matrix[row][column] = random.randrange(-100, 100)
    return np.array(matrix, dtype=None, copy=False)

def dataset_2():
    data, n = make_blobs(n_samples=150, centers=4, n_features=2, random_state=0, cluster_std=0.3)
    return np.array(data, dtype=None, copy=False)

def dataset_3():
    data, n = make_moons(n_samples=150, noise=0.07)
    return np.array(data, dtype=None, copy=False)

def dataset_4():
    data, n = make_circles(n_samples=150, noise=0.1, factor=0.1)
    return np.array(data, dtype=None, copy=False)

def dataset_5():
    data, n = make_classification(n_samples=150, n_features=2, n_informative=2,n_redundant=0, n_repeated=0, n_classes=2, n_clusters_per_class=2,class_sep=2,flip_y=0,weights=[0.5,0.5], random_state=17)
    return np.array(data, dtype=None, copy=False)

def dataset_6():
    iris = load_iris()
    dataset = np.array(iris.data[:, :2])
    return dataset

def showPlot(matrix):
    plot = plt.scatter(x = matrix[:, 0], y = matrix[:, 1]) 
    plt.show()
    plt.clf()