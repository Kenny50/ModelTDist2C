import numpy as np

def coordinate2distance(point_cloud_data):
    return [(item['x'] ** 2 + item['y'] ** 2 + item['z'] ** 2) ** 0.5 for item in point_cloud_data]