from zadanieB_12022022_validators_regex import remove_accents
from zadanieB_12022022_validators_regex import remove_special_char_beg_end
from zadanieB_12022022_validators_regex import remove_spec_char_inside_but_leave_some
import unittest


def make_valid(filename: str) -> str:

    a = remove_accents(filename)
    b = remove_special_char_beg_end(a)
    c = remove_spec_char_inside_but_leave_some(b)

    while ".." in c:
        c = c.replace("..", ".")

    if len(c) < 2:
        raise RuntimeError

    return c


print(make_valid(filename=".fef.3!@#$%543+_śłąśŚŻ)0-=.,/;'[]:46^%.."))


class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(make_valid('-.....dsęąą--....d@.'), 'dseaa--.d')

    def test_2(self):
        self.assertEqual(make_valid('..........1,*&^%-___-2..Ś'), '1-___-2.S')

    def test_3(self):
        self.assertEqual(make_valid('1.....1'), '1.1')

    def test_4(self):
        self.assertEqual(make_valid('...11..'), '11')

    def test_5(self):
        self.assertEqual(make_valid('abcd'), 'abcd')

