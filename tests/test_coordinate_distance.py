import unittest
import numpy as np
import time
from src.util.coordinate_to_distance import coordinate2distance
from src.request.point_cloud import get_point_cloud_data

class TestCoordinate2Distance(unittest.TestCase):

    def test_coordinate2distance(self):
        # Test case 1: Empty input
        data = []
        result = coordinate2distance(data)
        self.assertEqual(result, [])

        # Test case 2: Single point
        data = [{'x': 1, 'y': 2, 'z': 3}]
        result = coordinate2distance(data)
        self.assertEqual(result, [np.sqrt(1**2 + 2**2 + 3**2)])

        # Test case 3: Multiple points
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': -1, 'y': -2, 'z': -3}]
        result = coordinate2distance(data)
        expected = [np.sqrt(1**2 + 2**2 + 3**2), np.sqrt((-1)**2 + (-2)**2 + (-3)**2)]
        self.assertEqual(result, expected)
    
    def test_nest_sqrt_and_pow(self):

        # Test case 2: Single point, int
        data = [{'x': 1, 'y': 2, 'z': 3}]
        result = coordinate2distance(data)
        self.assertEqual(result, [np.sqrt(np.sqrt(1**2 + 2**2)**2 + 3**2)])

        # Test case 2: Single point, float
        data = [{'x': 1.2, 'y': 0.2, 'z': 0.3}]
        result = coordinate2distance(data)
        self.assertEqual(result, [np.sqrt(np.sqrt(1.2**2 + 0.2**2)**2 + 0.3**2)])

    def test_limit(self):
        # Test case 2: Single point, int
        data = [{'x': 0.0, 'y': 0.0, 'z': 0.0}]
        result = coordinate2distance(data)
        self.assertEqual(result, [0.0])

        # Test case 2: Single point, float
        data = [{'x': 10.0, 'y': 10.0, 'z': 10.0}]
        result = coordinate2distance(data)
        self.assertEqual([np.round(result,10)], [17.3205080757])

    def test_cost_time(self):
        data = [{'x': 1, 'y': 2, 'z': 3}] * 1000000  # Sample data with a large number of points

        start_time = time.time()
        result = coordinate2distance(data)
        end_time = time.time()
        execution_time = end_time - start_time

        # Assertions
        self.assertEqual(result, [np.sqrt(1**2 + 2**2 + 3**2)] * len(data))  # Example assertion
        print(f"Execution time: {execution_time} seconds")

    def test_cost_time_faker_data(self):
        data = get_point_cloud_data()  # Sample data with a large number of points

        start_time = time.time()
        result = coordinate2distance(data)
        end_time = time.time()
        execution_time = end_time - start_time

        # Assertions
        self.assertEqual([], [])  # Example assertion
        print(f"Execution time: {execution_time} seconds")

if __name__ == '__main__':
    unittest.main()
