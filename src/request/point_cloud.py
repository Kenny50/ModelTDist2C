import random

# Mock function for retrieving point cloud data
def get_point_cloud_data():
    # Replace this function with Redis client implementation to retrieve data from Redis channel
    # For now, we'll return a mock data
    # Set the dimensions and range of the data
    num_rows = 100
    num_cols = 100
    min_value = 0.0
    max_value = 10.0

    # Generate the mock data
    mock_data = []
    for _ in range(num_rows):
        row_data = []
        for _ in range(num_cols):
            data_point = {
                'x': round(random.uniform(min_value, max_value), 2),
                'y': round(random.uniform(min_value, max_value), 2),
                'z': round(random.uniform(min_value, max_value), 2)
            }
            row_data.append(data_point)
        # mock_data.append(row_data)
        mock_data.extend(row_data)
    return mock_data
