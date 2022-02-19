import unittest

from zajecia15.mountains import visible_mountain_landscape


class TestStringMethods(unittest.TestCase):

    def test_simple_2_mountain(self):
        res = visible_mountain_landscape([1, 2], [100, 1000])
        self.assertEqual(res, [0, 1])

    def test_original_test_case(self):
        res = visible_mountain_landscape([1, 2, 4, 8, 16], [5, 5, 24, 80, 160])
        self.assertEqual(res, [0, 2, 3])

    def test_same_angle(self):
        res = visible_mountain_landscape([1, 2], [10, 20])
        self.assertEqual(res, [0])

    def test_no_mountains(self):
        res = visible_mountain_landscape([], [])
        self.assertEqual(res, [])

    def test_himalaya(self):
        N = 10**6
        d = list(range(1, N+1))
        h = [d_ ** 2 for d_ in d]
        res = visible_mountain_landscape(d, h)
        self.assertEqual(len(res), N)
