import matplotlib.pyplot as plt
import numpy as np

# Distance to color conversion function
def distance2color(distances, max_dist=15.0):
    """
    INPUT:
        disances: NDArray with shape(n,)
    """
    cmap = plt.cm.jet_r
    i = np.array(distances) / max_dist
    i = cmap(i)[:, 0 : 3]*255
    return i
    # rounded_colors = np.round(i, decimals=2) 
    # return rounded_colors.tolist()
