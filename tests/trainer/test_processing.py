import unittest
from app.trainer.processing import Processing
from app.trainer.pt_br_mapper import UNICODE_ACCENTED_LETTERS

class TestProcessing(unittest.TestCase):

    def test_lower_case(self):
        tweet = Processing("Processing CAN Be LoWer Case TweeT").lower_case()

        self.assertEqual(tweet, "processing can be lower case tweet")

    def test_accented_letters(self):
        """Codes and values from UNICODE_ACCENTED_LETTERS"""

        text = "tweet with code {0} and another words"

        for code in UNICODE_ACCENTED_LETTERS.items():
            tweet = Processing(text.format(code[0])).accented_letters()
            self.assertEqual(tweet, text.format(code[1]))
