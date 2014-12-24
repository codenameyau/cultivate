"""
Cultivate - test_scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from languages import scraper
import unittest

class TestLanguagesScraper(unittest.TestCase):

    def setUp(self):
        pass

    def test_scraper(self):
        self.assertEqual(scraper.print_test(), 1)


if __name__ == '__main__':
    unittest.main()
