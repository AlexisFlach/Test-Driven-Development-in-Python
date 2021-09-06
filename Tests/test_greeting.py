from greeting import *
import unittest

class TestGreeting(unittest.TestCase):
  def test_greeting(self):
    msg = greeting("Alex")
    self.assertEqual(msg, "hello Alex")

if __name__ == '__main__':
	unittest.main()