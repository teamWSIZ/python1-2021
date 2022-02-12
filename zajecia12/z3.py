import unittest


def find_longest_1sequence(w: list[int]) -> tuple[int, int]:
    lenmax = 0
    posmax = 0
    l = 0
    pos = 0
    for i in range(len(w)):
        if w[i] == 1:
            l += 1
        else:
            l = 0
            pos = i + 1
        if l > lenmax:
            lenmax = l
            posmax = pos
    return lenmax, posmax


class Z3Test(unittest.TestCase):

    def test_simple1(self):
        self.assertEqual(find_longest_1sequence([0, 1, 1, 0, 0, 0, 1, 1, 1]), (3, 6))

    def test_all_filled(self):
        self.assertEqual(find_longest_1sequence([1, 1, 1]), (3, 0))

    def test_2_times_1(self):
        self.assertEqual(find_longest_1sequence([1, 0, 1]), (1, 0))

    def test_long_seq(self):
        self.assertEqual(find_longest_1sequence([1, 1, 1, 1, 0, 1, 1, 1, 1, 1]), (5, 5))

    def test_no_sequences(self):
        self.assertEqual(find_longest_1sequence([0, 0, 0, 0]), (0, 0))


if __name__ == '__main__':
    unittest.main()
