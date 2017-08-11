"""
test_last_word
"""
import unittest

from dougiebot import last_word

class TestLastWord(unittest.TestCase):
    """
    TestLastWord
    """

    def test_last_word(self):
        """
        test_last_word
        """
        self.assertEqual("hello", last_word("hello"))
        self.assertEqual("you", last_word("how are you????"))
        self.assertEqual(None, last_word(""))

if __name__ == '__main__':
    unittest.main()
