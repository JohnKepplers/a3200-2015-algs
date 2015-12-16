__author__ = 'alexkane'

import unittest
import lab20

class TestIlya(unittest.TestCase):
     def test_trivial0(self):
         expected = 0
         res = lab20.execute(4, [2, 3, 5, 2])
         self.assertEqual(expected, res)

     def test_trivial1(self):
         expected = 8
         res = lab20.execute(4, [2, 2, 4, 4])
         self.assertEqual(expected, res)

     def test_trivial2(self):
         expected = 2222222222
         res = lab20.execute(9, [1111111111, 1, 3, 200, 100, 7, 1111111111, 2, 2])
         self.assertEqual(expected, res)