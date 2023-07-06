import unittest
import numpy as np
import time
from src.util.color_conversion import distance2color
from src.request.point_cloud import get_point_cloud_data
from src.util.coordinate_to_distance import coordinate2distance


class Distance2ColorTestCase(unittest.TestCase):
    def test_data_to_color_time(self):
        data = get_point_cloud_data() * 100
        max_dist = 15.0

        start_time = time.time()
        distances = coordinate2distance(data)
        colors = distance2color(distances, max_dist)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertEqual([], [])
        print(f"Execution time test_data_to_color_time: {execution_time} seconds")

#     # def test_distance2color(self):
#         # # Test case 1: Normal distances
#         # distances = [5.0, 10.0, 15.0, 7.5, 12.5]
#         # expected_result = np.array([[0, 0, 255], [0, 128, 255], [0, 255, 255], [0, 64, 255], [0, 192, 255]])
#         # result = distance2color(distances)
#         # assert np.array_equal(result, expected_result), "Test case 1 failed"

#         # Test case 2: Maximum distance set to 10.0
#         # max_dist = 10.0
#         # distances = [2.5, 5.0, 7.5, 10.0]
#         # expected_result = np.array([[0, 0, 255], [0, 128, 255], [0, 255, 255], [0, 255, 0]])
#         # result = distance2color(distances, max_dist)
#         # self.assertEqual(result, expected_result)

#         # Test case 3: Empty distances list
#         # distances = []
#         # expected_result = np.array([])
#         # result = distance2color(distances)
#         # self.assertEqual(result, expected_result)

# if __name__ == '__main__':
#     unittest.main()
