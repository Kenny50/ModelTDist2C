import redis
import requests
import json
import matplotlib.pyplot as plt
import numpy as np

# Redis connection
r = redis.Redis()

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
    print('request')
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print('Color request sent successfully.')
    except requests.exceptions.HTTPError as err:
        print(f'Error sending color request. Status code: {err.response.status_code}')
    except requests.exceptions.RequestException as err:
        print(f'Error sending color request: {err}')

# Redis message handler
def message_handler(message):
    data = json.loads(message['data'])
    point_cloud = data['point_cloud']
    distances = [np.sqrt((np.sqrt(item['x']**2 + item['y']**2))**2 + item['z']**2) for item in point_cloud]
    colors = distance2color(distances)
    send_color_request(colors)

# Redis subscription
p = r.pubsub()
p.subscribe(**{'point_cloud': message_handler})
thread = p.run_in_thread(sleep_time=0.001)

# Keep the server running until interrupted
try:
    while True:
        pass
except KeyboardInterrupt:
    thread.stop()
