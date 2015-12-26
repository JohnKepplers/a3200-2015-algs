
import lab18
import unittest
class TestLevi(unittest.TestCase):
    def test_one(self):
      res = lab18.execute("Levenshtien", "Frankenstein")
      expected = 7
      self.assertEqual(expected, res)
    def test_two(self):
      res = lab18.execute("python", "shit")
      expected = 3
      self.assertEqual(expected, res)
