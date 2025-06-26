import unittest
from file import *

class MyTestClass(unittest.TestCase):
    
    def test_vowel_count(self):
        self.assertEqual(3, countVowels("aeityr"))


if __name__ == '__main__':
    unittest.main()
