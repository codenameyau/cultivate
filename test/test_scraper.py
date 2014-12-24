"""
Cultivate - test_scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from languages import scraper
import unittest

class TestTatoebaScraper(unittest.TestCase):

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

    def test_get_random_sentece(self):
        """
        Tests that a random sentence is returned
        """
        self.scraper.get_random_sentence()
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
