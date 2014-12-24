"""
Cultivate - scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
import requests
import bs4

class TatoebaScraper:

    def __init__(self):
        """
        Constructor: (String) -> TatoebaScraper
        Sets up the class data structures
        """
        # Define language settings
        self.language_from = 'eng'
        self.language_to = 'jpn'
        self.supported_languages = (
            'eng',
            'jpn',
        )

        # Define site path to scrape
        self.site_url = 'http://tatoeba.org/eng/sentences/show/' + self.language_to


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

    def get_random_sentence(self):
        """
        Public: None -> String
        Scrapes the site and finds target article
        """
        res = requests.get(self.site_url)
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.content)
            print soup.prettify()

    ####################
    # Internal Methods #
    ####################
