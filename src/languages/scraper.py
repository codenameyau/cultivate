"""
Cultivate - scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
import requests
import random
import json
import bs4

class LanguageScraper:

    def __init__(self, topics_file):
        """
        Constructor: (String) -> LanguageScraper
        Sets up the class data structures
        """
        # Define topics to study
        self.topics = []
        self.topics_file = topics_file
        self._load_topics()

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

    def get_random_topic(self):
        """
        Public: None -> String
        Returns a random topic from self.topics
        """
        return random.choice(self.topics)


    ####################
    # Internal Methods #
    ####################
    def _load_topics(self):
        """
        Internal: None -> None
        Loads the json content from topics
        """
        with open(self.topics_file, 'r') as json_file:
            self.topics = json.load(json_file)["topics"]

