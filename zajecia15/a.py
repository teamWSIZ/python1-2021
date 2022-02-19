import string
import unittest

import unidecode


def remove_accents(string):
    # removes accents-> ł->l, ń-n etc
    str_decoded = unidecode.unidecode(string)

    return str_decoded


def remove_polish_chars(s: str):
    fr_ = 'ąćęłźżóś'
    to_ = 'acelzzos'
    d = dict()
    for f, t in zip(fr_, to_):
        d[f] = t
    res = []
    for c in s:
        if c in d:
            res.append(d[c])
        else:
            res.append(c)
    return ''.join(res)


def make_valid(filename: str):
    filename = remove_accents(filename)
    special = ['_', '.', '-']
    # whitelist chars
    whitelisted = []
    for c in filename:
        if c in string.ascii_letters or c in special or c in string.digits:
            whitelisted.append(c)
    # no ..
    whitelisted = ''.join(whitelisted)
    print('***', whitelisted)
    while '..' in whitelisted:
        whitelisted = whitelisted.replace('..', '.')
    print(whitelisted)
    # two-pointers ....
    L = 0
    while L < len(whitelisted) and whitelisted[L] in special:
        L += 1
    R = len(whitelisted) - 1
    while R >= 0 and whitelisted[R] in special:
        R -= 1
    print(L,R)
    result = whitelisted[L:R + 1]
    return ''.join(result)


class TestStringMethods(unittest.TestCase):

    def test_t1(self):
        self.assertEqual('abcd', make_valid('abcd'))

    def test_t2(self):
        self.assertEqual('abcd', make_valid('ąbcd'))

    def test_t3(self):
        self.assertEqual('abcd', make_valid('ab@@@@@cd'))

    def test_t4(self):
        self.assertEqual('ab-._cd', make_valid('ab-._cd'))

    def test_t5(self):
        self.assertEqual('ab-._cd', make_valid('ab-._cd__'))

    def test_t6(self):
        self.assertEqual('a.a', make_valid('a....a'))

    def test_t7(self):
        self.assertEqual('AAS', make_valid('AAS'))

    def test_1(self):
        self.assertEqual('dseaa--.d', make_valid('-.....dsęąą--....d@.'))

    def test_2(self):
        self.assertEqual('1-___-2.S', make_valid('..........1,*&^%-___-2..Ś'))

    def test_3(self):
        self.assertEqual('1.1', make_valid('1.....1'))

    def test_4(self):
        self.assertEqual('11', make_valid('...11..'))

# if __name__ == '__main__':
# print(unidecode.unidecode('piątka'))  # piatka
# print(unidecode.unidecode('selbstständig'))  # selbststandig
# print(unidecode.unidecode('Федеральный'))  # Federal'nyi
# print(unidecode.unidecode('又称联邦总理'))  # pinyin 'You Cheng Lian Bang Zong Li'
# print(remove_polish_chars('piątkać'))

# print(string.ascii_letters)
# print(string.digits)
