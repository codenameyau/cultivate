"""
Cultivate - test_scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from languages import scraper
import unittest

class TestTatoebaScraper(unittest.TestCase):
    """
    Test Suite: TatoebaScraper
    """

    def setUp(self):
        self.scraper = scraper.TatoebaScraper()

    def test_set_language(self):
        """
        Tests that languages are set correctly
        """
        # Test for default languages
        self.assertEqual(self.scraper.language_from, 'eng')
        self.assertEqual(self.scraper.language_to, 'jpn')

        # Test after setting supported languages
        self.scraper.set_languages('jpn', 'eng')
        self.assertEqual(self.scraper.language_from, 'jpn')
        self.assertEqual(self.scraper.language_to, 'eng')

        # Test after setting non-supported languages
        self.scraper.set_languages('eng', 'lol')
        self.assertEqual(self.scraper.language_from, 'jpn')
        self.assertEqual(self.scraper.language_to, 'eng')


if __name__ == '__main__':
    unittest.main()
