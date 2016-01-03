from lab19 import palindrome
import unittest


class Test(unittest.TestCase):
    def test_one(self):
        string1 = " iwroteanotherstupidtest "
        res = palindrome(string1)
        expected = "iroori"
        self.assertEquals(expected, res)

    def test_two(self):
        string1 = " saippuakivikauppias "
        res = palindrome(string1)
        expected = "saippuakivikauppias"
        self.assertEquals(expected, res)

    def test_three(self):
        string3 = " trt "
        res = palindrome(string3)
        expected = "trt"
        self.assertEquals(expected, res)

    def test_four(self):
        string4 = "r"
        res = palindrome(string4)
        expected = "r"
        self.assertEquals(expected, res)

    def test_five(self):
        string4 = "rtdbhi"
        res = palindrome(string4)
        expected = "r"
        self.assertEquals(expected, res)

    def test_six(self):
        string4 = " thhut "
        res = palindrome(string4)
        expected = "thht"
        self.assertEquals(expected, res)
