import unittest
from app.trainer.processing import Processing

class TestStringMethods(unittest.TestCase):

  def test_lower_case(self):
      tweet = Processing("Processing Can Be Lower Case Tweet").lower_case()

      self.assertEqual(tweet, "processing can be lower case tweet")

if __name__ == '__main__':
    unittest.main()
