from util import color_conversion, coordinate_to_distance, three_to_two
from request import http_request, point_cloud
import time
import numpy as np


# Main function
def process_data_periodically():
    while True:
        # Retrieve point cloud data
        # point_cloud_data = point_cloud.get_point_cloud_data()

        # Extract distances from point_cloud data
        # distances = coordinate_to_distance.coordinate2distance(point_cloud_data)
        three_to_two.A += three_to_two.theta_spacing
        three_to_two.B += three_to_two.phi_spacing
        mock_coordinate = three_to_two.donut(three_to_two.A,three_to_two.B)
        mock_distances = coordinate_to_distance.coordinate2distance(mock_coordinate)
        # Call the distance2color function
        # colors = color_conversion.distance2color(distances)
        mock_colors = color_conversion.distance2color(mock_distances)

        zipped_data = []

        for coord, color in zip(mock_coordinate, mock_colors):
            coord['color'] = color
            zipped_data.append(coord)
        
        # Send the color request
        http_request.send_color_request(zipped_data)
        # Pause for 1 second
        time.sleep(1)

# Start the data processing
process_data_periodically()
