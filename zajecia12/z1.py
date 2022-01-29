"""
Dana jest lista int-ów, np. w=[5,6,8,1,2,4]
- znaleźć największy element listy, oraz pozycję na której występuje
(0-based, podać pozycję najbardziej z prawej strony, jeśli więcej elementów jest maksymalnych)
"""
from typing import List, Tuple


# def find_position_of_max(w: List[int]) -> Tuple[int, int]:
#     return (0, 0)

# def get_highest_number(numbers: list) -> tuple:
#     the_highest_number = max(numbers)
#     the_highest_number_index = numbers.rindex(the_highest_number)
#     return (the_highest_number, the_highest_number_index)

def get_the_highest_number(w: List[int]) -> Tuple[int, int]:
    index = 0
    max_ = w[index]

    for i in range(1, len(w)):
        if w[i] >= max_:
            max_ = w[i]
            index = i

    return max_, index


import unittest


class Z1Test(unittest.TestCase):

    def test_simple1(self):
        self.assertEqual(get_the_highest_number([5, 6, 8, 1, 2, 4]), (8, 2))

    def test_2_max_values(self):
        self.assertEqual(get_the_highest_number([5, 6, 8, 1, 2, 8]), (8, 5))

    def test_2values(self):
        self.assertEqual(get_the_highest_number([1, 2]), (2, 1))

    def test_2zeros(self):
        self.assertEqual(get_the_highest_number([0, 0]), (0, 1))


if __name__ == '__main__':
    unittest.main()
