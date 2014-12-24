"""
Cultivate - scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
import requests
import random
import json
import bs4

class TatoebaScraper:

    def __init__(self):
        """
        Constructor: (String) -> TatoebaScraper
        Sets up the class data structures
        """
        # Define site path to scrape
        self.site_url = 'http://tatoeba.org/eng/sentences/search/'

        # Define language settings
        self.language_from = 'eng'
        self.language_to = 'jpn'
        self.supported_languages = (
            'eng',
            'jpn',
        )


    ##################
    # Public Methods #
    ##################
    def set_languages(self, language_from, language_to):
        """
        Public: (String, String) -> None
        Sets the languages for the scraper
        """
        if language_from in self.supported_languages \
            and language_to in self.supported_languages:
            self.language_from = language_from
            self.language_to = language_to

    def retrieve_content(self, topic):
        """
        Public: (String) -> String
        Returns the HTML from request
        """
        pass


    ####################
    # Internal Methods #
    ####################
    def _build_query_url(self, topic):
        """
        Internal: (String) -> String
        Returns the url for scraping
        """
        # First find out how many pages
        pass
