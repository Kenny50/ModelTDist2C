# import unittest
# import numpy as np
# from src.util.color_conversion import distance2color

# class Distance2ColorTestCase(unittest.TestCase):
#     def test_distance2color(self):
#         distances = [0.0, 255.0]
#         expected_colors = [[255, 0, 0], [0, 0, 255]]
#         max_dist = 15.0

#         colors = distance2color(distances, max_dist)
#         self.assertEqual(colors, expected_colors)
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
