import unittest


def get_highest_number(w: list[int]) -> tuple[int, int]:
    index = 0
    max_ = w[index]
    for i in range(1, len(w)):
        if w[i] >= max_:
            max_ = w[i]
            index = i
    return max_, index


def get_lowest_number(w: list[int]) -> tuple[int, int]:
    u = [-i for i in w]
    e, idx = get_highest_number(u)
    return -e, idx


class Z2Test(unittest.TestCase):

    def test_simple1(self):
        self.assertEqual(get_lowest_number([5, 6, 8, 1, 2, 4]), (1, 3))

    def test_2_min_values(self):
        self.assertEqual(get_lowest_number([5, 1, 8, 1, 2, 8]), (1, 3))

    def test_2values(self):
        self.assertEqual(get_lowest_number([1, 2]), (1, 0))

    def test_2zeros(self):
        self.assertEqual(get_lowest_number([0, 0]), (0, 1))


if __name__ == '__main__':
    unittest.main()
