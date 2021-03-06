"""
Cultivate - test_scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from tatoeba import scraper
import unittest

class TestTatoebaScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = scraper.TatoebaScraper()
        self.scraper.set_url('http://tatoeba.org/eng/sentences/show/94899')

    def test_set_language(self):
        """
        Tests that languages are set correctly
        """
        # Test for default languages
        self.assertEqual(self.scraper.language_original, 'jpn')
        self.assertEqual(self.scraper.language_translated, 'eng')

        # Test after setting supported languages
        self.scraper.set_languages('jpn', 'eng')
        self.assertEqual(self.scraper.language_translated, 'jpn')
        self.assertEqual(self.scraper.language_original, 'eng')

        # Test after setting non-supported languages
        self.scraper.set_languages('eng', 'lol')
        self.assertEqual(self.scraper.language_translated, 'jpn')
        self.assertEqual(self.scraper.language_original, 'eng')

if __name__ == '__main__':
    unittest.main()
