from reverseString import reverseString
import unittest

class TestReverseString(unittest.TestCase):
  def test_reverseString(self):
    str1 = reverseString("ab")
    self.assertEqual(str1, "ba")
    str2 = reverseString("kamel")
    self.assertEqual(str2, "lemak")
    str3 = reverseString("maradona")
    self.assertEqual(str3,"anodaram")

if __name__ == '__main__':
	unittest.main()