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
        data = {}
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.content)

            # Find sentence id
            data['sentence_id'] = soup.find(id='SentenceSentenceId').attrs['value']

            # Find sentences and translations
            sentences = soup.find_all('div', class_='sentenceContent')
            print type(sentences)
        print data

    ####################
    # Internal Methods #
    ####################
