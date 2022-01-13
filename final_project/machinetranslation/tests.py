import unittest
from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english('Merci'), 'Bad')

class TestMyModule1(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french('Bad'), 'Merci')

unittest.main()