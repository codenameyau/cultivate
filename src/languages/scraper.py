"""
Cultivate - scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
import requests
import bs4

class LanguageScraper:

    def __init__(self):
        """
        Constructor: None -> None
        Sets up the class data structures
        """
        self.language_from = 'eng'
        self.language_to = 'jpn'
        self.supported_languages = set(
            'eng',
            'jpn',
        )

    def set_language(self, language_from, language_to):
        """
        Public: (String, String) -> None
        Sets the languages for the scraper
        """
        if language_from in self.supported_languages:
            self.language_from = language_from
        if language_to in self.supported_languages:
            self.language_to = language_to

