import matplotlib.pyplot as plt
import numpy as np

# Distance to color conversion function
def distance2color(distances, max_dist=15.0):
    cmap = plt.cm.jet_r
    i = np.array(distances) / max_dist
    colors = cmap(i)
    extracted_colors = colors[:, 0:3]
    scaled_colors = extracted_colors * 255
    rounded_colors = np.round(scaled_colors, decimals=2)
    return rounded_colors.tolist()
