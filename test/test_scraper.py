"""
Cultivate - test_scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from languages import scraper
import unittest

class TestLanguagesScraper(unittest.TestCase):
    """
    Test Suite: LanguageScraper
    """

    def setUp(self):
        self.json_file = 'test/data/topics.json'
        self.scraper = scraper.LanguageScraper(self.json_file)
        self.expected_topics = ['house', 'cat']

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

    def test_load_topics(self):
        """
        Tests that topics are loaded from file
        """
        topics = self.scraper.topics
        self.assertListEqual(topics, self.expected_topics)
        self.assertEqual(len(topics), len(self.expected_topics))

    def test_get_random_topic(self):
        """
        Tests that a random topic is returned
        """
        random_topic = self.scraper.get_random_topic()
        self.assertTrue(random_topic in self.expected_topics)


if __name__ == '__main__':
    unittest.main()
