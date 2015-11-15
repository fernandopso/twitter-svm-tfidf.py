import unittest
from app.trainer.processing import Processing

class TestStringMethods(unittest.TestCase):

    def test_lower_case(self):
        tweet = Processing("Processing Can Be Lower Case Tweet").lower_case()

        self.assertEqual(tweet, "processing can be lower case tweet")

    def test_accented_letters(self):
        """Codes and values from UNICODE_ACCENTED_LETTERS"""

        tweet = Processing("tweet with code \u00e0").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00e1").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00e2").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00e3").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00e4").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00c1").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00c2").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00c3").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00c4").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00c5").accented_letters()
        self.assertEqual(tweet, "tweet with code a")

        tweet = Processing("tweet with code \u00e7").accented_letters()
        self.assertEqual(tweet, "tweet with code c")

        tweet = Processing("tweet with code \u00c7").accented_letters()
        self.assertEqual(tweet, "tweet with code c")

        tweet = Processing("tweet with code \u00e8").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00e9").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00ea").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00eb").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00c8").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00c9").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00ca").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00cb").accented_letters()
        self.assertEqual(tweet, "tweet with code e")

        tweet = Processing("tweet with code \u00ec").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00ed").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00ee").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00ef").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00cd").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00cc").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00ce").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00cf").accented_letters()
        self.assertEqual(tweet, "tweet with code i")

        tweet = Processing("tweet with code \u00f2").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00f3").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00f4").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00f5").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00f6").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00d2").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00d3").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00d4").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00d5").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00d6").accented_letters()
        self.assertEqual(tweet, "tweet with code o")

        tweet = Processing("tweet with code \u00f1").accented_letters()
        self.assertEqual(tweet, "tweet with code n")

        tweet = Processing("tweet with code \u00d1").accented_letters()
        self.assertEqual(tweet, "tweet with code n")

        tweet = Processing("tweet with code \u00f9").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00fa").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00fb").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00fc").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00d9").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00da").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00db").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

        tweet = Processing("tweet with code \u00dc").accented_letters()
        self.assertEqual(tweet, "tweet with code u")

if __name__ == '__main__':
    unittest.main()
