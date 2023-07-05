import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import time


# Mock function for retrieving point cloud data
def get_point_cloud_data():
    # Replace this function with Redis client implementation to retrieve data from Redis channel
    # For now, we'll return a mock data
    mock_data = [
        {'x': 1.2, 'y': 0.3, 'z': 0.4},
        {'x': 5.1, 'y': 6.1, 'z': 7.4}
    ]
    return mock_data

# Distance to color conversion function
def distance2color(distances, max_dist=15.0):
    cmap = plt.cm.jet_r
    i = np.array(distances) / max_dist
    colors = cmap(i)
    extracted_colors = colors[:, 0:3]
    scaled_colors = extracted_colors * 255
    return scaled_colors.tolist()

# HTTP request function
def send_color_request(colors):
    url = 'http://host.docker.internal:3000/d2color'
    data = {'colors': colors}
    headers = {'Content-Type': 'application/json'}
    print('mock request')
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print('Color request sent successfully.')
    except requests.exceptions.HTTPError as err:
        print(f'Error sending color request. Status code: {err.response.status_code}')
    except requests.exceptions.RequestException as err:
        print(f'Error sending color request: {err}')
        
# Main function
def process_data_periodically():
    while True:
        print('test')
        # Retrieve point cloud data
        point_cloud = get_point_cloud_data()

        # Extract distances from point_cloud data
        distances = [np.sqrt(item['x'] ** 2 + item['y'] ** 2 + item['z'] ** 2) for item in point_cloud]

        # Call the distance2color function
        colors = distance2color(distances)

        # Send the color request
        send_color_request(colors)

        # Pause for 1 second
        time.sleep(1)

# Start the data processing
process_data_periodically()
