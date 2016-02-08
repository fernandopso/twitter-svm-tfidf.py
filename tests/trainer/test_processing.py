import unittest
from app.trainer.processing import Processing
from app.trainer.pt_br_mapper import UNICODE_ACCENTED_LETTERS

class TestProcessing(unittest.TestCase):

    def test_lower_case(self):
        tweet = Processing("Processing CAN Be LoWer Case TweeT").lower_case()

        self.assertEqual(tweet, "processing can be lower case tweet")

    def test_accented_letters(self):
        """Accentuation codes from UNICODE_ACCENTED_LETTERS"""

        text = "tweet with accent {0} and another words"

        for code in UNICODE_ACCENTED_LETTERS.items():
            text_parsed = text.format(code[0])
            text_result = text.format(code[1])

            text_proccessed = Processing(text_parsed).accented_letters()

            self.assertEqual(text_proccessed, text_result)
