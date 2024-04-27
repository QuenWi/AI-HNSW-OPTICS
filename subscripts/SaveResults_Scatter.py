import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def showPlot(dataset, cluster):
    for group in cluster:
        rand_color = np.random.rand(3,)
        for obj in group:
            plot = plt.scatter(x = dataset[obj][0], y = dataset[obj][1], c=rand_color) 
    plt.show(plot)
    