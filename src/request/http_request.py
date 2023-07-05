import requests
import json

# HTTP request function
def send_color_request(colors):
    url = 'http://host.docker.internal:3000/d2color'
    data = {'colors': colors}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
    except requests.exceptions.HTTPError as err:
        print(f'Error sending color request. Status code: {err.response.status_code}')
    except requests.exceptions.RequestException as err:
        print(f'Error sending color request: {err}')
