from util import color_conversion, coordinate_to_distance
from request import http_request, point_cloud
import time
import numpy as np


# Main function
def process_data_periodically():
    while True:
        # Retrieve point cloud data
        point_cloud_data = point_cloud.get_point_cloud_data()

        # Extract distances from point_cloud data
        distances = coordinate_to_distance.coordinate2distance(point_cloud_data)

        # Call the distance2color function
        colors = color_conversion.distance2color(distances)
        colors_2d = colors.reshape((100, 100))

        # Send the color request
        http_request.send_color_request(colors_2d)

        # Pause for 1 second
        time.sleep(1)

# Start the data processing
process_data_periodically()
