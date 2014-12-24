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
        self.data = {}
        self.soup = None


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

    def set_url(self, specified_url):
        """
        Public: (String) -> None
        Sets the site_url to specified url
        """
        self.site_url = specified_url

    def get_random_sentence(self):
        """
        Public: None -> String
        Scrapes the site and finds target article
        """
        res = requests.get(self.site_url)
        if res.status_code == 200:
            self.soup = bs4.BeautifulSoup(res.content)
            self._find_sentence_id()
            self._find_main_sentence()
            self._find_translations()
        print self.data

    ####################
    # Internal Methods #
    ####################
    def _find_sentence_id(self):
        """
        Internal: None -> None
        Stores the sentence id into data
        """
        self.data['sentence_id'] = self.soup.find(id='SentenceSentenceId').attrs['value']

    def _find_main_sentence(self):
        """
        Internal: None -> None
        Stores the main sentence into data
        """
        div = self.soup.find('div', class_='mainSentence')
        self.data['main_sentence'] = div.find('div', class_='text').string
        self.data['main_romaji'] = div.find('div', class_='romanization').attrs['title']

    def _find_translations(self):
        """
        Internal: None -> None
        Finds all additional translations and store in data
        """
        pass
