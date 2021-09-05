from palindrome import palindrome
import unittest

class TestPalindrome(unittest.TestCase):
  def test_palindrome(self):
    name1 = palindrome("a")
    self.assertFalse(name1)

  
if __name__ == '__main__':
	unittest.main()